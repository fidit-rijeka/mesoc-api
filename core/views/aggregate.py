import collections

from django.conf import settings
from django.db.models import Count

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

import nltk

from ..forms import (
    AggregateCellSimilarityForm, AggregateHeatmapForm, AggregateImpactForm, AggregateImpactSimilarityForm
)
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
    form_class = AggregateHeatmapForm

    def get(self, request):
        form = self.form_class(request.query_params)

        if form.is_valid():
            type_ = form.cleaned_data.get('type', '')
            latitude = form.cleaned_data.get('latitude')
            longitude = form.cleaned_data.get('longitude')

            aggregate = RepositoryCell.objects.get_aggregate(latitude, longitude, type_)
            if latitude and longitude:
                for a in aggregate:
                    a['similar_documents'] = '{}?latitude={}&longitude={}&cell={}'.format(
                        reverse('aggregate-cell-similar', request=request),
                        latitude,
                        longitude,
                        a['cell']
                    )

            status = HTTP_200_OK
            data = aggregate
        else:
            status = HTTP_400_BAD_REQUEST
            data = form.errors

        return Response(data=data, status=status)


class AggregateCellSimilarityView(APIView):
    form_class = AggregateCellSimilarityForm

    def get(self, request, *ags, **kwargs):
        form = self.form_class(request.query_params)
        if form.is_valid():
            type_ = form.cleaned_data.get('type', '')
            cell = form.cleaned_data['cell']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            agg_keywords = RepositoryCellKeyword.objects.get_aggregate_keywords(cell, latitude, longitude, type_)
            processor = KeyphraseToKeywordProcessor()
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
            aggregate = RepositoryDocumentImpact.objects.get_aggregate(
                form.cleaned_data['column'],
                form.cleaned_data['latitude'],
                form.cleaned_data['longitude'],
                form.cleaned_data['type']
            )

            for a in aggregate:
                impact_id = a.pop('impact_id')
                if form.cleaned_data['latitude'] and form.cleaned_data['longitude']:
                    a['similar_documents'] = '{}?latitude={}&longitude={}&impact={}'.format(
                        reverse('aggregate-impact-similar', request=request),
                        form.cleaned_data['longitude'],
                        form.cleaned_data['latitude'],
                        impact_id
                    )

            data = sorted(aggregate, key=lambda x: x['strength'], reverse=True)[:settings.CORE_NUM_SIMILAR_DOCUMENTS]
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
            impact = form.cleaned_data['impact']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            type_ = form.cleaned_data['type']

            aggregate_keywords = RepositoryDocumentImpact.objects.get_aggregate_keywords(
                impact,
                latitude,
                longitude,
                type_
            )

            processor = keyword_processing.KeyphraseToKeywordProcessor()
            aggregate_keywords = set(processor.process(aggregate_keywords))

            if aggregate_keywords:
                impacts = RepositoryDocumentImpact.objects.filter(
                    impact=form.cleaned_data['impact'],
                ).exclude(
                    document__cities__longitude=form.cleaned_data['longitude'],
                    document__cities__latitude=form.cleaned_data['latitude']
                ).select_related('document').prefetch_related('keywords')

                impacts = impacts.filter(document__type=type_) if type_ else impacts

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
