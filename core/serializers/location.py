from rest_framework.serializers import ModelSerializer

from core.models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('location_id', 'address')


class GeocodedLocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('location_id', 'address', 'longitude', 'latitude')
