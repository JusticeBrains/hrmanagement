from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee
from leave.models import LeaveRequest, LeaveType

@receiver(post_save, sender=LeaveRequest)
def update_employee_days_left(sender, instance, created, **kwargs):
    if instance.hr_status == 1 and instance.hr_extension_status != 1 and instance.is_extend != 1:
            if instance.leave_type.name == "Maternity":
                instance.no_of_days_requested = instance.leave_type.max_number_of_days
                instance.no_of_days_left = instance.employee.days_left

            else:
                # instance.no_of_days_requested = instance.no_of_days_requested
                max_days = instance.leave_type.max_number_of_days
                employee = instance.employee
                emp_days_left = employee.days_left
                if emp_days_left is not None:
                    if instance.no_of_days_requested <= emp_days_left and instance.no_of_days_requested > max_days:
                        instance.no_of_days_left = emp_days_left - instance.no_of_days_requested


            no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
            no_of_days_exhausted += instance.no_of_days_requested

            # update employee with new values of days_left and no_of_days_exhausted
            Employee.objects.filter(id=instance.employee.id).update(
                days_left=instance.no_of_days_left, no_of_days_exhausted=no_of_days_exhausted
            )
        
    if instance.hr_extension_status == 1 and instance.is_extend == 1 and instance.hr_status == 1:
        max_days = instance.leave_type.max_number_of_days

        employee = instance.employee
        emp_days_left = employee.days_left
        if emp_days_left is not None:
            if instance.no_of_extension_days <= emp_days_left and instance.no_of_days_requested > max_days:
                instance.no_of_days_left = emp_days_left - instance.no_of_extension_days


        no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
        no_of_days_exhausted += instance.no_of_extension_days

        # update employee with new values of days_left and no_of_days_exhausted
        Employee.objects.filter(id=instance.employee.id).update(
            days_left=instance.no_of_days_left, no_of_days_exhausted=no_of_days_exhausted
        )


@receiver(post_save, sender=LeaveType)
def update_paygroup_code(sender, instance, created, **kwargs):
    if created:
        instance.pay_group_code = instance.paygroup.no
        instance.save()