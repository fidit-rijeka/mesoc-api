from rest_framework.fields import CharField, IntegerField, SerializerMethodField
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from core.models import ImpactKeyword, DocumentImpact


class ImpactKeywordSerializer(ModelSerializer):
    class Meta:
        model = ImpactKeyword
        fields = ('value',)


class DocumentImpactSerializer(HyperlinkedModelSerializer):
    impact = CharField(max_length=100, read_only=True, source='impact.value')
    column = IntegerField(read_only=True, source='impact.column')
    keywords = SerializerMethodField()
    similar = SerializerMethodField()

    class Meta:
        model = DocumentImpact
        fields = (
            'impact',
            'column',
            'strength',
            'keywords',
            'similar',
            'document',
            'url'
        )
        read_only_fields = ('impact', 'column', 'strength', 'document')

    def get_keywords(self, obj):
        return obj.keywords.values_list('value', flat=True)

    def get_similar(self, obj):
        return reverse('documentimpact-similar', args=(obj.pk,), request=self.context['request'])
