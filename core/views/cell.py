import nltk

from django.conf import settings

from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from ..models import Cell, RepositoryCell
from ..permissions import IsVerified
from ..serializers.cell import CellSerializer
from ..serializers.repository import SimilarDocumentSerializer

from ..nlp.processing import KeyphraseToKeywordProcessor


class CellViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        return super().get_queryset().filter(document__user=self.request.user)

    @action(methods=('get',), detail=True)
    def similar(self, request, pk=None):
        document_cell = self.get_object()

        document_location = document_cell.document.locations.filter(documentlocation__primary=True).get()

        cells = RepositoryCell.objects.filter(
            cell=document_cell.cell,
        ).exclude(
            document__locations__location_id=document_location.location_id
        ).select_related('document').prefetch_related('keywords')

        top = []
        processor = KeyphraseToKeywordProcessor()
        document_keywords = document_cell.document.keywords.values_list('value', flat=True)
        document_keywords = set(processor.process(document_keywords))
        if document_keywords:
            for c in cells:
                keywords = set(processor.process(c.keywords.values_list('value', flat=True)))
                similarity = 1 - nltk.jaccard_distance(document_keywords, keywords)

                if similarity >= settings.CORE_CELL_SIMILARITY_THRESHOLD:
                    top.append((c.document, similarity))

            top = sorted(top, key=lambda x: x[1], reverse=True)[:settings.CORE_NUM_SIMILAR_DOCUMENTS]
            similarities = dict([(d[0].pk, d[1]) for d in top])
        else:
            top = []
            similarities = {}

        document_serializer = SimilarDocumentSerializer(
            [d[0] for d in top],
            many=True,
            context={'similarities': similarities}
        )

        return Response(data=document_serializer.data, status=HTTP_200_OK)
