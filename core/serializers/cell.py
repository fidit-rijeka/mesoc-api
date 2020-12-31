from rest_framework.reverse import reverse
from rest_framework.serializers import CharField, HyperlinkedModelSerializer, SerializerMethodField

from ..models import Cell, CellVariable


class CellSerializer(HyperlinkedModelSerializer):
    variables = SerializerMethodField()

    class Meta:
        model = Cell
        fields = ('order', 'classification', 'num_keywords', 'variables', 'document', 'url')

    def get_variables(self, obj):
        return reverse('cell-variables', args=(obj.pk,), request=self.context['request'])


class CellVariableSerializer(HyperlinkedModelSerializer):
    name = CharField(max_length=30, read_only=True, source='variable.name')

    class Meta:
        model = CellVariable
        fields = ('name', 'num_ontology_categories', 'num_keyword_vars', 'strength', 'cell',)
        read_only_fields = ('num_ontology_categories', 'num_keyword_vars', 'strength', 'cell',)
