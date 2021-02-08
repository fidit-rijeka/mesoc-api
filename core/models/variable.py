from django.core.validators import MinLengthValidator, MinValueValidator
from django.db.models import CharField, IntegerField, Model


class Variable(Model):
    id = IntegerField(primary_key=True, validators=(MinValueValidator(0),))
    name = CharField(max_length=60, validators=(MinLengthValidator(1),))
