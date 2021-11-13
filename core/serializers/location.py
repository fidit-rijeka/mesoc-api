from rest_framework.serializers import ModelSerializer

from core.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'city', 'country', 'longitude', 'latitude')
