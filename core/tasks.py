from django.core import mail

from celery import shared_task


@shared_task
def send_mail(subject, message, from_, to):
    mail.send_mail(subject, message, from_, to)
