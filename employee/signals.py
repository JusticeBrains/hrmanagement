from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from django.db.models import Sum
from employee.models import AppraisalGrading, Department, EmployeeAppraisal, Employee, EmployeeAppraisalDetail, EmployeeDeduction
from company.models import Company
from django.utils import timezone
from django.core.mail import send_mail
from datetime import datetime, timedelta

birth_date_remainder = Signal()

@receiver(birth_date_remainder)
def send_birthday_reminder(sender, instance, **kwargs):
    employee = Employee.objects.all()
    three_days_before_birthday = employee.birth_date.replace(year=datetime.now().year) - timedelta(days=3)

    if three_days_before_birthday.month == datetime.now().month and \
            three_days_before_birthday.day == datetime.now().day:
        subject = "Birthday Reminder"
        message = f"Dear {employee.name}, your birthday is coming up in 3 days!"
        send_mail(subject, message, 'hr@pay360.com', [employee.company_email])


@receiver(post_save, sender=EmployeeAppraisal)
def update_employee_appraisal(sender, instance , **kwargs):
        employee= Employee.objects.get(id=instance.emp_id.id)
        instance.emp_name = employee.fullname
        instance.employee_code = employee.code
        instance.job_title = employee.job_titles
        instance.department = employee.second_category_level


        # Temporarily disconnect the signal receiver
        post_save.disconnect(update_employee_appraisal, sender=EmployeeAppraisal)

        instance.save(update_fields=['emp_name', 'employee_code', 'job_title', 'department'])

        # Reconnect the signal receiver
        post_save.connect(update_employee_appraisal, sender=EmployeeAppraisal)


@receiver(post_save, sender=EmployeeAppraisalDetail)
def update_performance_score(sender, instance, **kwargs):
    employee= Employee.objects.get(id=instance.employee_id.id)
    instance.emp_name = employee.fullname
    instance.emp_code = employee.code
    emp_code = instance.emp_code

    active_period = timezone.now().year


    try:
        # Retrieve the corresponding EmployeeAppraisal object
        appraisal = EmployeeAppraisal.objects.filter(employee_code=emp_code, period=active_period).first()
        if appraisal:
            # Retrieve the total score from EmployeeAppraisalDetail records
            total_score = EmployeeAppraisalDetail.objects.filter(emp_code=emp_code, period=active_period).aggregate(total_score=Sum('score'))['total_score']
            
            # Update the performance score of the EmployeeAppraisal object
            appraisal.performance_score = total_score if total_score is not None else None

            # Save the updated EmployeeAppraisal object
            appraisal.save()
    except EmployeeAppraisal.DoesNotExist:
         return ValueError("Employee Appraisal Doesn't Exist")
    post_save.disconnect(update_performance_score, sender=EmployeeAppraisalDetail)
    
    instance.save(update_fields=['emp_name', 'emp_code',])

    post_save.connect(update_performance_score, sender=EmployeeAppraisalDetail)


@receiver(post_save, sender=EmployeeAppraisal)
def update_grade(sender, instance, **kwargs):
    post_save.disconnect(update_grade, sender=EmployeeAppraisal )
    grading = AppraisalGrading.get_grading_for_score(instance.performance_score)
    if grading:
        instance.grade = grading.grade
        instance.recommendation = grading.recommendation
        instance.percentage_score = f"{round((instance.performance_score / 100) * 100, ndigits=2)}%"
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
        if emp_days_left is not None or 0:
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


# @receiver(post_save, sender=PayGroup)
# def update_employee_leave_days(sender, instance,created, **kwargs):
#     post_save.disconnect(update_employee_leave_days, sender=PayGroup)
     
#     if created:
#         employees = Employee.objects.filter(pay_group_code=instance.no, company=instance.company)
#         employees.update_or_create(total_number_of_leave_days=instance.total_number_of_leave_days)

#         # for employee in employees:
#         #     # employees.update(total_number_of_leave_days=instance.total_number_of_leave_days)
#         #     employees.update_or_create(total_number_of_leave_days=instance.total_number_of_leave_days)
#         #     # employee.total_number_of_leave_days = instance.total_number_of_leave_days
#         #     employee.save()

#         post_save.connect(update_employee_leave_days, sender=PayGroup)
