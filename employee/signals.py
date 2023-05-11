from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from employee.models import EmployeeAppraisal, Employee

# @receiver(pre_save, sender=EmployeeAppraisal)
# def update_employee_appraisal(sender, instance , created , **kwargs):
#     employee = Employee.objects.get(id=instance.emp_code.id)
#     instance.emp_name = employee.fullname
#     instance.job_titles = employee.job_titles
#     instance.department = employee.second_category_level

# pre_save.connect(update_employee_appraisal, sender=EmployeeAppraisal)