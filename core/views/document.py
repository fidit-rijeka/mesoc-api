import celery

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet


from .. import tasks
from ..forms import DocumentImpactsForm
from ..models import Document
from ..permissions import IsVerified
from ..serializers.cell import CellSerializer
from ..serializers.document import DocumentUploadSerializer, DocumentSerializer
from ..serializers.impact import DocumentImpactSerializer


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

    @action(methods=('get',), detail=True)
    def impacts(self, request, pk=None):
        form = DocumentImpactsForm(request.query_params)

        if form.is_valid():
            document = self.get_object()
            impacts = document.document_impacts.prefetch_related('keywords')
            impacts = impacts.filter(impact__column=form.cleaned_data['column'])
            status = HTTP_200_OK
            data = DocumentImpactSerializer(impacts, many=True, context={'request': self.request}).data
        else:
            data = form.errors
            status = HTTP_400_BAD_REQUEST

        return Response(
            status=status,
            data=data
        )

    def get_serializer(self, *args, **kwargs):
        context = {'request': self.request}
        return self.serializer_classes.get(self.action, self.serializer_class)(*args, context=context, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        document_id = response.data['url'].split('/')[-2]
        celery.chain(
            tasks.read_contents.si(document_id),
            tasks.translate.s(),
            tasks.extract_keywords.s(),
            tasks.classify_document.s(),
            tasks.extract_impacts.s(document_id),
            tasks.commit_results.s(document_id),
            tasks.mail_results.si(document_id)
        ).apply_async(link_error=tasks.fail_document.si(document_id))

        return response
