from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from options.text_options import ASSIGNEDAREA
from django.utils import timezone
import uuid

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("Id"), primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _("Username"), max_length=50, unique=True, blank=True, null=True
    )
    assigned_area = models.CharField(
        _("Assigned Area"),
        max_length=50,
        choices=ASSIGNEDAREA.choices,
        null=True,
        blank=True,
    )
    email = models.EmailField(_("Email"), max_length=254, unique=False)
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    is_super = models.PositiveIntegerField(_("Is Super"), default=0)
    is_hr = models.PositiveIntegerField(_("Is Hr"), default=0)
    is_active = models.PositiveIntegerField(
        _("Is Active"), null=True, blank=True, default=1
    )
    is_staff = models.BooleanField(default=False)
    is_admin = models.PositiveIntegerField(
        _("Is Admin"), blank=True, null=True, default=0
    )
    date_joined = models.DateTimeField(_("Date Joined"), default=timezone.now)
    is_verified = models.CharField(
        _("Is Verified"), max_length=50, blank=True, null=True, default=0
    )
    emp_code = models.CharField(
        _("Employee Code"), max_length=50, blank=True, null=True
    )
    employee_level = models.CharField(
        _("Employee Level"), max_length=50, blank=True, null=True
    )
    profile_pic = models.TextField(_("Profile Pic"), null=True, blank=True)
    is_super_hr = models.PositiveIntegerField(_("Is Super HR"), default=0)
    staff_category = models.CharField(
        _("Staff Category"), max_length=50, blank=True, null=True
    )
    company = models.ForeignKey(
        "company.Company",
        verbose_name=_("Company"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    unique_code = models.CharField(
        _("Unique Code"), max_length=50, null=True, blank=True
    )
    is_accountant = models.PositiveIntegerField(
        _("Is Accountant"), blank=True, null=True, default=0
    )
    is_gm = models.PositiveIntegerField(_("Is GM"), default=0)
    generated_pass = models.CharField(
        _("Generated Password"), max_length=150, null=True, blank=True
    )

    employee_id = models.ForeignKey(
        "employee.Employee",
        verbose_name=_("Employee ID"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    multiple_companies = models.PositiveIntegerField(
        _("Is Multiple Companies"), default=0
    )
    companies = models.ManyToManyField(
        "company.Company",
        verbose_name=_("Multiple Companies"),
        related_name="multi_companies",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "email",
    ]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
