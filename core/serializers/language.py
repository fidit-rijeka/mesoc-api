from rest_framework.serializers import HyperlinkedModelSerializer

from ..models import Language


class LanguageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'name', 'url',)
        read_only_fields = ('url',)
