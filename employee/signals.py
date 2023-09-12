from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from django.db.models import Sum
from employee.models import (
    KPI,
    AppraisalGrading,
    AppraisalSetup,
    BehaviouralCompetencies,
    Branch,
    Department,
    EmployeeAppraisal,
    Employee,
    EmployeeBehavioural,
    EmployeeDeduction,
    EmployeeKRA,
    EmployeeMedicalClaim,
    PayGroup,
    PropertyAssignment,
    PropertyRequest,
    Unit,
)
from django.db import transaction
from django.core.exceptions import ValidationError
from company.models import Company, JobTitles
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime, timedelta
# from celery.task import periodic_task
from django.core.management import call_command


from employee.management.commands import update_scheduler
from options.text_options import AppraisalSetUpType


birth_date_remainder = Signal()


# @periodic_task(run_every=timedelta(minutes=1))
# def update_employees_signal(sender, **kwargs):
#     call_command('update_scheduler')



@receiver(birth_date_remainder)
def send_birthday_reminder(sender, instance, **kwargs):
    employee = Employee.objects.all()
    three_days_before_birthday = employee.birth_date.replace(
        year=datetime.now().year
    ) - timedelta(days=3)

    if (
        three_days_before_birthday.month == datetime.now().month
        and three_days_before_birthday.day == datetime.now().day
    ):
        subject = "Birthday Reminder"
        message = f"Dear {employee.name}, your birthday is coming up in 3 days!"
        send_mail(subject, message, "hr@pay360.com", [employee.company_email])


