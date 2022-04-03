from django.contrib import auth
from django.dispatch import receiver
from django.db.models import signals

from rest_framework.authtoken.models import Token

from .models import Document, PasswordReset, Verification


@receiver(signals.post_save, sender=auth.get_user_model())
def generate_user_token(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        Token.objects.create(user=instance)


@receiver(signals.post_save, sender=auth.get_user_model())
def create_verification(sender, instance, created, **kwargs):
    if created and not kwargs.get('raw', False):
        Verification.objects.create(user=instance)


@receiver(signals.post_save, sender=Verification)
def send_verification_email(sender, instance, created, **kwargs):
    instance.send_by_email()


@receiver(signals.post_save, sender=PasswordReset)
def send_password_reset_email(sender, instance, created, **kwargs):
    instance.send_by_email()


@receiver(signals.post_delete, sender=Document)
def delete_document_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(False)
