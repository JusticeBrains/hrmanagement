from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from options.text_options import ASSIGNEDAREA
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Fullname"), max_length=50, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    profile_pic = models.ImageField(_("Profile Pic"),
                                    upload_to='users/profile_pic',
                                    height_field=None, width_field=None,
                                    max_length=None, null=True, blank=True)
    assigned_Area = models.CharField(_("Assigned Area"), max_length=50, choices=ASSIGNEDAREA.choices)
    received_notifications = models.BooleanField(_("Received Notifications"), blank=True, null=True)
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
