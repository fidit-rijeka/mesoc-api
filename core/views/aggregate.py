import collections
import decimal

from django.conf import settings
from django.db.models import Avg, Count

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

import nltk

from ..forms import AggregateCellSimilarityForm, AggregateImpactForm, AggregateImpactSimilarityForm
from ..models import (
    City, RepositoryCell, RepositoryCellKeyword, RepositoryDocument, RepositoryDocumentCity, RepositoryDocumentImpact
)
from ..serializers.city import CitySerializer
from ..serializers.repository import SimilarDocumentSerializer

from ..nlp.processing import KeyphraseToKeywordProcessor
from ..nlp.processing import keyword_processing


class AggregateLocationView(APIView):
    def get(self, request):
        aggregate = RepositoryDocumentCity.objects

        type_ = getattr(RepositoryDocument, request.query_params.get('type', '').upper(), '')
        aggregate = aggregate.filter(document__type=type_) if type_ else aggregate
        aggregate = aggregate.values('document__type', 'city').annotate(doc_count=Count('document'))

        locations = collections.OrderedDict()
        for city in aggregate:
            id_ = city['city']

            if id_ not in locations:
                locations[id_] = [0, 0]

            dt = city['document__type']
            dt_index = 0 if dt == RepositoryDocument.SCIENTIFIC else 1
            locations[id_][dt_index] += city['doc_count']

        data = []
        cities = City.objects.filter(id__in=locations.keys()).order_by('id')
        for city in cities:
            d = CitySerializer(city, context={'request': request}).data
            d.update(
                {
                    'num_scientific': locations[city.pk][0],
                    'num_pilot': locations[city.pk][1],
                    'heatmap': 'https://api.mesoc.dev/aggregates/heatmap/?latitude={}&longitude={}'.format(
                        city.latitude,
                        city.longitude
                    )
                }
            )
            locations.pop(city.pk)
            data.append(d)

        return Response(data=data, status=HTTP_200_OK)


class AggregateHeatmapView(APIView):
    def get(self, request):
        aggregate = RepositoryCell.objects.select_related('city').select_related('document')

        try:
            latitude = decimal.Decimal(request.query_params.get('latitude', ''))
        except decimal.InvalidOperation:
            latitude = None

        try:
            longitude = decimal.Decimal(request.query_params.get('longitude', ''))
        except decimal.InvalidOperation:
            longitude = None

        type_ = getattr(RepositoryDocument, request.query_params.get('type', '').upper(), '')
        aggregate = aggregate.filter(document__type=type_) if type_ else aggregate
        aggregate = aggregate.filter(document__cities__latitude=latitude) if latitude else aggregate
        aggregate = aggregate.filter(document__cities__longitude=longitude) if longitude else aggregate

        aggregate = aggregate.values('order').annotate(classification=Avg('classification'))

        return Response(data=aggregate, status=HTTP_200_OK)


class AggregateCellSimilarityView(APIView):
    form_class = AggregateCellSimilarityForm

    def get(self, request, *ags, **kwargs):
        form = self.form_class(request.query_params)
        if form.is_valid():
            processor = KeyphraseToKeywordProcessor()
            agg_keywords = RepositoryCellKeyword.objects.filter(
                cell__order=form.cleaned_data['cell'],
                cell__document__cities__longitude=form.cleaned_data['longitude'],
                cell__document__cities__latitude=form.cleaned_data['latitude']
            ).values_list('value', flat=True)
            agg_keywords = set(processor.process(agg_keywords))

            if agg_keywords:
                cells = RepositoryCell.objects.filter(
                    order=form.cleaned_data['cell'],
                ).exclude(
                    document__cities__longitude=form.cleaned_data['longitude'],
                    document__cities__latitude=form.cleaned_data['latitude']
                ).select_related('document').prefetch_related('keywords')

                top = []
                for cell in cells:
                    keywords = set(processor.process(cell.keywords.values_list('value', flat=True)))

                    similarity = 1 - nltk.jaccard_distance(agg_keywords, keywords)
                    if similarity >= settings.CORE_CELL_SIMILARITY_THRESHOLD:
                        top.append((cell.document, similarity))

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

            status = HTTP_200_OK
            data = document_serializer.data
        else:
            status = HTTP_400_BAD_REQUEST
            data = form.errors

        return Response(data=data, status=status)


