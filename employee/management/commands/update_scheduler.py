import logging
from typing import Any, Optional

from django.conf import settings
from django.core.management.base import BaseCommand
import requests

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.core.mail import send_mail
from django.conf import settings


logger = logging.getLogger(__name__)

from django.core.management import call_command


def update_employee_record():
    call_command("load_data")
    # Send email report
    try:
        print("---------------Sending -----------------------")
        subject = 'Report'
        message = 'The task has been completed successfully.'
        from_email = "justiceduodu14@gmail.com"
        recipient_list = ['justicemclean@proton.me',]

        send_mail(subject, message, from_email, recipient_list)
        print("---------------Sent -----------------------")
    except:
        print("-----------------Couldn't send------------------------")

@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Run APScheduler."

    def handle(self, *args: Any, **options: Any):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            update_employee_record,
            trigger=CronTrigger(hour="*/1"),
            id="update_employee_record",
            max_instances=1,
            replace_existing=True,
        )

        logger.info("Added job 'update_employee_record'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")