from decimal import Decimal
from datetime import date
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count, Q

from .models import Period, GlobalInputs
from payroll.models import (
    EmployeeSavingSchemeEntries,
    EmployeeTransactionEntries,
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

    if instance.status == 1 and instance.process == True:
        employees = Employee.objects.filter(company_id=instance.company)
        company = instance.company
        processing_user = instance.user_process_id

        for employee in employees:
            entries = EmployeeTransactionEntries.objects.filter(
                Q(start_period__start_date__lt=instance.start_date, recurrent=True)
                |Q(start_period__start_date__lte=instance.start_date, recurrent=True)
                | Q(recurrent=True)
                | Q(end_period__end_date__lte=instance.end_date),
                employee=employee,
                company=company,
            )

            total_allowances = entries.filter(
                transaction_type=TransactionType.ALLOWANCE,
            ).aggregate(amount=Sum("amount"))["amount"]
            total_deductions = entries.filter(
                transaction_type=TransactionType.DEDUCTION,
             
            ).aggregate(amount=Sum("amount"))["amount"]

            employee_basic = Decimal(employee.annual_basic)
            if total_allowances is not None:
                gross_income = employee_basic + total_allowances
            elif total_allowances is None:
                total_allowances = 0.0
                gross_income = employee_basic
            if total_deductions is not None:
                net_income = gross_income - total_deductions
            elif total_deductions is None:
                total_deductions = 0.0
                net_income = gross_income 

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
                paymaster.user_id = processing_user

            paymaster.save()
