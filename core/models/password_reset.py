import datetime
import uuid

from django.conf import settings
from django.contrib import auth
from django.db.models import CASCADE, DateTimeField, Model, OneToOneField, UUIDField
from django.utils.timezone import now


class PasswordReset(Model):
    uuid = UUIDField(unique=True, default=uuid.uuid4)
    user = OneToOneField(auth.get_user_model(), CASCADE)
    requested_at = DateTimeField(auto_now_add=True)
    expires_at = DateTimeField(default=now() + datetime.timedelta(days=settings.PASSWORD_RESET_MAX_AGE))

    def regenerate(self):
        self.uuid = uuid.uuid4()
        self.requested_at = now()
        self.expires_at = self.requested_at + datetime.timedelta(days=settings.PASSWORD_RESET_MAX_AGE)
