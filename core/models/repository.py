from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FloatField, ForeignKey, IntegerField, ManyToManyField, Model,
    PositiveIntegerField
)


class RepositoryDocument(Model):
    SCIENTIFIC = 1
    PILOT = 2

    TYPES = {
        SCIENTIFIC: 'scientific',
        PILOT: 'pilot'
    }

    id = PositiveIntegerField(primary_key=True)
    type = IntegerField(choices=TYPES.items())
    document_title = CharField(max_length=400, validators=(MinLengthValidator(1),))
    processed_at = DateTimeField(auto_now=True)
    cities = ManyToManyField('core.City', through='core.RepositoryDocumentCity',)


class RepositoryDocumentCity(Model):
    document = ForeignKey('core.RepositoryDocument', on_delete=CASCADE)
    city = ForeignKey('core.City', on_delete=CASCADE)
    primary = BooleanField(default=True)


class RepositoryCell(Model):
    id = IntegerField(primary_key=True)
    classification = FloatField(validators=(MaxValueValidator(1.0), MinValueValidator(0.0)))
    num_keyword_vars = IntegerField(validators=(MinValueValidator(1),))
    order = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    document = ForeignKey('core.RepositoryDocument', CASCADE, 'cells')


class RepositoryCellKeyword(Model):
    value = CharField(max_length=100)
    cell = ForeignKey('core.RepositoryCell', CASCADE, related_name='keywords')
