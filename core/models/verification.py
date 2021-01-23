import uuid

from django.conf import settings
from django.contrib import auth
from django.db import models
from django.template.loader import render_to_string

from .. import tasks


class Verification(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    user = models.OneToOneField(auth.get_user_model(), models.CASCADE)

    def regenerate_uuid(self):
        self.uuid = uuid.uuid4()
        return self.uuid

    def send_by_email(self):
        base_url = settings.VERIFICATION_BASE_URL
        verification_url = '{}/{}/'.format(base_url, self.uuid)

        tasks.send_mail.delay(
            render_to_string('core/verification_mail_subject.txt'),
            render_to_string('core/verification_mail_message.txt', context={'verification_url': verification_url}),
            None,
            (self.user.email,)
        )
