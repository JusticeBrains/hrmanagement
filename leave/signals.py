import re
import traceback
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver, Signal
from datetime import timedelta

from company.models import Company
from .models import EmployeeLeaveLimits, LeaveLimits
from employee.models import Employee
from leave.models import LeaveRequest, LeavePlan
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils import timezone
from django.core.validators import validate_email
from django.db.models import Q

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
        employees = Employee.objects.filter(
            Q(company_id=instance.employee.company_id, is_hr=1)
            | Q(company_id=instance.employee.company_id, is_super=1)
            | Q(id=instance.employee.id)
        )

        for employee in employees:
            try:
                print("---------------Sending -----------------------")
                subject = "Leave Request Submitted"
                

                if employee.id == instance.employee.id:
                    print(employee.id == instance.employee.id)
                    message = (
                        f"Hello {employee.fullname}, your request has been submitted"
                    )
                    recipient_list = [employee.company_email]
                    
                    print("---------------Sent -----------------------")

                if employee.is_hr == 1 or employee.is_super == 1:
                    message = (
                        f"{instance.employee.fullname} has submitted a leave request"
                    )
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
                for email in recipient_list:
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                        raise ValueError(
                            f"Invalid email address: {email}"
                        )  # Validates email address

                send_mail(subject, message, from_email, recipient_list)

                print("---------------Sent -----------------------")

            except ValueError as ve:
                print(f"Error occurred while sending email: {str(ve)}")
            except Exception as e:
                print("Error occurred while sending email:")
                print(str(e))
                traceback.print_exc()


@receiver(post_save, sender=LeavePlan)
def send_email(sender, instance, created, **kwargs):
    if created:
        employees = Employee.objects.filter(
            Q(company_id=instance.employee.company_id, is_hr=1)
            | Q(company_id=instance.employee.company_id, is_super=1)
            | Q(id=instance.employee.id)
        )

        for employee in employees:
            try:
                subject = "Leave Plan Submitted"

                if employee.id == instance.employee.id:
                    print(f"{instance.employee.id}")
                    print(f"employee.id: {employee.id}")
                    print(f"instance.employee.id: {instance.employee.id}")

                    print("---------------Sending -----------------------")
                    print(
                        f"{instance.employee.company_id}, {instance.employee.company_id}, {instance.employee.fullname}"
                    )
                    message = f"Hello {instance.employee.fullname}, your leave plan has been submitted"
                    recipient_list = [
                        instance.employee.company_email,
                    ]

                if employee.is_hr == 1 or employee.is_super == 1:
                    message = f"{instance.employee.fullname} has submitted a leave plan"
                    
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
                for email in recipient_list:
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                        raise ValueError(
                            f"Invalid email address: {email}"
                        )  # Validates email address
                send_mail(subject, message, from_email, recipient_list)
                print("---------------Sent -----------------------")
            except ValueError as ve:
                print(f"Error occurred while sending email: {str(ve)}")
            except Exception as e:
                print("Error occurred while sending email:")
                print(str(e))
                traceback.print_exc()


@receiver(post_save, sender=LeaveRequest)
def send_going_on_leave_mail(sender, instance, created, **kwargs):
    if created:
        employees = Employee.objects.filter(
            Q(company_id=instance.employee.company_id, is_hr=1)
            | Q(company_id=instance.employee.company_id, is_super=1)
            | Q(id=instance.employee.id)
        )
        if timezone.now().date() + timedelta(days=1) == instance.start_date:
            for employee in employees:
                try:
                    subject = "Leave Starting Tommorrow"
                    if employee.id == instance.employee.id:
                        print("---------------Sending -----------------------")

                        message = f"Hello you will be starting your leave Tommorrow"
                        recipient_list = [
                            employee.company_email,
                        ]

                    if employee.is_hr == 1 or employee.is_super == 1:
                        message = f"{instance.employee.fullname}, will be starting their leave Tommorrow"
                       
                        recipient_list = [
                            employee.company_email,
                        ]

                    from_email = env.str("EMAIL_USER")
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


@receiver(pre_save, sender=LeaveRequest)
def hod_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.filter(
        Q(company_id=instance.employee.company_id, is_hr=1)
        | Q(company_id=instance.employee.company_id, is_super=1)
        | Q(id=instance.employee.id)
    )
    for employee in employees:
        if instance.hod_status == 1 and instance.hr_status == 0:
            try:
                subject = "Leave Request Approved By Head Of Department"

                if employee.id == instance.employee.id:
                    print("---------------Sending -----------------------")
                    message = f"Hello your request has been approved by the HOD. <br>Thank You.<br>"
                    recipient_list = [
                        instance.employee.company_email,
                    ]

                if employee.is_hr == 1 or employee.is_super == 1:
                    message = f"{instance.employee.fullname}'s request has been approved by the HOD. <br>Thank You.<br>"
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
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


