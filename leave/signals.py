import re
import traceback
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from datetime import timedelta

from company.models import Company
from .models import EmployeeLeaveLimits, HolidayCalender, LeaveLimits
from employee.models import Employee
from leave.models import LeaveRequest, LeaveType, LeavePlan
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone

from environs import Env

env = Env()
env.read_env()

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

# Send email report


@receiver(post_save, sender=LeaveRequest)
def send_email(sender, instance, created, **kwargs):
    if created:
        employees = Employee.objects.all()
        employee_company = instance.employee.company_id
        for employee in employees:
            if (
                employee.company_id == employee_company
                and employee.is_hr == 0
                or employee.is_super == 0
            ):
                print(
                    f"{employee.company_id}, {employee_company}, {instance.employee.fullname}"
                )
                try:
                    print("---------------Sending -----------------------")
                    subject = "Leave Request Submitted"
                    message = f"Hello {instance.employee.fullname}, your request has been submitted"
                    from_email = env.str("EMAIL_USER")
                    recipient_list = [
                        instance.employee.company_email,
                        employee.company_email,
                        from_email,
                    ]
                    for email in recipient_list:
                        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                            raise ValueError(f"Invalid email address: {email}")
                    send_mail(subject, message, from_email, recipient_list)
                    print("---------------Sent -----------------------")
                except ValueError as ve:
                    print(f"Error occurred while sending email: {str(ve)}")

                except Exception as e:
                    print("Error occurred while sending email:")
                    print(str(e))
                    traceback.print_exc()

            # if (
            #     employee.company_id == employee_company
            #     and employee.is_hr == 1
            #     or employee.is_super == 1
            # ):
            #     print(
            #         f"{employee.company_id}, {employee_company}, {instance.employee.fullname}"
            #     )
            #     try:
            #         print("---------------Sending -----------------------")
            #         subject = "Leave Request Submitted"
            #         message = (
            #             f"{instance.employee.fullname} has submitted a leave request"
            #         )
            #         from_email = env.str("EMAIL_USER")
            #         recipient_list = [
            #             from_email,
            #             employee.company_email,
            #         ]
            #         for email in recipient_list:
            #             if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            #                 raise ValueError(f"Invalid email address: {email}")
            #         send_mail(subject, message, from_email, recipient_list)
            #         print("---------------Sent -----------------------")
            #     except ValueError as ve:
            #         print(f"Error occurred while sending email: {str(ve)}")

            #     except Exception as e:
            #         print("Error occurred while sending email:")
            #         print(str(e))
            #         traceback.print_exc()


@receiver(post_save, sender=LeaveRequest)
def send_going_on_leave_mail(sender, instance, created, **kwargs):
    if created:
        employees = Employee.objects.all()
        employee_company = instance.employee.company_id
        if timezone.now().date() + timedelta(days=1) == instance.start_date:
            for employee in employees:
                if (
                    employee.company_id == employee_company
                    and employee.is_hr == 1
                    or employee.is_super == 1
                    and instance.hr_status == 1
                ):
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Starting Tommorrow"
                        message = f"{instance.employee.fullname}, will be starting their leave Tommorrow"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            from_email,
                            employee.company_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()
                if instance.employee:
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Starting Tommorrow"
                        message = f"Hello {instance.employee.fullname},you will be starting your leave Tommorrow"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            instance.employee.company_email,
                            from_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()


@receiver(post_save, sender=LeaveRequest)
def hod_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.all()
    employee_company = instance.employee.company_id
    for employee in employees:
        if employee.company_id == employee_company:
            if employee.is_super == 1 or employee.is_hr == 1:
                if instance.hod_status == 1 and instance.hr_status == 0:
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Request Approved By Head Of Department"
                        message = f"{instance.employee.fullname}'s request has been approved by the HOD. <br>Thank You.<br>"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            from_email,
                            employee.company_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()
                if instance.employee:
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Request Approved By Head Of Department"
                        message = f"Hello {instance.employee.fullname}, your request has been approved by the HOD. <br>Thank You.<br>"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            instance.employee.company_email,
                            from_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()


