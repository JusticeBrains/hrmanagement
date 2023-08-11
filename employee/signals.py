from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from django.db.models import Sum
from employee.models import (
    KPI,
    AppraisalGrading,
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
from django.core.exceptions import ValidationError
from company.models import Company
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime, timedelta
# from celery.task import periodic_task
from django.core.management import call_command


from employee.management.commands import update_scheduler


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


@receiver(pre_save, sender=EmployeeAppraisal)
def update_employee_appraisal(sender, instance, **kwargs):
    employee = Employee.objects.get(id=instance.emp_id.id)
    if instance:
        instance.emp_name = employee.fullname
        instance.employee_code = employee.code
        instance.job_title = employee.job_titles
        instance.department = employee.department.name
        instance.department_id = employee.department
        instance.company = employee.company_id.name
        instance.company_id = employee.company_id


@receiver(pre_save, sender=EmployeeAppraisal)
def update_grade(sender, instance, **kwargs):
    grading = AppraisalGrading.get_grading_for_score(instance.performance_score)
    if instance:
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


@receiver(pre_save, sender=EmployeeBehavioural)
def update_emp_total_score_scores(sender, instance, **kwargs):
    if instance:
        if instance.final_score is not None and instance.score_on_target is not None:
            instance.computed_score = round(
                (instance.final_score / 100) * instance.score_on_target, ndigits=2
            )

@receiver(post_save, sender=Branch)
def updated_fields_branch(sender, instance,created, **kwargs):
    post_save.disconnect(updated_fields_branch, sender=Branch)
    if created:
        instance.unit_name = instance.unit.name
        instance.save()
    post_save.connect(updated_fields_branch, sender=Branch)


@receiver(post_save, sender=Unit)
def updated_fields_unit(sender, instance,created, **kwargs):
    post_save.disconnect(updated_fields_unit, sender=Unit)

    if created:
        instance.department_name = instance.department.name
        instance.save()
    post_save.connect(updated_fields_unit, sender=Unit)
