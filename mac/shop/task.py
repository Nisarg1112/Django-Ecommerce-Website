from celery import shared_task
from django.core.mail import send_mail
from time import sleep


@shared_task()
def sleepy(duration):
    sleep(duration)
    return None
