from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from .. import tasks
from ..models import Document
from ..permissions import IsVerified
from ..serializers.cell import CellSerializer
from ..serializers.document import DocumentUploadSerializer, DocumentSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    http_method_names = ('get', 'post', 'patch')
    permission_classes = (IsAuthenticated, IsVerified,)
    serializer_class = DocumentSerializer
    serializer_classes = {
        'create': DocumentUploadSerializer,
    }

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(methods=('get',), detail=True)
    def heatmap(self, request, pk=None,):
        document = self.get_object()
        cells = document.cells
        return Response(
            status=HTTP_200_OK,
            data=CellSerializer(cells, many=True, context={'request': self.request}).data
        )

    def get_serializer(self, *args, **kwargs):
        context = {'request': self.request}
        return self.serializer_classes.get(self.action, self.serializer_class)(*args, context=context, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        tasks.process_document.delay(response.data)

        return response
