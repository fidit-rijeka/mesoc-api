import nltk

from django.conf import settings

from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from core.models import DocumentImpact, RepositoryDocumentImpact
from core.nlp.processing.keyword_processing import KeyphraseToKeywordProcessor
from core.serializers.impact import DocumentImpactSerializer
from core.serializers.repository import SimilarDocumentSerializer
from core.permissions import IsVerified


class DocumentImpactViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = DocumentImpact.objects.all()
    serializer_class = DocumentImpactSerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        return super().get_queryset().filter(document__user=self.request.user)

    @action(methods=('get',), detail=True)
    def similar(self, request, pk=None):
        document_impact = self.get_object()

        document_city = document_impact.document.cities.filter(documentcity__primary=True).get()
        document_impacts = RepositoryDocumentImpact.objects.exclude(
            document__cities__longitude=document_city.longitude,
            document__cities__latitude=document_city.latitude,
        )

        document_impacts = document_impacts.filter(impact__column=document_impact.impact.column)
        document_impacts = document_impacts.select_related('document').prefetch_related('keywords')

        top = []
        processor = KeyphraseToKeywordProcessor()
        impact_keywords = document_impact.keywords.values_list('value', flat=True)
        impact_keywords = set(processor.process(impact_keywords))
        if impact_keywords:
            for i in document_impacts:
                keywords = set(processor.process(i.keywords.values_list('value', flat=True)))
                similarity = 1 - nltk.jaccard_distance(impact_keywords, keywords)

                if similarity >= settings.CORE_CELL_SIMILARITY_THRESHOLD:
                    top.append((i.document, similarity))

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
