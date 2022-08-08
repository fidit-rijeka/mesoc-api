import collections

from django.conf import settings
from django.db.models import Count

from rest_framework.reverse import reverse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

import nltk

from core.forms import (
    AggregateCellSimilarityForm, AggregateHeatmapForm, AggregateImpactForm, AggregateImpactSimilarityForm
)
from core.models import (
    RepositoryCell, RepositoryCellKeyword, RepositoryDocument, RepositoryDocumentImpact, RepositoryDocumentLocation,
    Location
)

from core.serializers.repository import SimilarDocumentSerializer
from core.serializers.location import GeocodedLocationSerializer

from core.nlp.processing import KeyphraseToKeywordProcessor
from core.nlp.processing import keyword_processing


class AggregateLocationView(APIView):
    def get(self, request):
        aggregate = RepositoryDocumentLocation.objects

        type_ = getattr(RepositoryDocument, request.query_params.get('type', '').upper(), '')
        aggregate = aggregate.filter(document__type=type_) if type_ else aggregate
        aggregate = aggregate.values('document__type', 'location').annotate(doc_count=Count('document'))

        locations = collections.OrderedDict()
        for a in aggregate:
            id_ = a['location']

            if id_ not in locations:
                locations[id_] = [0, 0]

            dt = a['document__type']
            dt_index = 0 if dt == RepositoryDocument.SCIENTIFIC else 1
            locations[id_][dt_index] += a['doc_count']

        data = []
        places = Location.objects.filter(id__in=locations.keys()).order_by('id')
        for place in places:
            d = GeocodedLocationSerializer(place, context={'request': request}).data
            d.update(
                {
                    'num_scientific': locations[place.pk][0],
                    'num_pilot': locations[place.pk][1],
                    'heatmap': '{}?location_id={}'.format(
                        reverse('aggregate-heatmap', request=request),
                        place.location_id
                    )
                }
            )
            locations.pop(place.pk)
            data.append(d)

        return Response(data=data, status=HTTP_200_OK)


class AggregateHeatmapView(APIView):
    form_class = AggregateHeatmapForm

    def get(self, request):
        form = self.form_class(request.query_params)

        if form.is_valid():
            type_ = form.cleaned_data['type'] if form.cleaned_data['type'] != '' else None
            id_ = form.cleaned_data['location_id'] if form.cleaned_data['location_id'] != '' else None
            aggregate = RepositoryCell.objects.get_aggregate(id_, type_)
            if id_:
                for a in aggregate:
                    a['similar_documents'] = '{}?location_id={}&cell={}'.format(
                        reverse('aggregate-cell-similar', request=request),
                        id_,
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
            type_ = form.cleaned_data['type'] if form.cleaned_data['type'] != '' else None
            cell = form.cleaned_data['cell']
            id_ = form.cleaned_data['location_id']

            agg_keywords = RepositoryCellKeyword.objects.get_aggregate_keywords(cell, id_, type_)
            processor = KeyphraseToKeywordProcessor()
            agg_keywords = set(processor.process(agg_keywords))

            if agg_keywords:
                cells = RepositoryCell.objects.filter(
                    cell=cell,
                ).exclude(
                    document__locations__location_id=id_,
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
            column = form.cleaned_data['column']
            id_ = form.cleaned_data['location_id'] if form.cleaned_data['location_id'] else None
            type_ = form.cleaned_data['type'] if form.cleaned_data['type'] else None

            aggregate = RepositoryDocumentImpact.objects.get_aggregate(column, id_, type_)

            for a in aggregate:
                impact_id = a.pop('impact_id')
                if id_:
                    a['similar_documents'] = '{}?location_id={}&impact={}'.format(
                        reverse('aggregate-impact-similar', request=request),
                        id_,
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
            id_ = form.cleaned_data['location_id'] if form.cleaned_data['location_id'] != '' else None
            type_ = form.cleaned_data['type'] if form.cleaned_data['type'] != '' else None

            aggregate_keywords = RepositoryDocumentImpact.objects.get_aggregate_keywords(
                impact,
                id_,
                type_
            )

            processor = keyword_processing.KeyphraseToKeywordProcessor()
            aggregate_keywords = set(processor.process(aggregate_keywords))

            if aggregate_keywords:
                impacts = RepositoryDocumentImpact.objects.filter(
                    impact=impact,
                ).exclude(
                    document__locations__location_id=id_
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
