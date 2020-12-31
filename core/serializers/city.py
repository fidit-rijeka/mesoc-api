from rest_framework.serializers import CharField, HyperlinkedModelSerializer

from ..models import City


class CitySerializer(HyperlinkedModelSerializer):
    city = CharField(max_length=58,  source='name')
    country = CharField(max_length=56,  source='country.name', read_only=True)

    class Meta:
        model = City
        fields = ('city', 'longitude', 'latitude', 'country', 'url')
        read_only_fields = ('url',)
