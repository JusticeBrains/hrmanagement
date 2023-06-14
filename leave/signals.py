from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from datetime import timedelta

from company.models import Company
from .models import EmployeeLeaveLimits, HolidayCalender, LeaveLimits
from employee.models import Employee
from leave.models import LeaveRequest, LeaveType, LeavePlan
from django.core.exceptions import ValidationError


send_leave_reminder = Signal()

# @receiver(send_leave_reminder)
# def send_leave_reminder_handler(sender, instance, **kwargs):
#     leaves = LeaveRequest.objects.all()
#     for leave in leaves:
#         reminder_date = leave.end_date - timedelta(days=1)
#         if datetime.now().date() >= reminder_date:
#             subject = "Leave Ending Soon"
#             message = f"Dear {leave.employee}, you will be resuming work on {leave.end_date}"
#             send_mail(subject, message, 'hr@pay360.com', [leave.employee.company_email])

# # Receiver function to emit the signal after LeaveRequest is saved
# @receiver(post_save, sender=LeaveRequest)
# def emit_leave_reminder_signal(sender, instance, created, **kwargs):
#     if created:
#         send_leave_reminder.send(sender=LeaveRequest, instance=instance)



@receiver(post_save, sender=LeaveRequest)
def update_employee_days_left(sender, instance, created, **kwargs):
    employee_limits = EmployeeLeaveLimits.objects.all()
    employees = Employee.objects.all()
    if (
        instance.hr_status == 1
        and instance.hr_extension_status != 1
        and instance.is_extend != 1
        and instance.unpaid_leave == 0
    ):
        # for emp in employees:
    
        if instance.leave_type == employee_limits.leave_type and instance.employee == employee_limits.employee:
            if instance.no_of_days_requested > employee_limits.number_of_days_left:
                raise ValidationError(f"Number of Requested{instance.no_of_days_requested} is greated than your max_days for this leave type of {employee_limits. max_number_of_days}")
            if instance.no_of_days_requested <= employee_limits.number_of_days_left:
                employee_limits.number_of_days_exhausted += instance.no_of_days_requested
                employee_limits.number_of_days_left -= employee_limits.number_of_days_exhausted
                employee_limits.save()

            # update employee with new values of days_left and no_of_days_exhausted
            # Employee.objects.filter(id=instance.employee.id).update(
            #     days_left=instance.no_of_days_left,
            #     no_of_days_exhausted=no_of_days_exhausted,
            # )

    #     else:
    #         # instance.no_of_days_requested = instance.no_of_days_requested
    #         max_days = instance.leave_type.max_number_of_days
    #         employee = instance.employee
    #         emp_days_left = employee.days_left
    #         if emp_days_left is not None:
    #             if (
    #                 instance.no_of_days_requested <= emp_days_left
    #                 and instance.no_of_days_requested <= max_days
    #             ):
    #                 instance.no_of_days_left = (
    #                     emp_days_left - instance.no_of_days_requested
    #                 )

    #         no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
    #         no_of_days_exhausted += instance.no_of_days_requested

    #         # update employee with new values of days_left and no_of_days_exhausted
    #         Employee.objects.filter(id=instance.employee.id).update(
    #             days_left=instance.no_of_days_left,
    #             no_of_days_exhausted=no_of_days_exhausted,
    #         )

    # if (
    #     instance.hr_extension_status == 1
    #     and instance.is_extend == 1
    #     and instance.hr_status == 1
    # ):
    #     max_days = instance.leave_type.max_number_of_days

    #     employee = instance.employee
    #     emp_days_left = employee.days_left
    #     if emp_days_left is not None:
    #         if instance.no_of_extension_days <= emp_days_left:
    #             instance.no_of_days_left = emp_days_left - instance.no_of_extension_days

    #     no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
    #     no_of_days_exhausted += instance.no_of_extension_days

    #     # update employee with new values of days_left and no_of_days_exhausted
    #     Employee.objects.filter(id=instance.employee.id).update(
    #         days_left=instance.no_of_days_left,
    #         no_of_days_exhausted=no_of_days_exhausted,
    #     )

    # if instance.hr_status == 1 and instance.unpaid_leave == 1:
    #     no_of_days_exhausted = instance.employee.no_of_days_exhausted or 0
    #     no_of_days_exhausted += instance.no_of_days_requested

    #     Employee.objects.filter(id=instance.employee.id).update(
    #         days_left=instance.no_of_days_left,
    #         no_of_days_exhausted=no_of_days_exhausted,
    #     )

    post_save.disconnect(update_employee_days_left, sender=LeaveRequest)
    instance.save()
    post_save.connect(update_employee_days_left, sender=LeaveRequest)


