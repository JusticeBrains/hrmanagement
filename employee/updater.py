from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command

def update_employee_record():
    call_command('load_data')


def start():
    scheduler = BlockingScheduler()
    scheduler.add_job(update_employee_record, 'interval', hours=1)
    scheduler.start()
