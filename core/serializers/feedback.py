from django.core.validators import MinLengthValidator

from rest_framework.serializers import CharField, Serializer


class FeedbackSerializer(Serializer):
    subject = CharField(required=True, max_length=50, validators=(MinLengthValidator(1),))
    message = CharField(required=True, max_length=1200, validators=(MinLengthValidator(120),))
