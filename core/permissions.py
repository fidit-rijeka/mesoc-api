from rest_framework.permissions import BasePermission


class IsVerified(BasePermission):
    message = 'User is not verified'

    def has_permission(self, request, view):
        return request.user and request.user.verified


class CanUseExportApi(BasePermission):
    def has_permission(self, request, view):
        return request.user.can_use_export_api
