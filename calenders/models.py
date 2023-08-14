import uuid
from django.db import models

from django.utils.translation import gettext_lazy as _


class Period(models.Model):
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(_("Code"), max_length=50, blank=True, null=True)
    period_no = models.CharField(_("Period No"), max_length=50, blank=True, null=True)
    period_name = models.CharField(
        _("Period Name"), max_length=150, blank=True, null=True
    )
    no_of_days = models.PositiveIntegerField(_("No Of Days"), blank=True, null=True)
    no_of_hours = models.PositiveIntegerField(_("No Of Hours"), blank=True, null=True)
    no_of_hours_per_day = models.PositiveIntegerField(
        _("No Of Hours Per Day"), blank=True, null=True
    )
    no_of_working_days = models.PositiveIntegerField(
        _("No Of Working Days"), blank=True, null=True
    )
    calender_year = models.PositiveIntegerField(
        _("Calender Year"), blank=True, null=True
    )
    closed = models.BooleanField(_("Closed"), default=False)
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)

    class Meta:
        verbose_name = "Period"
        verbose_name_plural = "Periods"

    def __str__(self) -> str:
        return f"{self.code}"

    def __repr__(self) -> str:
        return f"{self.code}"
