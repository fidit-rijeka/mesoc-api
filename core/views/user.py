from django.contrib import auth

from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from ..permissions import IsVerified
from ..serializers.user import UserSerializer


class UserViewSet(CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    http_method_names = ('get', 'post', 'patch',)
    serializer_class = UserSerializer
    queryset = auth.get_user_model().objects.all()
    permission_classes = (IsAuthenticated, IsVerified)
    action_permission_classes = {
        'create': (AllowAny,),
    }

    def get_object(self):
        return self.get_queryset().get()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def get_permissions(self):
        permissions = self.action_permission_classes.get(self.action, self.permission_classes)
        return (permission() for permission in permissions)
