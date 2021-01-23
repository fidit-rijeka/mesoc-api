from rest_framework.reverse import reverse
from rest_framework.serializers import (
    BooleanField, HyperlinkedModelSerializer, SerializerMethodField, UUIDField, ValidationError
)

from ..models import Verification


class VerificationSerializer(HyperlinkedModelSerializer):
    uuid = UUIDField(required=True)
    verified = BooleanField(read_only=True, source='user.verified')
    user = SerializerMethodField()

    class Meta:
        model = Verification
        fields = ('uuid', 'verified', 'user')
        read_only_fields = ('user',)

    def validate(self, attrs):
        validated = super().validate(attrs)

        user = self.context['request'].user

        if user.verified:
            raise ValidationError(detail='User is already verified.')

        try:
            v = user.verification
        except Verification.DoesNotExist:
            v = None

        if v is None or v.uuid != validated['uuid']:
            raise ValidationError({'uuid': 'UUID is not associated with the user.'})

        return attrs

    def get_user(self, obj):
        return reverse('account', request=self.context['request'])
