from decimal import Decimal
from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from employee.models import Employee, PayGroup
from company.models import JobTitles
from .models import (
    EmployeeSavingSchemeEntries,
    SavingSchemeEntries,
    TransactionEntries,
    EmployeeTransactionEntries,
    ShiftEntries,
    EmployeeShiftEntries
)
from options.text_options import DisbursementType


@receiver(post_save, sender=SavingSchemeEntries)
def create_employee_saving_scheme(sender, instance, **kwargs):
    """
    Create or update EmployeeSavingSchemeEntries objects based on the disbursement_type of the SavingSchemeEntries instance.
    """
    post_save.disconnect(create_employee_saving_scheme, sender=SavingSchemeEntries)
    if instance:
        disbursement_type = instance.disbursement_type
        saving_scheme_name = instance.saving_scheme_name
        recurrent = instance.recurrent
        start_period_code = instance.start_period_code
        start_period = instance.start_period
        end_period_code = instance.end_period_code
        end_period = instance.end_period
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company
        status = instance.status
        
        @transaction.atomic
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
                    "start_period":start_period,
                    "start_period_code":start_period_code,
                    "end_period":end_period,
                    "end_period_code":end_period_code,
                    "user_id":user_id,
                    "company_name":company_name,
                    "employee_name":employee_name,
                    "employee_code": employee_code,
                    "status":status,
                    "employee_contribution":employee_per,
                    "employer_contribution":employer_per,
                    "company": company
                },
            )

            if not created:
                save_entry.recurrent = recurrent
                save_entry.start_period_code = start_period_code
                save_entry.start_period = start_period
                save_entry.end_period = end_period
                save_entry.end_period_code = end_period_code
                save_entry.user_id = user_id
                save_entry.status = status
                save_entry.employee_contribution = employee_per
                save_entry.employer_contribution = employer_per
                save_entry.employee_code = employee_code
                save_entry.company = company
                save_entry.save()

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)

            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                instance.global_name = employee.company
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )

        elif disbursement_type == DisbursementType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.global_id)
            instance.global_name = pay_group.no

            employees = Employee.objects.filter(
                company_id=company, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
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
            instance.global_name = job_title.description
            employees = Employee.objects.filter(
                company_id=company, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_per = float(
                employee_code = employee.code
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                instance.global_name = employee.job_title_description
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                employee_per = float(
                    (instance.percentage_of_employee_basic / 100) * employee_basic
                )
                employer_per = float(
                    (instance.percentage_of_employer_basic / 100) * employee_basic
                )
                instance.global_name = employee_name
                create_or_update_employee_saving_scheme_entry(
                    employee, employee_name, employee_per, employer_per
                )
        instance.save()
    post_save.connect(create_employee_saving_scheme, sender=SavingSchemeEntries)


@receiver(post_save, sender=TransactionEntries)
def create_employee_transaction(sender, instance, **kwargs):
    """
    Create or update EmployeeTransactionEntries objects based on the disbursement_type of the TransactionEntries instance.
    """
    post_save.disconnect(create_employee_transaction, sender=TransactionEntries)
    if instance:
        disbursement_type = instance.disbursement_type
        recurrent = instance.recurrent
        start_period_code = instance.start_period_code
        start_period = instance.start_period
        end_period = instance.end_period
        end_period_code = instance.end_period_code
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company
        status = instance.status
        transaction_type = instance.transaction_type
        contribute_to_ssf = instance.contribute_to_ssf
        taxable = instance.taxable
        percentage_of_basic = instance.percentage_of_basic
        transaction_entry_name = instance.transaction_name
        company = instance.company

        @transaction.atomic
        def create_or_update_employee_transaction_entry(employee, employee_name):
            """
            Create or update EmployeeTransactionEntries object for the given employee.
            """
            save_entry, created = EmployeeTransactionEntries.objects.get_or_create(
                transaction_entry=instance,
                transaction_entry_name=transaction_entry_name,
                company_name=company_name,
                company=company,
                employee=employee,
                employee_name=employee_name,
                employee_code=employee_code,
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
                "start_period": start_period,
                "end_period": end_period,
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
                save_entry.start_period = start_period
                save_entry.end_period = end_period
                save_entry.save()

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                instance.global_name = employee.company
                if percentage_of_basic is not None:
                    amount = (percentage_of_basic/100) * employee_basic
                elif percentage_of_basic is None:
                    amount = instance.amount
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.global_id)
            instance.global_name = pay_group.no

            employees = Employee.objects.filter(
                company_id=company, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                if percentage_of_basic is not None:
                    amount = (percentage_of_basic/100) * employee_basic
                elif percentage_of_basic is None:
                    amount = instance.amount
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.JOB_TITLE:
            job_title = JobTitles.objects.get(id=instance.global_id)
            instance.global_name = job_title.description
            employees = Employee.objects.filter(
                company_id=company, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                if percentage_of_basic is not None:
                    amount = (percentage_of_basic/100) * employee_basic
                elif percentage_of_basic is not None:
                    amount = instance.amount
                create_or_update_employee_transaction_entry(employee, employee_name)

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                instance.global_name = employee_name
                employee_basic = Decimal(employee.annual_basic)
                employee_code = employee.code
                if percentage_of_basic is not None:
                    amount = (percentage_of_basic/100) * employee_basic
                elif percentage_of_basic is None:
                    amount = instance.amount
                create_or_update_employee_transaction_entry(employee, employee_name)
        instance.save()

    post_save.connect(create_employee_transaction, sender=TransactionEntries)
        

@receiver(post_save, sender=ShiftEntries)
def create_employee_shift_entry(sender, instance, **kwargs):
    """
    Create or update EmployeeSavingSchemeEntries objects based on the disbursement_type of the SavingSchemeEntries instance.
    """
    if instance:
        disbursement_type = instance.disbursement_type
        shift_name = instance.shift_name
        recurrent = instance.recurrent
        period = instance.period
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company
        status = instance.status

        @transaction.atomic
        def create_or_update_employee_shift_entry(
            employee, employee_name
        ):
            """
            Create or update EmployeeSavingSchemeEntries object for the given employee.
            """
            save_entry, created = EmployeeShiftEntries.objects.get_or_create(
                shift_code=instance,
                shift_name=shift_name,
                employee=employee,
                employee_name = employee_name,
                company = company,
                defaults={
                    "recurrent":recurrent,
                    "period":period,
                    "user_id":user_id,
                    "company_name":company_name,
                    "employee_name":employee_name,
                    "employee_code":employee_code,
                    "status":status,
                },
            )

            if not created:
                save_entry.period = period
                save_entry.user_id = user_id
                save_entry.status = status
                save_entry.company_name = company_name
                save_entry.recurrent = recurrent
                save_entry.employee_code= employee_code
                save_entry.save()

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                create_or_update_employee_shift_entry(
                    employee, employee_name
                )

        elif disbursement_type == DisbursementType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                create_or_update_employee_shift_entry(
                    employee, employee_name
                )

        elif disbursement_type == DisbursementType.JOB_TITLE:
            job_title = JobTitles.objects.get(id=instance.global_id)
            employees = Employee.objects.filter(
                company_id=company, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                create_or_update_employee_shift_entry(
                    employee, employee_name
                )

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                create_or_update_employee_shift_entry(
                    employee, employee_name
                )
