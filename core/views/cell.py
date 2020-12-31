from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from ..models import Cell
from ..permissions import IsVerified
from ..serializers.cell import CellSerializer, CellVariableSerializer


class CellViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer
    permission_classes = (IsAuthenticated, IsVerified)

    def get_queryset(self):
        return super().get_queryset().filter(document__user=self.request.user)

    @action(methods=('get',), detail=True)
    def variables(self, request, pk=None):
        cell_variables = self.get_object().cellvariable_set.all()
        cvs = CellVariableSerializer(cell_variables, many=True, context={'request': self.request})
        return Response(data=cvs.data, status=HTTP_200_OK)