class AggregateImpactView(APIView):
    form_class = AggregateImpactForm

    def get(self, request):
        form = self.form_class(request.query_params)

        if form.is_valid():
            aggregate = RepositoryDocumentImpact.objects.select_related('document').select_related('impact')
            aggregate = aggregate.prefetch_related('keywords')

            column = form.cleaned_data.get('column')
            aggregate = aggregate.filter(impact__column=column) if column in range(0, 3) else aggregate

            type_ = getattr(RepositoryDocument, form.cleaned_data.get('type', '').upper(), '')
            aggregate = aggregate.filter(document__type=type_) if type_ else aggregate

            latitude = form.data.get('latitude', '')
            longitude = form.data.get('longitude', '')
            aggregate = aggregate.filter(document__cities__latitude=latitude) if latitude else aggregate
            aggregate = aggregate.filter(document__cities__longitude=longitude) if longitude else aggregate

            aggregate_values = aggregate.values('impact__id', 'impact__column', 'impact__value').distinct()
            aggregate_values = aggregate_values.annotate(avg_strength=Avg('strength'))

            Through = RepositoryDocumentImpact.keywords.through
            keywords = Through.objects.filter(
                repositorydocumentimpact__id__in=aggregate.values('id')
            )
            keywords = keywords.select_related('repositorydocumentimpact')
            keywords = keywords.select_related('repositorydocumentimpact__impact')
            keywords = keywords.select_related('impactkeyword')

            impact_keywords = {}
            for kw in keywords:
                try:
                    impact_keywords[kw.repositorydocumentimpact.impact.value].add(kw.impactkeyword.value)
                except KeyError:
                    impact_keywords[kw.repositorydocumentimpact.impact.value] = set([kw.impactkeyword.value])

            impacts = sorted(
                aggregate_values, key=lambda x: x['avg_strength'], reverse=True
            )[:settings.CORE_NUM_SIMILAR_DOCUMENTS]

            data = [
                {
                    'impact': i['impact__value'],
                    'column': i['impact__column'],
                    'strength': i['avg_strength'],
                    'keywords': impact_keywords[i['impact__value']]
                } for i in impacts
            ]
            status = HTTP_200_OK
        else:
            status = HTTP_400_BAD_REQUEST
            data = form.errors

        return Response(data=data, status=status)


class AggregateImpactSimilarityView(APIView):
    form_class = AggregateImpactSimilarityForm

    def get(self, request):
        form = self.form_class(request.query_params)

        if form.is_valid():
            aggregate = RepositoryDocumentImpact.objects.select_related('document').select_related('impact')
            aggregate = aggregate.prefetch_related('keywords')

            type_ = getattr(RepositoryDocument, form.data.get('type', '').upper(), '')
            latitude = form.data.get('latitude', '')
            longitude = form.data.get('longitude', '')
            aggregate = aggregate.filter(impact__column=form.data.get('column'))
            aggregate = aggregate.filter(document__type=type_) if type_ else aggregate
            aggregate = aggregate.filter(document__cities__latitude=latitude) if latitude else aggregate
            aggregate = aggregate.filter(document__cities__longitude=longitude) if longitude else aggregate

            processor = keyword_processing.KeyphraseToKeywordProcessor()
            aggregate_keywords = aggregate.values_list('keywords__value', flat=True)
            aggregate_keywords = set(processor.process(aggregate_keywords))

            if aggregate_keywords:
                impacts = RepositoryDocumentImpact.objects.filter(
                    impact__column=form.cleaned_data['column'],
                ).exclude(
                    document__cities__longitude=form.cleaned_data['longitude'],
                    document__cities__latitude=form.cleaned_data['latitude']
                ).select_related('document').prefetch_related('keywords')

                top = []
                for impact in impacts:
                    keywords = set(processor.process(impact.keywords.values_list('value', flat=True)))

                    similarity = 1 - nltk.jaccard_distance(aggregate_keywords, keywords)
                    if similarity >= settings.CORE_IMPACT_SIMILARITY_THRESHOLD:
                        top.append((impact.document, similarity))

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

            status = HTTP_200_OK
            data = document_serializer.data
        else:
            status = HTTP_400_BAD_REQUEST
            data = form.errors

        return Response(data=data, status=status)
