import re
import traceback
from django.db import transaction
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
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

            # Update company_names field
            if instance.companies.exists():
                company_dicts = []
                related_companies = instance.companies.all()

                for company in related_companies:
                    company_dicts.append(
                        {"company_id": str(company.id), "name": company.name}
                    )

                with transaction.atomic():
                    instance.company_names = [{"companies": company_dicts}]

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



@receiver(pre_save, sender=CustomUser)
def updated_multiple_companies(sender, instance, **kwargs):
    if instance:
        print("Signal handler called for CustomUser instance:", instance)
        try:
            if instance.companies.exists():
                company_dicts = []
                related_companies = instance.companies.all()

                for company in related_companies:
                    company_dicts.append(
                        {"company_id": str(company.id), "name": company.name}
                    )

                with transaction.atomic():
                    instance.company_names = [{"companies": company_dicts}]
        except Exception as e:
            print("Error creating ---")
            print(str(e))
            traceback.print_exc()
