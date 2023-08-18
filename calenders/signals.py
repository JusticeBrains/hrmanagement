import calendar
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Period


@receiver(post_save, sender=Period)
def populate_date(sender, instance, **kwargs):
    post_save.disconnect(populate_date, sender=Period)
    if instance and instance.month_calendar:
        first_day = instance.month_calendar[0][0]
        last_week = instance.month_calendar[-1]
        last_day = last_week[-1] if last_week[-1] != 0 else last_week[-2]

        if 1 <= first_day <= 31 and 1 <= last_day <= 31:
            instance.start_date = date(
                instance.period_year.year, instance.month, first_day
            )
            instance.end_date = date(
                instance.period_year.year, instance.month, last_day
            )
            instance.period_name = f"{instance.MONTH_NAMES.get(instance.month)} {instance.period_year.year}"
            instance.period_code = f"{instance.MONTH_NAMES.get(instance.month)[:3].upper()}{instance.period_year.year}"
            instance.company = instance.period_year.company

            if instance.total_working_days is None:
                instance.total_working_days = instance.count_working_days(
                instance.start_date, instance.end_date
            )
                instance.total_working_hours = instance.total_working_days * 8
                
            elif instance.total_working_days is not None:
                instance.total_working_days = instance.total_working_days
                instance.total_working_hours = instance.total_working_days * 8


            instance.save()
            print(f"Start Date: {instance.start_date}")
            print(f"End Date: {instance.end_date}")
    post_save.connect(populate_date, sender=Period)
