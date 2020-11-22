import datetime

from django.conf import settings
from django.contrib import auth
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from rest_framework.serializers import CharField, EmailField, ModelSerializer, Serializer, UUIDField

from ..models import PasswordReset


class PasswordResetSerializer(Serializer):
    uuid = UUIDField(write_only=True, required=True)
    password = CharField(write_only=True, max_length=128, required=True)

    def validate_uuid(self, uuid):
        if not PasswordReset.objects.filter(uuid=uuid, expires_at__lte=now()).exists():
            raise ValidationError('Invalid UUID.', code='invalid')

        return uuid

    def validate(self, attrs):
        validated = super().validate(attrs)

        pr = PasswordReset.objects.get(uuid=validated['uuid'])
        auth.password_validation.validate_password(password=validated['password'], user=pr.user)

        return validated
