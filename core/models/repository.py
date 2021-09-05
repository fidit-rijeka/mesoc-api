from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db.models import (
    BooleanField, CASCADE, CharField, DateTimeField, FloatField, ForeignKey, IntegerField, ManyToManyField, Model,
    PositiveIntegerField, UniqueConstraint
)


class RepositoryDocument(Model):
    SCIENTIFIC = 'scientific'
    PILOT = 'pilot'

    TYPES = {
        SCIENTIFIC: 'scientific',
        PILOT: 'pilot'
    }

    id = PositiveIntegerField(primary_key=True)
    type = CharField(max_length=10, choices=TYPES.items())
    document_title = CharField(max_length=400, validators=(MinLengthValidator(1),))
    processed_at = DateTimeField(auto_now=True)
    impacts = ManyToManyField(
        'core.Impact',
        through='core.RepositoryDocumentImpact',
        related_name='repository_documents'
    )
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


class RepositoryDocumentImpact(Model):
    class Meta:
        constraints = (
            UniqueConstraint(fields=('document', 'impact'), name='unique_repository_document_impact'),
        )

    strength = FloatField(validators=(MinValueValidator(0.0), MaxValueValidator(1.0)))
    document = ForeignKey('core.RepositoryDocument', CASCADE, related_name='repository_document_impacts')
    impact = ForeignKey('core.Impact', CASCADE, related_name='impact_repository_documents')
    keywords = ManyToManyField('core.ImpactKeyword', related_name='repository_document_impacts')
