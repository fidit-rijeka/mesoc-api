from rest_framework.permissions import BasePermission


class IsVerified(BasePermission):
    message = 'User is not verified'

    def has_permission(self, request, view):
        return request.user and request.user.verified


class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
