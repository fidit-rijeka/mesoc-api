from rest_framework.authtoken.models import Token


class AuthToken(Token):
    key = 'Bearer'