@receiver(post_save, sender=LeaveRequest)
def hr_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.all()
    employee_company = instance.employee.company_id
    for employee in employees:
        if employee.company_id == employee_company:
            if employee.is_super == 1 or employee.is_hr == 1:
                if instance.hr_status == 1 and instance.hod_status == 1:
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Request Approved By HR"
                        message = f"{instance.employee.fullname}'s request has been approved by the HR. <br>Thank You.<br>"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            from_email,
                            employee.company_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()
                if instance.employee:
                    try:
                        print("---------------Sending -----------------------")
                        subject = "Leave Request Approved By HR"
                        message = f"Hello {instance.employee.fullname}, your request has been approved by your HR. <br>Thank You.<br>"
                        from_email = env.str("EMAIL_USER")
                        recipient_list = [
                            instance.employee.company_email,
                            from_email,
                        ]
                        for email in recipient_list:
                            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                                raise ValueError(f"Invalid email address: {email}")
                        send_mail(subject, message, from_email, recipient_list)
                        print("---------------Sent -----------------------")
                    except ValueError as ve:
                        print(f"Error occurred while sending email: {str(ve)}")

                    except Exception as e:
                        print("Error occurred while sending email:")
                        print(str(e))
                        traceback.print_exc()


@receiver(post_save, sender=LeaveRequest)
def update_employee_days_left(sender, instance, created, **kwargs):
    employee = instance.employee
    leave_type = instance.leave_type
    period = instance.period
    employee_limits = EmployeeLeaveLimits.objects.filter(
        employee=employee, leave_type=leave_type
    ).first()
    if instance.hr_status == 1:
        if instance.no_of_days_requested > employee_limits.number_of_days_left:
            raise ValidationError(
                f"Number of Requested{instance.no_of_days_requested} is greated than your leave days left for this leave type of {employee_limits.number_of_days_left}"
            )
        if instance.no_of_days_requested <= employee_limits.number_of_days_left:
            employee_limits.number_of_days_exhausted += instance.no_of_days_requested
            employee_limits.number_of_days_left -= (
                employee_limits.number_of_days_exhausted
            )
            employee_limits.save()

    if (
        instance.hr_extension_status == 1
        and instance.is_extend == 1
        and instance.hr_status == 1
        and instance.period == timezone.now().year
    ):
        if instance.no_of_extension_days > employee_limits.number_of_days_left:
            raise ValidationError(
                f"Number of Requested{instance.no_of_extension_days} is greated than your leave days left for this leave type of {employee_limits.number_of_days_left}"
            )
        if instance.no_of_extension_days <= employee_limits.number_of_days_left:
            employee_limits.number_of_days_exhausted += instance.no_of_extension_days
            employee_limits.number_of_days_left -= employee_limits.no_of_extension_days
            employee_limits.save()

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
        instance.leave_type_id = instance.leave_type.code
        instance.company_id = instance.paygroup.comp_id
        instance.paygroup_name = instance.paygroup.no
        print("------------------Starting--------------------------")
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
                        leave_type_id=instance.leave_type.code,
                        max_number_of_days=instance.max_number_of_days,
                        paygroup=instance.paygroup,
                        company=Company.objects.get(id=instance.paygroup.comp_id),
                    )
                elif EmployeeLeaveLimits.objects.filter(
                    leave_type=instance.leave_type,
                    employee=emp,
                    paygroup=instance.paygroup,
                ).exists():
                    EmployeeLeaveLimits.objects.update(
                        max_number_of_days=instance.max_number_of_days,
                        leave_type_id=instance.leave_type.code,
                    )
    instance.save()
    post_save.connect(create_employee_leave_limits, sender=LeaveLimits)
