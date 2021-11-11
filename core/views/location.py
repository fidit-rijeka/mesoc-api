from django.conf import settings

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from core.forms import LocationForm
from core.models import Location
from core.permissions import IsVerified
from core.serializers.location import LocationSerializer
from core.geo_api.geo_api import GoogleGeoAPI


class LocationView(APIView):
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticated, IsVerified)
    form_class = LocationForm

    def get(self, request):
        form = type(self).form_class(request.query_params)
        if form.is_valid():
            locations = Location.search_api(form.cleaned_data['address'])
            serializer = LocationSerializer(locations, many=True)

            data = serializer.data
            status = HTTP_200_OK
        else:
            data = form.errors
            status = HTTP_400_BAD_REQUEST

        return Response(status=status, data=data)
