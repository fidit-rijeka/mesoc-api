from django.utils.timezone import now

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

    def validate(self, attrs):
        validated = super().validate(attrs)

        user = self.context['request'].user

        if user.verified:
            raise ValidationError(detail='User is already verified.')

        if not self.Meta.model.objects.filter(uuid=validated['uuid'], expires_at__gt=now(), user=user).exists():
            raise ValidationError({'uuid': ['Specified UUID is not valid or has expired.']})

        return attrs

    def get_user(self, obj):
        return reverse('account', request=self.context['request'])

    def save(self):
        v = self.Meta.model.objects.filter(uuid=self.validated_data['uuid']).select_related('user').get()
        v.user.verified = True
        v.user.save()

        return v
