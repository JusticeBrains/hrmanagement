from pprint import pprint
from decimal import Decimal
from django.db import transaction
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum, Q, F

from .models import Period, GlobalInputs
from payroll.models import (
    EmployeeLoanPayment,
    EmployeeSavingSchemeEntries,
    EmployeeTransactionEntries,
    LoanEntries,
    Paymaster,
)
from employee.models import Employee
from options.text_options import TransactionType


@receiver(pre_save, sender=Period)
def populate_date(sender, instance, **kwargs):
    if instance and instance.status == 1:
        current_period = instance
        current_year = instance.period_year.year
        total_working_hours = Period.objects.filter(
            period_year=instance.period_year, company=instance.company
        ).aggregate(total_working_hours=Sum("total_working_hours"))[
            "total_working_hours"
        ]

        global_input, _ = GlobalInputs.objects.get_or_create(
            current_period=current_period,
            current_year=current_year,
            annual_working_hours=total_working_hours,
            company=instance.period_year.company,
        )
        global_input.save()


@receiver(pre_save, sender=Period)
def process_payroll(sender, instance, **kwargs):
    if (instance.status == 1 or instance.status == 2) and instance.process:
        company = instance.company
        processing_user = instance.user_process_id

        employees = Employee.objects.filter(company_id=company)
        loan_entries = LoanEntries.objects.prefetch_related(
            "employee", "company"
        ).filter(
            status=True,
            closed=False,
            company=company,
        )
        saving_scheme = EmployeeSavingSchemeEntries.objects.prefetch_related(
            "employee", "company"
        ).filter(recurrent=True, status=True)

        total_loan_deductions = 0
        with transaction.atomic():
            for employee in employees:
                # Fetch entries for the employee once, instead of multiple times in the loop
                payslip = []

                entries = (
                    EmployeeTransactionEntries.objects.select_related(
                        "employee", "company"
                    )
                    .filter(
                        Q(
                            Q(
                                start_period__start_date__lte=instance.start_date,
                                recurrent=True,
                            )
                            | Q(recurrent=True)
                            | Q(end_period__end_date__lte=instance.end_date),
                            employee=employee,
                            company=company,
                        )
                    )
                    .exclude(
                        Q(
                            Q(start_period__start_date__lt=instance.start_date)
                            & Q(end_period__end_date__lte=instance.start_date)
                        )
                        | Q(end_period__end_date__lte=instance.start_date)
                    )
                )

                total_allowances = entries.filter(
                    transaction_type=TransactionType.ALLOWANCE
                ).aggregate(amount=Sum("amount"))["amount"] or Decimal(0)
                total_deductions = entries.filter(
                    transaction_type=TransactionType.DEDUCTION
                ).aggregate(amount=Sum("amount"))["amount"] or Decimal(0)

                employee_basic = Decimal(employee.annual_basic)
                gross_income = employee_basic + total_allowances

                # Calculate loan deductions for this employee
                loan_dict = []
                for emp_loan in loan_entries:
                    if emp_loan.employee == employee:
                        monthly_amount = emp_loan.monthly_repayment
                        amount_to_be_paid = (
                            min(monthly_amount, emp_loan.total_amount_paid)
                            if emp_loan.total_amount_paid is not None
                            else monthly_amount
                        )
                        if instance.status == 2:
                            if emp_loan.total_amount_paid is not None:
                                emp_loan.total_amount_paid += amount_to_be_paid
                                emp_loan.monthly_repayment = amount_to_be_paid
                            else:
                                emp_loan.total_amount_paid = amount_to_be_paid
                                emp_loan.monthly_repayment = amount_to_be_paid
                            emp_loan.save()
                        loan_dict.append(
                            {
                                "loan_name": emp_loan.loan_name,
                                "amount_paid": float(amount_to_be_paid),
                                "total_amount_paid": float(
                                    emp_loan.total_amount_paid
                                ),
                            }
                        )

                        total_loan_deductions += amount_to_be_paid

                        if emp_loan.total_amount_paid == emp_loan.amount:
                            emp_loan.closed = True
                            emp_loan.save()
                    

                net_income = gross_income - (total_deductions + total_loan_deductions)
                total_deductions += (
                    total_loan_deductions if total_loan_deductions is not None else 0
                )
                employee.net_salary = net_income
                employee.gross_salary = gross_income
                payslip.append(
                    {
                        "basic_salary": float(employee_basic),
                        "gross_salary": float(gross_income),
                        "net_salary": float(net_income),
                        "total_deductions": float(total_deductions),
                        "total_allowances": float(total_allowances),
                        "total_loan_deductions": float(total_loan_deductions),
                        "loans": loan_dict,
                    }
                )
                employee.save()
                
                paymaster, created = Paymaster.objects.get_or_create(
                    period=instance,
                    company=company,
                    employee=employee,
                    defaults={
                        "allowances": total_allowances,
                        "deductions": total_deductions,
                        "gross_salary": gross_income,
                        "net_salary": net_income,
                        "basic_salary": employee_basic,
                        "payslip": payslip,
                        "user_id": processing_user,
                    },
                )
                # Update attributes if the Paymaster instance already existed
                if not created:
                    paymaster.allowances = total_allowances
                    paymaster.deductions = total_deductions
                    paymaster.gross_salary = gross_income
                    paymaster.net_salary = net_income
                    paymaster.basic_salary = employee_basic
                    paymaster.payslip = payslip
                    paymaster.user_id = processing_user
            paymaster.save()
