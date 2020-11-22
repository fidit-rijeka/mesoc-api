from rest_framework.serializers import BooleanField, ModelSerializer

from ..models import Verification


class VerificationSerializer(ModelSerializer):
    verified = BooleanField(source='user.verified')

    class Meta:
        model = Verification
        fields = ('id', 'verified')
        read_only_fields = ('id', 'verified')