@receiver(pre_save, sender=LeavePlan)
def hod_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.filter(
        Q(company_id=instance.employee.company_id, is_hr=1)
        | Q(company_id=instance.employee.company_id, is_super=1)
        | Q(id=instance.employee.id)
    )
    for employee in employees:
        if instance.hod_status == 1 and instance.hr_status == 0:
            try:
                subject = "Leave Plan Approved By Head Of Department"

                if employee.id == instance.employee.id:
                    print(f"{instance.employee.id}")
                    print("---------------Sending -----------------------")
                    message = f"Hello {instance.employee.fullname}, your leave plan has been approved by the HOD. <br>Thank You.<br>"
                    recipient_list = [
                        instance.employee.company_email,
                    ]

                if employee.is_hr == 1 or employee.is_super == 1:
                    message = f"{instance.employee.fullname}'s leave plan has been approved by the HOD. <br>Thank You.<br>"
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
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


@receiver(pre_save, sender=LeaveRequest)
def hr_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.filter(
        Q(company_id=instance.employee.company_id, is_hr=1)
        | Q(company_id=instance.employee.company_id, is_super=1)
        | Q(id=instance.employee.id)
    )
    for employee in employees:
        if instance.hod_status == 1 and instance.hr_status == 1:
            try:
                subject = "Leave Request Approved By HR"

                if employee.id == instance.employee.id:
                    print(f"{instance.employee.id}")
                    print("---------------Sending -----------------------")
                    message = f"Hello your request has been approved by the HR. <br>Thank You.<br>"
                    recipient_list = [
                        instance.employee.company_email,
                    ]

                if employee.is_hr == 1 or employee.is_super == 1:
                    message = f"{instance.employee.fullname}'s request has been approved by the HR. <br>Thank You.<br>"
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
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


@receiver(post_save, sender=LeavePlan)
def hr_approved_status(sender, instance, **kwargs):
    employees = Employee.objects.filter(
        Q(company_id=instance.employee.company_id, is_hr=1)
        | Q(company_id=instance.employee.company_id, is_super=1)
        | Q(id=instance.employee.id)
    )
    for employee in employees:
        if instance.hod_status == 1 and instance.hr_status == 1:
            try:
                subject = "Leave Plan Approved By HR"

                if employee.id == instance.employee.id:
                    print("---------------Sending -----------------------")
                    message = f"Hello your leave plan has been approved by the HR. <br>Thank You.<br>"
                    recipient_list = [
                        instance.employee.company_email,
                    ]
                    
                if employee.is_hr == 1 or employee.is_super == 1:
                    message = f"{instance.employee.fullname}'s leave plan has been approved by the HR. <br>Thank You.<br>"
                    recipient_list = [
                        employee.company_email,
                    ]

                from_email = env.str("EMAIL_USER")
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


@receiver(pre_save, sender=LeaveRequest)
def update_employee_days_left(sender, instance, **kwargs):
    employee = instance.employee
    leave_type = instance.leave_type
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


@receiver(pre_save, sender=LeavePlan)
def update_employee_plan_days_left(sender, instance, **kwargs):
    employee = instance.employee
    leave_type = instance.leave_type
    employee_limits = EmployeeLeaveLimits.objects.filter(
        employee=employee, leave_type=leave_type
    ).first()
    if instance.hr_status == 1:
        if instance.no_of_days_requested > employee_limits.number_of_plan_days_left:
            raise ValidationError(
                f"Number of Requested{instance.no_of_days_requested} is greated than your leave days left for this leave type of {employee_limits.number_of_days_left}"
            )
        if instance.no_of_days_requested <= employee_limits.number_of_plan_days_left:
            employee_limits.number_of_plan_days_exhausted += (
                instance.no_of_days_requested
            )
            employee_limits.number_of_plan_days_left -= (
                employee_limits.number_of_days_exhausted
            )
            employee_limits.save()


@receiver(pre_save, sender=LeaveLimits)
def create_employee_leave_limits(sender, instance, **kwargs):
    employee = Employee.objects.all()
    if instance:
        instance.leave_name = instance.leave_type.name
        instance.leave_type_id = instance.leave_type.code
        instance.company_id = instance.leave_type.company.id
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
                        company=Company.objects.get(id=instance.leave_type.company.id),
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
