from django.utils import timezone


from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = Token.objects.select_related('user').get(key=response.data['token']).user
        user.last_login = timezone.now()
        user.save()

        if response.status_code == HTTP_200_OK:
            response = Response(
                status=HTTP_200_OK,
                data={'token': response.data['token'], 'verified': user.verified}
            )

        return response
