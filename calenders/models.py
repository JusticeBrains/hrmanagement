from django.db import models

from django.utils.translation import gettext_lazy as _

class Period(models.Model):
    date = models.DateField(_("Date"))
    active = models.BooleanField(_("Active"), blank=True, null=True)

    @property
    def month(self):
        return self.date.month
    
    @property
    def year(self):
        return self.date.year
    
    class Meta:
        verbose_name = "Period"
        verbose_name_plural = "Periods"
    
    def __str__(self) -> str:
        return f"{self.month},{self.year}"
    
    def __repr__(self) -> str:
        return f"{self.month},{self.year}"
