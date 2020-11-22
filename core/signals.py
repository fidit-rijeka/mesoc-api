from django.conf import settings
from django.contrib import auth
from django.dispatch import receiver
from django.db.models import signals
from django.template.loader import render_to_string

from rest_framework.authtoken.models import Token

from . import tasks
from .models import PasswordReset, Verification


@receiver(signals.post_save, sender=auth.get_user_model())
def generate_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(signals.post_save, sender=auth.get_user_model())
def create_verification(sender, instance, created, **kwargs):
    if created:
        Verification.objects.create(user=instance)


@receiver(signals.post_save, sender=Verification)
def send_verification_email(sender, instance, created, **kwargs):
    if created:
        if sender == auth.get_user_model():
            Verification.objects.create(user=instance)
            uuid = instance.verification.id
            to = (instance.email,)
        else:
            uuid = instance.id
            to = (instance.user.email,)

        base_url = settings.VERIFICATION_BASE_URL
        verification_url = '{}/{}/'.format(base_url, uuid)

        tasks.send_mail.delay(
            render_to_string('core/verification_mail_subject.txt'),
            render_to_string('core/verification_mail_message.txt', context={'verification_url': verification_url}),
            None,
            to
        )


@receiver(signals.post_save, sender=PasswordReset)
def send_password_reset_email(sender, instance, created, **kwargs):
    base_url = settings.PASSWORD_RESET_BASE_URL
    password_reset_url = '{}/{}/'.format(base_url, instance.uuid)

    tasks.send_mail.delay(
        render_to_string('core/password_reset_mail_subject.txt'),
        render_to_string('core/password_reset_mail_message.txt', context={'password_reset_url': password_reset_url}),
        None,
        (instance.user.email,)
    )
