from django.contrib import auth

from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..permissions import IsVerified, IsSelf
from ..serializers.user import UserSerializer


class UserViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ('post', 'patch', 'put')
    serializer_class = UserSerializer
    queryset = auth.get_user_model().objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permissions = (AllowAny,)
        else:
            permissions = (IsAuthenticated, IsVerified, IsSelf)

        return (permission() for permission in permissions)
