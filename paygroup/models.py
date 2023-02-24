from django.db import models
from django.utils.translation import gettext_lazy as _


class PayGroup(models.Model):
    description = models.CharField(_("Description"), max_length=250)
    short_name = models.CharField(_("Short Name"), max_length=50)
