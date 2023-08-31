import calendar
from datetime import date
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count

from .models import Period, GlobalInputs
from payroll.models import EmployeeSavingSchemeEntries, EmployeeTransactionEntries, Paymaster
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

        for employee in employees:
            total_allowances = EmployeeTransactionEntries.objects.filter(
                employee=employee, transaction_type=TransactionType.ALLOWANCE
            ).aggregate(amount=Sum("amount"))["amount"]
            total_deductions = EmployeeTransactionEntries.objects.filter(
                employee=employee, transaction_type=TransactionType.DEDUCTION
            ).aggregate(amount=Sum("amount"))["amount"]
            employee_basic = employee.annual_basic
            gross_income = employee_basic + total_allowances
            net_income = gross_income - total_deductions
            company = instance.company

            paymatser, _ = Paymaster.objects.get_or_create(
                period=instance,
                allowances = total_allowances,
                deductions=total_deductions,
                gross_salary=gross_income,
                net_salary=net_income,
                company=company,
                employee=employee,
                basic_salary=employee_basic
            )
            paymatser.save()
