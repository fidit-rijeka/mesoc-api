import getpass

import django.core.signals
import django.db.models.signals

from django.contrib.auth import get_user_model, password_validation
from django.core.management import BaseCommand
from django.core.validators import ValidationError, validate_email

from rest_framework.authtoken.models import Token

from core import signals


class Command(BaseCommand):
    User = get_user_model()
    help = 'Create a new user with export API permission.'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument('email', help='User\'s email address.')

    def _disconnect_verification_signal(self):
        django.db.models.signals.post_save.disconnect(signals.create_verification, type(self).User)

    def _connect_verification_signal(self):
        django.db.models.signals.post_save.connect(signals.create_verification, type(self).User)

    def _validate_email(self, email):
        validate_email(email)
        if type(self).User.objects.filter(email=email).exists():
            raise ValidationError('User with the specified email address already exists.', code='invalid')

    def _validate_password(self, password, email):
        password_validation.validate_password(password, type(self).User(email=email))

    def handle(self, *args, **options):
        email = options['email']

        try:
            self._validate_email(email)
            password = getpass.getpass()
            self._validate_password(password, email)

            self._disconnect_verification_signal()
            u = type(self).User.objects.create_user(email, password)
            u.verified = True
            u.can_use_export_api = True
            u.save()
            self._connect_verification_signal()

            token = Token.objects.filter(user=u).values_list(flat=True)[0]
            self.stdout.write(
                self.style.SUCCESS('Export user created successfully with the following API key: {}.'.format(token))
            )
        except ValidationError as e:
            for msg in e.messages:
                self.stdout.write(self.style.ERROR(msg))
        except KeyboardInterrupt:
            pass
