from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from employee.models import AppraisalGrading, EmployeeAppraisal, Employee, EmployeeAppraisalDetail
from django.utils import timezone

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
            if total_score is not None:
                appraisal.performance_score = total_score
            else:
                appraisal.performance_score = None

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
    else:
        instance.grade = None
        instance.recommendation = None
    instance.percentage_score = f"{round((instance.performance_score / 100) * 100, ndigits=2)} %"
    instance.save()

    post_save.connect(update_grade, sender=EmployeeAppraisal)