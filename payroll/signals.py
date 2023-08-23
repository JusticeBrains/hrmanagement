from decimal import Decimal
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from employee.models import Employee, PayGroup
from company.models import JobTitles
from .models import (
    EmployeeSavingSchemeEntries,
    SavingSchemeEntries,
    TransactionEntries,
    EmployeeTransactionEntries,
)
from options.text_options import DisbursementType


@receiver(post_save, sender=SavingSchemeEntries)
def create_employee_saving_scheme(sender, instance, **kwargs):
    """
    Create or update EmployeeSavingSchemeEntries objects based on the disbursement_type of the SavingSchemeEntries instance.
    """
    if instance:
        disbursement_type = instance.disbursement_type
        saving_scheme_name = instance.saving_scheme_name
        recurrent = instance.recurrent
        start_period_code = instance.start_period_code
        end_period_code = instance.end_period_code
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company
        status = instance.status

        def create_or_update_employee_saving_scheme_entry(
            employee, employee_name, employee_per, employer_per
        ):
            """
            Create or update EmployeeSavingSchemeEntries object for the given employee.
            """
            save_entry, created = EmployeeSavingSchemeEntries.objects.get_or_create(
                saving_scheme=instance,
                employee=employee,
                saving_scheme_name=saving_scheme_name,
                employee_name = employee_name,
                company_name = company_name,
                defaults={
                    "recurrent":recurrent,
                    "start_period_code":start_period_code,
                    "end_period_code":end_period_code,
                    "user_id":user_id,
                    "company_name":company_name,
                    "employee_name":employee_name,
                    "status":status,
                    "employee_contribution":employee_per,
                    "employer_contribution":employer_per,
                },
            )

            if not created:
                save_entry.recurrent = recurrent
                save_entry.start_period_code = start_period_code
                save_entry.end_period_code = end_period_code
                save_entry.user_id = user_id
                save_entry.status = status
                save_entry.employee_contribution = employee_per
                save_entry.employer_contribution = employer_per
                save_entry.save()

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )

        elif disbursement_type == DisbursementType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )

        elif disbursement_type == DisbursementType.JOB_TITLE:
            job_title = JobTitles.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )

                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )


@receiver(post_save, sender=TransactionEntries)
def create_employee_transaction(sender, instance, **kwargs):
    """
    Create or update EmployeeTransactionEntries objects based on the disbursement_type of the TransactionEntries instance.
    """
    if instance:
        disbursement_type = instance.disbursement_type
        recurrent = instance.recurrent
        start_period_code = instance.start_period_code
        end_period_code = instance.end_period_code
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company
        status = instance.status
        transaction_type = instance.transaction_type
        contribute_to_ssf = instance.contribute_to_ssf
        taxable = instance.taxable
        percentage_of_basic = instance.percentage_of_basic
        amount = instance.amount
        transaction_entry_name = instance.transaction_entry_name

        def create_or_update_employee_transaction_entry(employee, employee_name):
            """
            Create or update EmployeeTransactionEntries object for the given employee.
            """
            save_entry, created = EmployeeTransactionEntries.objects.get_or_create(
                transaction_entry=instance,
                transaction_entry_name=transaction_entry_name,
                company_name=company_name,
                employee=employee,
                employee_name=employee_name,

                defaults={
                "recurrent":recurrent,
                "start_period_code":start_period_code,
                "end_period_code":end_period_code,
                "user_id":user_id,
                "transaction_type":transaction_type,
                "amount":amount,
                "contribute_to_ssf":contribute_to_ssf,
                "taxable":taxable,
                "status":status,
                }
            )

            if not created:
                save_entry.recurrent = recurrent
                save_entry.start_period_code = start_period_code
                save_entry.end_period_code = end_period_code
                save_entry.user_id = user_id
                save_entry.status = status
                save_entry.transaction_type = transaction_type
                save_entry.amount = amount
                save_entry.contribute_to_ssf = contribute_to_ssf
                save_entry.taxable = taxable
                save_entry.save()

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.JOB_TITLE:
            job_title = JobTitles.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                create_or_update_employee_transaction_entry(employee, employee_name)
