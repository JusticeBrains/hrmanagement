from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from employee.models import EmployeeAppraisal, Employee

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