@receiver(post_save, sender=LeavePlan)
def update_employee_days_left_leave_plan(sender, instance, created, **kwargs):
    if instance.hr_status == 1:
        if instance.leave_type.name == "Maternity":
            instance.no_of_days_requested = instance.leave_type.max_number_of_days
            instance.plan_days_left = instance.employee.plan_days_left

        else:
            # instance.no_of_days_requested = instance.no_of_days_requested
            max_days = instance.leave_type.max_number_of_days
            employee = instance.employee
            emp_days_left = employee.plan_days_left
            if emp_days_left is not None:
                if (
                    instance.no_of_days_requested <= emp_days_left
                    and instance.no_of_days_requested <= max_days
                ):
                    instance.plan_days_left = (
                        emp_days_left - instance.no_of_days_requested
                    )

        no_of_days_exhausted = instance.employee.plan_no_of_days_exhausted or 0
        no_of_days_exhausted += instance.no_of_days_requested

        # update employee with new values of days_left and no_of_days_exhausted
        Employee.objects.filter(id=instance.employee.id).update(
            days_left=instance.no_of_days_left,
            plan_no_of_days_exhausted=no_of_days_exhausted,
        )

    post_save.disconnect(update_employee_days_left_leave_plan, sender=LeavePlan)
    instance.save()
    post_save.connect(update_employee_days_left_leave_plan, sender=LeavePlan)


# @receiver(post_save, sender=LeaveType)
# def update_paygroup_code(sender, instance, created, **kwargs):
#     if created:
#         instance.pay_group_code = instance.paygroup.no
#         instance.save()


# @receiver(post_save, sender=LeavePlan)
# @receiver(post_save, sender=LeaveRequest)
# def compute_leave_resumption_date(sender, instance, created, **kwargs):
#     if created:
#         holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
#         instance.resumption_date = instance.end_date + timedelta(days=1)
#         while instance.resumption_date in holidays or instance.resumption_date.weekday() >= 5:
#             instance.resumption_date += timedelta(days=1)
#         instance.save()


# @receiver(post_save, sender=LeaveRequest)
# @receiver(post_save, sender=LeavePlan)
# def compute_leave_resumption_date(sender, instance, created, **kwargs):
#     if created:
#         holidays = HolidayCalender.objects.values_list("holiday_date", flat=True)
#         resumption_date = instance.end_date + timedelta(days=1)

#         while resumption_date.weekday() >= 5 or resumption_date.date() in holidays:
#             resumption_date += timedelta(days=1)

#         instance.resumption_date = resumption_date
#         instance.save()


@receiver(post_save, sender=LeaveLimits)
def create_employee_leave_limits(sender, instance, created, **kwargs):
    post_save.disconnect(create_employee_leave_limits, sender=LeaveLimits)
    employee = Employee.objects.all()
    if created:
        instance.leave_name = instance.leave_type.name
        instance.company_id = instance.paygroup.comp_id
        print("------------------Starting----------------1----------")
        for emp in employee:
            if (
                emp.pay_group_code == instance.paygroup.no
                and emp.company == instance.paygroup.company
            ):
                print(f"{emp.company_id}")
                if not EmployeeLeaveLimits.objects.filter(
                    leave_type=instance.leave_type,
                    employee=emp,
                    paygroup=instance.paygroup,
                ).exists():
                    EmployeeLeaveLimits.objects.create(
                        leave_type=instance.leave_type,
                        employee=emp,
                        max_number_of_days=instance.max_number_of_days,
                        paygroup=instance.paygroup,
                        company=Company.objects.get(id=instance.paygroup.comp_id),
                    )
                else:
                    print("Already Exists")

    post_save.connect(create_employee_leave_limits, sender=LeaveLimits)
