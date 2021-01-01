from django.core.validators import MinLengthValidator
from django.db.models import CharField, Model


class Language(Model):
    code = CharField(max_length=2, validators=(MinLengthValidator(2),))
    name = CharField(max_length=20, validators=(MinLengthValidator(2),))
