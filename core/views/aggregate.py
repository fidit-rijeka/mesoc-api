import collections
import decimal

from django.conf import settings
from django.db.models import Avg, Count

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView, Response

import nltk

from ..forms import AggregateCellSimilarityForm
from ..models import City, RepositoryCell, RepositoryCellKeyword, RepositoryDocument, RepositoryDocumentCity
from ..serializers.city import CitySerializer
from ..serializers.repository import SimilarDocumentSerializer


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
        except ValueError:
            latitude = None

        try:
            longitude = decimal.Decimal(request.query_params.get('longitude', ''))
        except ValueError:
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
            agg_keywords = set(RepositoryCellKeyword.objects.filter(
                cell__order=form.cleaned_data['cell'],
                cell__document__cities__longitude=form.cleaned_data['longitude'],
                cell__document__cities__latitude=form.cleaned_data['latitude']
            ).values_list('value', flat=True))

            cells = RepositoryCell.objects.filter(
                order=form.cleaned_data['cell'],
            ).exclude(
                document__cities__longitude=form.cleaned_data['longitude'],
                document__cities__latitude=form.cleaned_data['latitude']
            ).select_related('document').prefetch_related('keywords')

            top = []
            for cell in cells:
                keywords = set(cell.keywords.values_list('value', flat=True))

                similarity = 1 - nltk.jaccard_distance(agg_keywords, keywords)
                top.append((cell.document, similarity))

            top = sorted(top, key=lambda x: x[1], reverse=True)[:settings.CORE_NUM_SIMILAR_DOCUMENTS]
            similarities = dict([(d[0].pk, d[1]) for d in top])

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
