from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import Response
from rest_framework.viewsets import ViewSet

from ..models import Verification
from ..permissions import IsOwner
from ..serializers.verification import VerificationSerializer


class VerificationViewSet(ViewSet):
    permission_classes = (IsAuthenticated, IsOwner)

    def create(self, request, *args, **kwargs):
        if not request.user.verified:
            Verification.objects.filter(user=self.request.user).delete()
            Verification.objects.create(user=self.request.user)

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'non_field_errors': ['User already verified.']})

    def partial_update(self, request, *args, **kwargs):
        try:
            v = Verification.objects.get(id=self.kwargs.get('pk'))
            self.check_object_permissions(request, v)

            v.user.verified = True
            v.user.save()

            response = Response(status=status.HTTP_200_OK, data=VerificationSerializer(instance=v).data)
            v.delete()
        except Verification.DoesNotExist:
            response = Response(status=status.HTTP_404_NOT_FOUND, data={'detail': 'Not found.'})

        return response