@receiver(post_save, sender=AppraisalSetup)
def create_appraisal(sender, instance,**kwargs):
    post_save.disconnect(create_appraisal, sender=AppraisalSetup)
    if instance:
        appraisal_type = instance.appraisal_type
        appraisal_date = instance.appraisal_date
        appraisal_id = instance.appraisal_id
        period = instance.period
        company_id = instance.company_id
        company = instance.company
        status = instance.status


        @transaction.atomic
        def create_or_update_employee_employee_appraisal(
            employee, employee_name
        ):
            """
            Create or update EmployeeSavingSchemeEntries object for the given employee.
            """
            save_entry, created = EmployeeAppraisal.objects.get_or_create(
                appraisal_setup=instance,
                emp_id=employee,
                emp_name = employee_name,
                defaults={
                    "company":company,
                    "emp_name":employee_name,
                    "employee_code": employee_code,
                    "status":status,
                    "company": company,
                    "company_id": company_id,
                    "appraisal_date": appraisal_date,
                },
            )

            if not created:
                save_entry.status = status
                save_entry.employee_code = employee_code
                save_entry.company = company
                save_entry.company_id = company_id
                save_entry.period = period
                save_entry.appraisal_date = appraisal_date
                save_entry.save()

        if appraisal_type == AppraisalSetUpType.ALL_STAFF:
            employees = Employee.objects.filter(company_id=company_id)

            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                instance.appraisal_name = employee.company
                create_or_update_employee_employee_appraisal(
                    employee, employee_name
                )

        elif appraisal_type == AppraisalSetUpType.PAY_GROUP:
            pay_group = PayGroup.objects.get(id=instance.appraisal_id)
            instance.appraisal_name = pay_group.no

            employees = Employee.objects.filter(
                company_id=company_id, pay_group_code=pay_group
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                create_or_update_employee_employee_appraisal(
                    employee, employee_name
                )

        elif appraisal_type == AppraisalSetUpType.JOB_TITLE:
            job_title = JobTitles.objects.get(id=instance.appraisal_id)
            instance.appraisal_name = job_title.description
            employees = Employee.objects.filter(
                company_id=company_id, job_titles=job_title
            )
            for employee in employees:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                instance.appraisal_name = employee.job_title_description
                create_or_update_employee_employee_appraisal(
                    employee, employee_name
                )

        elif appraisal_type == AppraisalSetUpType.INDIVIDUAL:
            employee = Employee.objects.get(id=instance.appraisal_id)
            if employee:
                employee_name = f"{employee.last_name} {employee.first_name}"
                employee_code = employee.code
                instance.appraisal_name = employee_name
                create_or_update_employee_employee_appraisal(
                    employee, employee_name
                )
        instance.save()
    post_save.disconnect(create_appraisal, sender=AppraisalSetup)




@receiver(pre_save, sender=EmployeeAppraisal)
def update_employee_appraisal(sender, instance, **kwargs):
    employee = Employee.objects.get(id=instance.emp_id.id)
    grading = AppraisalGrading.get_grading_for_score(instance.performance_score)
    if instance:
        instance.emp_name = employee.fullname
        instance.employee_code = employee.code
        instance.job_title = employee.job_titles
        instance.department = employee.department.name
        instance.department_id = employee.department
        instance.company = employee.company_id.name
        instance.company_id = employee.company_id

        if grading:
            instance.grade = grading.grade
            instance.recommendation = grading.recommendation
            # instance.percentage_score = f"{round((instance.performance_score / instance.total_kpi_scores) * 100, ndigits=2)}%"
        else:
            instance.grade = None
            instance.recommendation = None
            instance.percentage_score = None



@receiver(post_save, sender=Department)
def populate_company_field_department(sender, instance, **kwargs):
    """
    Populate company field with company name from the job application
    """
    post_save.disconnect(populate_company_field_department, sender=Department)
    if instance.company_id:
        comp = Company.objects.get(id=instance.company_id)
        instance.company = comp.name
        instance.save()
    post_save.connect(populate_company_field_department, sender=Department)


@receiver(post_save, sender=EmployeeDeduction)
def leave_days_deduction(sender, instance, **kwargs):
    """
    Deduct leave days from employee
    """
    post_save.disconnect(leave_days_deduction, sender=EmployeeDeduction)
    if instance.no_of_days:
        employee = instance.employee
        emp_days_left = employee.days_left
        if emp_days_left is not None:
            if emp_days_left >= instance.no_of_days:
                emp_days_left = emp_days_left - instance.no_of_days
                instance.employee_name = instance.employee.fullname
            no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
            no_of_days_exhausted += instance.no_of_days

            Employee.objects.filter(id=employee.id).update(
                days_left=emp_days_left, no_of_days_exhausted=no_of_days_exhausted
            )
    instance.save()

    post_save.connect(leave_days_deduction, sender=EmployeeDeduction)


@receiver(pre_save, sender=EmployeeKRA)
def update_emp_total_score_scores(sender, instance, **kwargs):
    if instance:
        if (
            instance.supervisor_total_score is not None
            and instance.total_score is not None
        ):
            instance.computed_supervisor_score = round(
                (instance.supervisor_total_score / 100) * instance.total_score,
                ndigits=2,
            )
        if instance.emp_total_score is not None and instance.total_score is not None:
            instance.computed_employee_score = round(
                (instance.emp_total_score / 100) * instance.total_score, ndigits=2
            )


@receiver(pre_save, sender=EmployeeBehavioural)
def update_emp_total_score_scores(sender, instance, **kwargs):
    if instance:
        if instance.final_score is not None and instance.score_on_target is not None:
            instance.computed_score = round(
                (instance.final_score / 100) * instance.score_on_target, ndigits=2
            )


@receiver(post_save, sender=EmployeeBehavioural)
@receiver(post_save, sender=EmployeeKRA)
def update_performance_score(instance, **kwargs):
    employee = Employee.objects.get(id=instance.employee_id.id)

    active_period = timezone.now().year

    try:
        # Retrieve the corresponding EmployeeAppraisal object
        appraisal = EmployeeAppraisal.objects.filter(
            emp_id=employee, period=active_period
        ).first()
        if appraisal:
            # Retrieve the total score from records
            total_supervisor_total_score = EmployeeKRA.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(total_supervisor_total_score=Sum("computed_supervisor_score"))[
                "total_supervisor_total_score"
            ]

            kra_total_scores = EmployeeKRA.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(kra_total_scores=Sum("total_score"))["kra_total_scores"]

            score_on_target = EmployeeBehavioural.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(score_on_target=Sum("score_on_target"))["score_on_target"]
            # Update the performance score and total kra score of the EmployeeAppraisal object
            appraisal.appraisal_score = (
                total_supervisor_total_score
                if total_supervisor_total_score is not None
                else None
            )
            total_behavioural_score = EmployeeBehavioural.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(total_behavioural_score=Sum("computed_score"))[
                "total_behavioural_score"
            ]
            appraisal.behavioural_score = (
                total_behavioural_score if total_behavioural_score is not None else None
            )
            appraisal.weighted_score = (
                kra_total_scores if kra_total_scores is not None else None
            )
            appraisal.performance_score = (
                total_supervisor_total_score + total_behavioural_score
                if total_supervisor_total_score and total_behavioural_score is not None
                else None
            )
            appraisal.weighted_behavioural_score = (
                score_on_target if score_on_target is not None else None
            )
            # Save the updated EmployeeAppraisal object
            appraisal.save()
    except EmployeeAppraisal.DoesNotExist:
        return ValueError("Employee Appraisal Doesn't Exist")


@receiver(pre_save, sender=EmployeeKRA)
def update_kra_fields(sender, instance, **kwargs):
    employee = Employee.objects.get(id=instance.employee_id.id)
    if instance:
        instance.emp_code = employee.code
        instance.emp_name = employee.fullname
        instance.department = employee.department.name
        instance.department_id = employee.department
        instance.company = employee.company_id.name
        instance.company_id = employee.company_id


@receiver(post_save, sender=EmployeeMedicalClaim)
def update_medical_claim(sender, instance, created, **kwargs):
    post_save.disconnect(update_medical_claim, sender=EmployeeMedicalClaim)
    if created:
        employee = Employee.objects.get(id=instance.employee_id.id)
        instance.emp_name = employee.fullname
        instance.department = instance.department_id.name
        instance.company = instance.company_id.name

        claim_amount = instance.claim_amount
        medical_claim_amount_left = employee.medical_claim_amount_left
        if medical_claim_amount_left is not None:
            if claim_amount <= medical_claim_amount_left:
                medical_claim_left = medical_claim_amount_left - claim_amount
                used_medical_claim_amount = employee.used_medical_claim_amount or 0
                used_medical_claim_amount += claim_amount
                Employee.objects.filter(id=employee.id).update(
                    medical_claim_amount_left=medical_claim_left,
                    used_medical_claim_amount=used_medical_claim_amount,
                )
        instance.save()
    post_save.connect(update_medical_claim, sender=EmployeeMedicalClaim)


@receiver(post_save, sender=PropertyAssignment)
def update_property_assignment(sender, instance, created, **kwargs):
    post_save.disconnect(update_property_assignment, sender=PropertyAssignment)

    if created:
        instance.employee_name = instance.employee_id.fullname
        instance.department_name = instance.department_id.name
        instance.company_name = instance.company_id.name

    instance.save()
    post_save.connect(update_property_assignment, sender=PropertyAssignment)


@receiver(post_save, sender=PropertyRequest)
def update_property_request(sender, instance, created, **kwargs):
    post_save.disconnect(update_property_request, sender=PropertyRequest)

    if created:
        instance.department_name = instance.department_id.name
        instance.company_name = instance.company_id.name

    instance.save()
    post_save.connect(update_property_request, sender=PropertyRequest)


@receiver(pre_save, sender=EmployeeAppraisal)
def create_employee_behaviourial(sender, instance, **kwargs):
    if instance:
        behaviourials = BehaviouralCompetencies.objects.filter(
            company_id=instance.company_id, period=instance.period
        )

        for behaviorial in behaviourials:
            EmployeeBehavioural.objects.get_or_create(
                employee_id=instance.emp_id,
                employee_name=instance.emp_id.fullname,
                score_on_target=behaviorial.target_score,
                competency=behaviorial.competency,
                period=behaviorial.period,
            )


@receiver(post_save, sender=Unit)
def updated_fields_unit(sender, instance,created, **kwargs):
    post_save.disconnect(updated_fields_unit, sender=Unit)

    if created:
        instance.department_name = instance.department.name
        instance.save()
    post_save.connect(updated_fields_unit, sender=Unit)
