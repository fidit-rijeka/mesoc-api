from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..models import Language
from ..permissions import IsVerified
from ..serializers.language import LanguageSerializer


class LanguageViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        qs = super().get_queryset()
        language = self.request.query_params.get('language', None)
        return qs.filter(name__istartswith=language) if language else qs
