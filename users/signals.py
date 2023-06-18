import re
import traceback
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

from environs import Env

from users.models import CustomUser

env = Env()
env.read_env()

@receiver(post_save, sender=CustomUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        try:
            print("---------------Sending -----------------------")
            subject = "Login Credentials"
            message = (
                f"Hello {instance.first_name} your password to signin is {instance.generated_pass}"
            )
            from_email = env.str("EMAIL_USER")
            recipient_list = [
                instance.email,
                from_email
            ]
            for email in recipient_list:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise ValueError(f"Invalid email address: {email}")
            send_mail(subject, message, from_email, recipient_list)
            instance.generated_pass = make_password(instance.generated_pass)
            print("---------------Sent -----------------------")
        except ValueError as ve:
            print(f"Error occurred while sending email: {str(ve)}")

        except Exception as e:
            print("Error occurred while sending email:")
            print(str(e))
            traceback.print_exc()
    instance.save()
