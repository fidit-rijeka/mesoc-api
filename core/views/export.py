from django.http import FileResponse

from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet

from core.models import Document
from core.permissions import IsVerified, CanUseExportApi
from core.serializers.export import DocumentExportSerializer


class DocumentExportView(ListModelMixin, GenericViewSet):
    queryset = Document.objects.filter(state=Document.PROCESSED).all()
    http_method_names = ('get',)
    permission_classes = (IsAuthenticated, IsVerified, CanUseExportApi)
    serializer_class = DocumentExportSerializer

    @action(methods=('get',), detail=True)
    def file(self, request, pk=None):
        try:
            doc = Document.objects.filter(id=pk).get()
            return FileResponse(doc.file.open(), as_attachment=True, content_type='application/pdf')
        except Document.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
