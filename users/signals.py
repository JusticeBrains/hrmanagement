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


@receiver(post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:  # Only perform actions for newly created instances
        try:
            print("---------------Sending -----------------------")
            subject = "Login Credentials"
            message = f"Hello {instance.first_name} your password to sign in is {instance.generated_pass}"
            from_email = env.str("EMAIL_USER")
            recipient_list = [instance.email, from_email]
            for email in recipient_list:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise ValueError(f"Invalid email address: {email}")
            send_mail(subject, message, from_email, recipient_list)
            instance.generated_pass = None
            instance.save()
            print("---------------Sent -----------------------")
            del instance.generated_pass  # Delete the generated_pass attribute
        except ValueError as ve:
            print(f"Error occurred while sending email: {str(ve)}")
        except Exception as e:
            print("Error occurred while sending email:")
            print(str(e))
            traceback.print_exc()
        else:
            post_save.disconnect(user_created, sender=CustomUser)
            instance.save()
            post_save.connect(user_created, sender=CustomUser)


@receiver(post_save, sender=CustomUser)
def updated_multiple_companies(sender, instance, *args, **kwargs):
    post_save.disconnect(updated_multiple_companies, sender=CustomUser)
    if instance:
        employee = Employee.objects.get(id=instance.employee_id.id)
        if instance.is_hr == 1:
            if employee:
                instance.unique_code = employee.unique_code

                company = Company.objects.filter(unique_code=instance.unique_code)

                if len(company) > 1:
                    instance.multiple_companies = 1
                elif len(company) <= 1:
                    instance.multiple_companies = 0

        elif instance.is_hr == 0:
            instance.unique_code = employee.unique_code
            instance.multiple_companies = 0

        if instance.companies:
            company_dicts = []
            for company in instance.companies.all():
                comp = Company.objects.get(id=company.id)
                company_dicts.append({"company_id": str(company.id), "name": comp.name})
            comp_json = [{"companies": company_dicts}]
            instance.company_names = comp_json
        instance.save()
    post_save.connect(updated_multiple_companies, sender=CustomUser)
