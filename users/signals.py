import re
import traceback
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

from environs import Env

from users.models import CustomUser
from employee.models import Employee
from company.models import Company
env = Env()
env.read_env()

# @receiver(post_save, sender=CustomUser)
# def user_created(sender, instance, created, **kwargs):
#     post_save.disconnect(user_created, sender=CustomUser)
#     if created:
#         pass_gen = instance.generated_pass
#         try:
#             print("---------------Sending -----------------------")
#             subject = "Login Credentials"
#             message = (
#                 f"Hello {instance.first_name} your password to signin is {instance.generated_pass}"
#             )
#             from_email = env.str("EMAIL_USER")
#             recipient_list = [
#                 instance.email,
#                 from_email
#             ]
#             for email in recipient_list:
#                 if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#                     raise ValueError(f"Invalid email address: {email}")
#             send_mail(subject, message, from_email, recipient_list)
#             instance.generated_pass = make_password(pass_gen)
#             instance.save()
#             print("---------------Sent -----------------------")
#         except ValueError as ve:
#             print(f"Error occurred while sending email: {str(ve)}")

#         except Exception as e:
#             print("Error occurred while sending email:")
#             print(str(e))
#             traceback.print_exc()

#     post_save.connect(user_created, sender=CustomUser)


@receiver(post_save, sender=CustomUser)
def updated_multiple_companies(sender, created, instance, *args, **kwargs):
    post_save.disconnect(updated_multiple_companies, sender=CustomUser)
    if created:
        employee = Employee.objects.get(id=instance.employee_id.id)
        if instance.is_hr == 1:
            if employee:
                instance.unique_code = employee.unique_code
                
                company = Company.objects.filter(unique_code=instance.unique_code)

                if len(company) > 1:
                    instance.multiple_companies = 1
    
        elif instance.is_hr == 0:
            instance.unique_code = employee.unique_code
            instance.multiple_companies = 0
        instance.save()
    post_save.connect(updated_multiple_companies, sender=CustomUser)




