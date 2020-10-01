from celery import shared_task
from celery.schedules import crontab
from .models import Image


@shared_task
def clear_latest_prop():
    Image.objects.filter(show_later=True).update(show_later=False)
