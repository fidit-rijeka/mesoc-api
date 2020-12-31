from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..models import City
from ..permissions import IsVerified
from ..serializers.city import CitySerializer


class LocationViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = City.objects.exclude(name='Unknown')
    serializer_class = CitySerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        qs = super().get_queryset()
        city = self.request.query_params.get('city', None)
        country = self.request.query_params.get('country', None)

        qs = qs.filter(name__istartswith=city) if city else qs
        qs = qs.filter(country__name__istartswith=country) if country else qs

        return qs
