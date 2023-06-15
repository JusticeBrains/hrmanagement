from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.db.models import Sum
from employee.models import (
    KPI,
    AppraisalGrading,
    Department,
    EmployeeAppraisal,
    Employee,
    EmployeeDeduction,
    EmployeeKRA,
    EmployeeMedicalClaim,
    PayGroup,
    PropertyAssignment,
    PropertyRequest,
)
from django.core.exceptions import ValidationError
from company.models import Company
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime, timedelta

birth_date_remainder = Signal()


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


@receiver(post_save, sender=EmployeeAppraisal)
def update_employee_appraisal(sender, instance, **kwargs):
    employee = Employee.objects.get(id=instance.emp_id.id)
    instance.emp_name = employee.fullname
    instance.employee_code = employee.code
    instance.job_title = employee.job_titles
    instance.department = employee.second_category_level
    instance.company = employee.company

    # Temporarily disconnect the signal receiver
    post_save.disconnect(update_employee_appraisal, sender=EmployeeAppraisal)

    instance.save(
        update_fields=["emp_name", "employee_code", "job_title", "department"]
    )

    # Reconnect the signal receiver
    post_save.connect(update_employee_appraisal, sender=EmployeeAppraisal)


@receiver(post_save, sender=EmployeeAppraisal)
def update_grade(sender, instance, **kwargs):
    post_save.disconnect(update_grade, sender=EmployeeAppraisal)
    grading = AppraisalGrading.get_grading_for_score(instance.performance_score)
    if grading:
        instance.grade = grading.grade
        instance.recommendation = grading.recommendation
        # instance.percentage_score = f"{round((instance.performance_score / instance.total_kpi_scores) * 100, ndigits=2)}%"
    else:
        instance.grade = None
        instance.recommendation = None
        instance.percentage_score = None
    instance.save()

    post_save.connect(update_grade, sender=EmployeeAppraisal)


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


def populate_appraisal_employee_grading(instance, **kwargs):
    """
    Populate employee grading from appraisal grading
    """
    post_save.disconnect(populate_appraisal_employee_grading, sender=AppraisalGrading)
    if instance.company_id:
        instance.company = instance.company_id.name
    instance.save()
    post_save.connect(populate_appraisal_employee_grading, sender=AppraisalGrading)


@receiver(post_save, sender=KPI)
def update_kpi_fields(sender, instance, created, **kwargs):
    post_save.disconnect(update_kpi_fields, sender=KPI)
    employee = Employee.objects.get(id=instance.employee_id.id)
    if created:
        instance.company = employee.company
        instance.company_id = employee.company_id


        instance.score = round(
            (instance.supervisor_score / 100) * instance.kpi_score, ndigits=2
        )
    instance.save()
    post_save.connect(update_kpi_fields, sender=KPI)



@receiver(post_save, sender=KPI)
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
            total_score = KPI.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(total_score=Sum("score"))["total_score"]
            total_kpi_scores = KPI.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(total_kpi_scores=Sum("kpi_score"))["total_kpi_scores"]

            kra_total_scores = EmployeeKRA.objects.filter(
                employee_id=employee, period=active_period
            ).aggregate(kra_total_scores=Sum("total_score"))["kra_total_scores"]

            # Update the performance score and total kpi score of the EmployeeAppraisal object
            appraisal.performance_score = appraisal.performance_score or 0
            appraisal.performance_score += total_score
            appraisal.weighted_score = appraisal.weighted_score or 0
            appraisal.weighted_score += total_kpi_scores 
            
        
            # Save the updated EmployeeAppraisal object
            appraisal.save()
    except EmployeeAppraisal.DoesNotExist:
        return ValueError("Employee Appraisal Doesn't Exist")
    post_save.disconnect(update_performance_score, sender=KPI)

    instance.save()

    post_save.connect(update_performance_score, sender=KPI)


@receiver(post_save, sender=EmployeeKRA)
def update_kra_fields(sender, instance, created, **kwargs):
    post_save.disconnect(update_kra_fields, sender=EmployeeKRA)
    employee = Employee.objects.get(id=instance.employee_id.id)
    if created:
        instance.emp_code = employee.code
        instance.emp_name = employee.fullname
        instance.department = instance.department_id.name
        instance.company = instance.company_id.name
       
        instance.save(
            update_fields=[
                "emp_code",
                "emp_name",
                "department",
                "company",
            ]
        )

    post_save.connect(update_kra_fields, sender=EmployeeKRA)


@receiver(post_save, sender=EmployeeMedicalClaim)
def update_medical_claim(sender , instance, created, **kwargs):
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


@receiver(post_save, sender=PayGroup)
def update_employee_leave_days(sender, instance,created, **kwargs):
    post_save.disconnect(update_employee_leave_days, sender=PayGroup)

    if created:
        employees = Employee.objects.filter(pay_group_code=instance.no, company=instance.company)
        employees.update_or_create(total_number_of_leave_days=instance.total_number_of_leave_days)

        # for employee in employees:
        #     # employees.update(total_number_of_leave_days=instance.total_number_of_leave_days)
        #     employees.update_or_create(total_number_of_leave_days=instance.total_number_of_leave_days)
        #     # employee.total_number_of_leave_days = instance.total_number_of_leave_days
        #     employee.save()

        post_save.connect(update_employee_leave_days, sender=PayGroup)

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