from django.utils import timezone

from rest_framework.authtoken.views import ObtainAuthToken

from ..models import AuthToken


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = AuthToken.objects.select_related('user').get(key=response.data['token']).user
        user.last_login = timezone.now()
        user.save()

        return response
