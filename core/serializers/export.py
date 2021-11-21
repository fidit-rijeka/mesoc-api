from rest_framework.serializers import CharField, IntegerField, ListField, ModelSerializer, SerializerMethodField
from rest_framework.reverse import reverse

from core.models import Cell, Document, DocumentImpact, Language
from core.serializers.location import LocationSerializer


class CellExportSerializer(ModelSerializer):
    class Meta:
        model = Cell
        fields = ('cell', 'cell_2d', 'classification')


class DocumentImpactExportSerializer(ModelSerializer):
    impact = CharField(max_length=100, read_only=True, source='impact.value')
    column = IntegerField(read_only=True, source='impact.column')
    keywords = ListField(source='keywords_list')

    class Meta:
        model = DocumentImpact
        fields = (
            'impact',
            'column',
            'strength',
            'keywords',
        )


class LanguageExportSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = ('code', 'name')


class DocumentExportSerializer(ModelSerializer):
    title = CharField(max_length=100, source='file_title', read_only=True)
    language = LanguageExportSerializer()
    location = LocationSerializer()
    keywords = ListField(source='keywords_list')
    cells = CellExportSerializer(many=True)
    impacts = DocumentImpactExportSerializer(many=True, source='document_impacts')
    file = SerializerMethodField()

    class Meta:
        model = Document
        fields = ('id', 'title', 'abstract', 'type', 'language', 'location', 'keywords', 'cells', 'impacts', 'file')

    def get_file(self, obj):
        return reverse('export-file', args=(obj.pk,), request=self.context['request'])
