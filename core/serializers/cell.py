from rest_framework.reverse import reverse
from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField

from ..models import Cell


class CellSerializer(HyperlinkedModelSerializer):
    similar_documents = SerializerMethodField()

    class Meta:
        model = Cell
        fields = ('cell', 'classification', 'similar_documents', 'document', 'url')

    def get_similar_documents(self, obj):
        return reverse('cell-similar', args=(obj.pk,), request=self.context['request'])
