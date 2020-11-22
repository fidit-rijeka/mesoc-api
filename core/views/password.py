from django.contrib import auth
from django.core.validators import EmailValidator, ValidationError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ..models import PasswordReset
from ..serializers.password import PasswordResetSerializer


class PasswordResetViewSet(ViewSet):
    def create(self, request, *args, **kwargs):
        errors = {}
        email = request.data.get('email')

        try:
            self._validate_email(email)
        except ValidationError as e:
            errors['email'] = e.messages
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            user_model = auth.get_user_model()

            try:
                user = user_model.objects.get(email=email)

                pr, created = PasswordReset.objects.get_or_create(user=user)
                if not created:
                    pr.regenerate()
                    pr.save()
            except user_model.DoesNotExist:
                pass

            response_status = status.HTTP_202_ACCEPTED
            errors = None

        return Response(status=response_status, data=errors)

    def partial_update(self, request, *args, **kwargs):
        ps = PasswordResetSerializer(data=request.data)
        if ps.is_valid():
            pr = PasswordReset.objects.get(uuid=ps.validated_data['uuid'])
            pr.user.set_password(ps.validated_data['password'])
            pr.user.save()
            pr.delete()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=ps.errors)

    def _validate_email(self, email):
        if email is None:
            raise ValidationError('This field is required.', code='required')

        EmailValidator()(email)
