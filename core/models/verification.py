import datetime
import uuid

from django.conf import settings
from django.contrib import auth
from django.db.models import CASCADE, DateTimeField, Model, OneToOneField, UUIDField
from django.template.loader import render_to_string
from django.utils.timezone import now

from .. import tasks


class Verification(Model):
    uuid = UUIDField(unique=True, default=uuid.uuid4)
    requested_at = DateTimeField(auto_now_add=True)
    expires_at = DateTimeField(default=now() + datetime.timedelta(days=settings.CORE_PASSWORD_RESET_MAX_AGE))
    user = OneToOneField(auth.get_user_model(), CASCADE)

    def regenerate(self):
        self.uuid = uuid.uuid4()
        self.requested_at = now()
        self.expires_at = self.requested_at + datetime.timedelta(days=settings.CORE_PASSWORD_RESET_MAX_AGE)

    def send_by_email(self):
        base_url = settings.CORE_VERIFICATION_BASE_URL
        verification_url = '{}/{}/'.format(base_url, self.uuid)

        tasks.send_mail.delay(
            render_to_string('core/verification_mail_subject.txt'),
            render_to_string('core/verification_mail_message.txt', context={'verification_url': verification_url}),
            None,
            (self.user.email,)
        )
