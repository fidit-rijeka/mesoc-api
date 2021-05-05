import celery

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
        qs = self.queryset.filter(user=self.request.user)

        state = self.request.query_params.get('state', '')
        state_upper = state.upper()
        if state_upper == 'ACTIVE':
            active_states = [s for s in qs.model.STATES.keys() if s != qs.model.DISMISSED]
            qs = qs.filter(state__in=active_states)
        elif state in qs.model.STATES.values():
            qs = qs.filter(state=getattr(qs.model, state_upper))

        return qs

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

        document_id = response.data['url'].split('/')[-2]
        celery.chain(
            tasks.convert_to_pdf.s(document_id),
            tasks.extract_keywords.s(),
            tasks.classify_document.s(),
            tasks.commit_results.s(document_id),
            tasks.mail_results.si(document_id)
        ).apply_async(link_error=tasks.fail_document.si(document_id))

        return response
