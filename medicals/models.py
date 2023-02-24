from django.db import models
from django.utils.translation import gettext_lazy as _

from options.text_options import MEDICALLIMITTYPE


class MedicalCode(models.Model):
    description = models.CharField(_("Description"), max_length=50)
    limit_type = models.CharField(_("Limit Type"), choices=MEDICALLIMITTYPE.choices, max_length=50)
    medical_limit = models.DecimalField(_("Medical Limit"), max_digits=5, decimal_places=2)
    blocked = models.BooleanField(_("Blocked"))

    class Meta:
        verbose_name = "Medical Code"
        verbose_name_plural = "Medical Codes"


class MedicalCenters(models.Model):
    name = models.CharField(_("Name"), max_length=50, )
    address = models.CharField(_("Address"), max_length=50)
    address2 = models.CharField(_("Address 2"), max_length=50, blank=True, null=True)
    contact_number = models.CharField(_("Contact Number"), max_length=50)
    contact_person = models.CharField(_("Contact Person"), max_length=200)
    blocked = models.BooleanField(_("Blocked"))
