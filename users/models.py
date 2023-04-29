from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from options.text_options import ASSIGNEDAREA
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Username"), max_length=50, unique=True, blank=True, null=True)
    assigned_Area = models.CharField(_("Assigned Area"), max_length=50, choices=ASSIGNEDAREA.choices, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=254, unique=False)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    is_super = models.PositiveIntegerField(_("Is Super"), default=0)
    is_hr = models.PositiveIntegerField(_("Is Hr"), default=0)
    is_active = models.PositiveIntegerField(_("Is Active"), null=True, blank=True, default=0)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)
    is_verified = models.CharField(_("Is Verified"), max_length=50, blank=True, null=True, default=0)
    emp_code = models.CharField(_("Employee Code"), max_length=50, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
