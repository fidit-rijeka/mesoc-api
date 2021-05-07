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
from ..serializers.cell import CellSerializer, CellVariableSerializer
from ..serializers.repository import SimilarDocumentSerializer


class CellViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        return super().get_queryset().filter(document__user=self.request.user)

    @action(methods=('get',), detail=True)
    def similar(self, request, pk=None):
        document_cell = self.get_object()

        document_city = document_cell.document.cities.filter(documentcity__primary=True).get()

        cells = RepositoryCell.objects.filter(
            order=document_cell.order,
        ).exclude(
            document__cities__longitude=document_city.longitude,
            document__cities__latitude=document_city.latitude,
        ).select_related('document').prefetch_related('keywords')

        top10 = []
        document_keywords = set(document_cell.document.keywords.values_list('value', flat=True))
        for c in cells:
            keywords = c.keywords.values_list('value', flat=True)
            similarity = 1 - nltk.jaccard_distance(document_keywords, set(keywords))

            if similarity >= settings.CORE_CELL_SIMILARITY_THRESHOLD:
                top10.append((c.document, similarity))

        top10 = sorted(top10, key=lambda x: x[1], reverse=True)[:10]
        similarities = dict([(d[0].pk, d[1]) for d in top10])

        document_serializer = SimilarDocumentSerializer(
            [d[0] for d in top10],
            many=True,
            context={'similarities': similarities}
        )

        return Response(data=document_serializer.data, status=HTTP_200_OK)

    @action(methods=('get',), detail=True)
    def variables(self, request, pk=None):
        cell_variables = self.get_object().cellvariable_set.all()
        cvs = CellVariableSerializer(cell_variables, many=True, context={'request': self.request})
        return Response(data=cvs.data, status=HTTP_200_OK)
