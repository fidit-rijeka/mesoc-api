from django.contrib import auth

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import PasswordReset
from ..serializers.password import PasswordResetConfirmationSerializer, PasswordResetRequestSerializer


class PasswordResetViewSet(CreateModelMixin, GenericViewSet):
    http_method_names = ('post',)
    serializer_class = PasswordResetRequestSerializer
    queryset = PasswordReset.objects.all()

    def create(self, request, *args, **kwargs):
        prs = self.get_serializer(data=request.data)
        if prs.is_valid():
            try:
                user = auth.get_user_model().objects.filter(email=prs.validated_data['user']['email']).get()
                pr, created = self.queryset.model.objects.get_or_create(user=user)
                if not created:
                    pr.regenerate()
                    pr.save()
            except auth.get_user_model().DoesNotExist:
                pass

            http_status = status.HTTP_202_ACCEPTED
            data = None
        else:
            http_status = status.HTTP_400_BAD_REQUEST
            data = prs.errors

        return Response(status=http_status, data=data)

    @action(methods=('post',), detail=False)
    def confirmation(self, request, pk=None):
        prs = PasswordResetConfirmationSerializer(data=request.data, context={'request': self.request})
        if prs.is_valid():
            pr = prs.save()
            http_status = status.HTTP_204_NO_CONTENT
            data = None
            pr.delete()
        else:
            http_status = status.HTTP_400_BAD_REQUEST
            data = prs.errors

        return Response(status=http_status, data=data)
