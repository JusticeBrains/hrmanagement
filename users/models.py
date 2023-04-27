from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from options.text_options import ASSIGNEDAREA
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)
    assigned_Area = models.CharField(_("Assigned Area"), max_length=50, choices=ASSIGNEDAREA.choices)
    email = models.EmailField(_("Email"), max_length=254, unique=False)
    received_notifications = models.BooleanField(_("Received Notifications"), blank=True, null=True)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    is_super = models.PositiveIntegerField(_("Is Super"), default=0)
    is_hr = models.PositiveIntegerField(_("Is Hr"), default=0)


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
