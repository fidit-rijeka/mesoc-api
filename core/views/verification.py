from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.viewsets import GenericViewSet

from ..models import Verification
from ..serializers.verification import VerificationSerializer


class VerificationViewSet(CreateModelMixin, GenericViewSet):
    http_method_names = ('post', 'put')
    permission_classes = (IsAuthenticated,)
    serializer_class = VerificationSerializer
    queryset = Verification.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if self.request.user.verified:
            data = {'details': ['User is already verified.']}
            http_status = status.HTTP_400_BAD_REQUEST
        else:
            try:
                v = self.get_queryset().get()
                v.regenerate_uuid()
                v.save()
            except Verification.DoesNotExist:
                self.queryset.model.objects.create()

            data = None
            http_status = status.HTTP_202_ACCEPTED

        return Response(status=http_status, data=data)

    @action(methods=('post',), detail=False)
    def confirmation(self, request, *args, **kwargs):
        vs = self.get_serializer(data=request.data)
        if vs.is_valid():
            self.request.user.verified = True
            self.request.user.save()

            data = None
            http_status = status.HTTP_204_NO_CONTENT

            self.request.user.verification.delete()
        else:
            http_status = status.HTTP_400_BAD_REQUEST
            data = vs.errors

        return Response(status=http_status, data=data)
