from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from options.text_options import ASSIGNEDAREA


class CustomUser(AbstractUser):
    fullname = models.CharField(_("Fullname"), max_length=50, blank=True, null=True)
    profile_pic = models.ImageField(_("Profile Pic"),
                                    upload_to='users/profile_pic',
                                    height_field=None, width_field=None,
                                    max_length=None, null=True, blank=True)
    assigned_Area = models.CharField(_("Assigned Area"), max_length=50, choices=ASSIGNEDAREA.choices)
    received_notifications = models.BooleanField(_("Received Notifications"), blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
