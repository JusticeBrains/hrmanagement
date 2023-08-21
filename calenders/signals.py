import calendar
from datetime import date
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count

from .models import Period, GlobalInputs


@receiver(pre_save, sender=Period)
def populate_date(sender, instance, **kwargs):
    if instance and instance.status == 1:
        cuurent_period = instance
        current_year = instance.period_year.year
        total_working_hours = Period.objects.filter(period_year=instance.period_year, company=instance.company).aggregate(total_working_hours=Sum("total_working_hours"))["total_working_hours"]

        global_input,_ = GlobalInputs.objects.get_or_create(
            current_period=cuurent_period,
            current_year=current_year,
            annual_working_hours=total_working_hours,
            company=instance.period_year.company,
        )
        global_input.save()
