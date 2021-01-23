from django.contrib import auth
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from rest_framework.serializers import (
    CharField, EmailField, HyperlinkedModelSerializer, Serializer, SerializerMethodField, UUIDField
)

from ..models import PasswordReset


class PasswordResetRequestSerializer(Serializer):
    email = EmailField(source='user.email', write_only=True)

    class Meta:
        model = PasswordReset
        fields = ('email',)


class PasswordResetConfirmationSerializer(HyperlinkedModelSerializer):
    uuid = UUIDField(required=True, write_only=True)
    password = CharField(write_only=True, max_length=128, required=True)

    class Meta:
        model = PasswordReset
        fields = ('uuid', 'password', 'user')
        read_only_fields = ('user',)

    def validate_password(self, password):
        auth.password_validation.validate_password(password=password, user=self.context['request'].user)
        return password

    def validate(self, data):
        data = super().validate(data)
        uuid = data['uuid']
        if not PasswordReset.objects.filter(uuid=uuid, expires_at__gt=now()).exists():
            raise ValidationError({'uuid': ['Specified UUID is not valid or has expired.']})

        return data

    def save(self):
        pr = PasswordReset.objects.filter(uuid=self.validated_data['uuid']).select_related('user').get()
        pr.user.set_password(self.validated_data['password'])
        pr.user.save()

        return pr
