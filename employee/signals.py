from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from calenders.models import Period
from employee.models import EmployeeAppraisal, Employee, EmployeeAppraisalDetail


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
    emp_code = instance.emp_code
    active_period = Period.objects.get(active=True)


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
