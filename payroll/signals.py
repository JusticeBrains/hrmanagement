from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from employee.models import Employee, PayGroup
from company.models import JobTitles
from .models import EmployeeSavingSchemeEntries, SavingSchemeEntries
from options.text_options import DisbursementType

@receiver(post_save, sender=SavingSchemeEntries)
def create_employee_saving_scheme(sender, instance, **kwargs):
    if instance:
        disbursement_type = instance.disbursement_type
        saving_scheme_name = instance.saving_scheme_name
        recurrent = instance.recurrent
        start_period_code = instance.start_period_code
        end_period_code = instance.end_period_code
        user_id = instance.user_id
        company_name = instance.company_name
        company = instance.company

        if disbursement_type == DisbursementType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company)
            for employee in employees:
                save_entry, created = EmployeeSavingSchemeEntries.objects.get_or_create(
                    saving_scheme = instance,
                    saving_scheme_name=saving_scheme_name,
                    recurrent=recurrent,
                    start_period_code=start_period_code,
                    end_period_code=end_period_code,
                    user_id=user_id,
                    company_name=company_name,
                    employee= employee,
                    employee_name= f"{employee.last_name} {employee.first_name}"
                )

                if not created:
                    save_entry.saving_scheme = instance
                    save_entry.saving_scheme_name = saving_scheme_name
                    save_entry.recurrent = recurrent
                    save_entry.start_period_code = start_period_code
                    save_entry.end_period_code = end_period_code
                    save_entry.user_id=user_id
                    save_entry.company_name=company_name
                    save_entry.employee = employee
                    save_entry.employee_name = f"{employee.last_name} {employee.first_name}"
                    save_entry.save()

        elif disbursement_type == DisbursementType.PAY_GROUP:
            employees = Employee.objects.filter(company_id=company, pay_group_code=PayGroup.objects.get(id=instance.global_id))
            for employee in employees:
                save_entry, created = EmployeeSavingSchemeEntries.objects.get_or_create(
                    saving_scheme = instance,
                    saving_scheme_name=saving_scheme_name,
                    recurrent=recurrent,
                    start_period_code=start_period_code,
                    end_period_code=end_period_code,
                    user_id=user_id,
                    company_name=company_name,
                    employee= employee,
                    employee_name= f"{employee.last_name} {employee.first_name}"
                )

                if not created:
                    save_entry.saving_scheme = instance
                    save_entry.saving_scheme_name = saving_scheme_name
                    save_entry.recurrent = recurrent
                    save_entry.start_period_code = start_period_code
                    save_entry.end_period_code = end_period_code
                    save_entry.user_id=user_id
                    save_entry.company_name=company_name
                    save_entry.employee = employee
                    save_entry.employee_name = f"{employee.last_name} {employee.first_name}"
                    save_entry.save()

        elif disbursement_type == DisbursementType.JOB_TITLE:
            employees = Employee.objects.filter(company_id=company, job_titles=JobTitles.objects.get(id=instance.global_id))
            for employee in employees:
                save_entry, created = EmployeeSavingSchemeEntries.objects.get_or_create(
                    saving_scheme = instance,
                    saving_scheme_name=saving_scheme_name,
                    recurrent=recurrent,
                    start_period_code=start_period_code,
                    end_period_code=end_period_code,
                    user_id=user_id,
                    company_name=company_name,
                    employee= employee,
                    employee_name= f"{employee.last_name} {employee.first_name}"
                )

                if not created:
                    save_entry.saving_scheme = instance
                    save_entry.saving_scheme_name = saving_scheme_name
                    save_entry.recurrent = recurrent
                    save_entry.start_period_code = start_period_code
                    save_entry.end_period_code = end_period_code
                    save_entry.user_id=user_id
                    save_entry.company_name=company_name
                    save_entry.employee = employee
                    save_entry.employee_name = f"{employee.last_name} {employee.first_name}"
                    save_entry.save()

        elif disbursement_type == DisbursementType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.global_id)
            if employee:
                save_entry, created = EmployeeSavingSchemeEntries.objects.get_or_create(
                    saving_scheme = instance,
                    saving_scheme_name=saving_scheme_name,
                    recurrent=recurrent,
                    start_period_code=start_period_code,
                    end_period_code=end_period_code,
                    user_id=user_id,
                    company_name=company_name,
                    employee= employee,
                    employee_name= f"{employee.last_name} {employee.first_name}"
                )

                if not created:
                    save_entry.saving_scheme = instance
                    save_entry.saving_scheme_name = saving_scheme_name
                    save_entry.recurrent = recurrent
                    save_entry.start_period_code = start_period_code
                    save_entry.end_period_code = end_period_code
                    save_entry.user_id=user_id
                    save_entry.company_name=company_name
                    save_entry.employee = employee
                    save_entry.employee_name = f"{employee.last_name} {employee.first_name}"
                    save_entry.save()