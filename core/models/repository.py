from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator
from django.db.models import (
    Avg, BooleanField, CASCADE, CharField, DateTimeField, FloatField, ForeignKey, IntegerField, Manager,
    ManyToManyField, Model, PositiveIntegerField, UniqueConstraint
)


class RepositoryDocumentImpactManager(Manager):
    def get_aggregate(self, column, latitude=None, longitude=None, type_=None):
        aggregate = self.select_related('document').select_related('impact').prefetch_related('keywords')

        aggregate = aggregate.filter(impact__column=column)
        aggregate = aggregate.filter(document__cities__latitude=latitude) if latitude else aggregate
        aggregate = aggregate.filter(document__cities__longitude=longitude) if latitude else aggregate
        aggregate = aggregate.filter(document__type=type_) if type_ else aggregate

        aggregate_values = aggregate.values('impact__id', 'impact__column', 'impact__value').distinct()
        aggregate_values = aggregate_values.annotate(avg_strength=Avg('strength'))

        Through = RepositoryDocumentImpact.keywords.through
        keywords = Through.objects.filter(repositorydocumentimpact__id__in=aggregate.values('id'))
        keywords = keywords.select_related('repositorydocumentimpact')
        keywords = keywords.select_related('repositorydocumentimpact__impact')
        keywords = keywords.select_related('impactkeyword')

        impact_keywords = {}
        for kw in keywords:
            try:
                impact_keywords[kw.repositorydocumentimpact.impact.value].add(kw.impactkeyword.value)
            except KeyError:
                impact_keywords[kw.repositorydocumentimpact.impact.value] = {kw.impactkeyword.value}

        data = []
        for av in aggregate_values:
            d = {
                    'impact_id': av['impact__id'],
                    'impact': av['impact__value'],
                    'column': av['impact__column'],
                    'strength': av['avg_strength'],
                    'keywords': impact_keywords[av['impact__value']],
                }
            data.append(d)

        return data

    def get_aggregate_keywords(self, impact, latitude=None, longitude=None, type_=None):
        aggregate = self.select_related('document').select_related('impact').prefetch_related('keywords')

        aggregate = aggregate.filter(impact=impact) if impact else aggregate
        aggregate = aggregate.filter(document__cities__latitude=latitude) if latitude else aggregate
        aggregate = aggregate.filter(document__cities__longitude=longitude) if latitude else aggregate
        aggregate = aggregate.filter(document__type=type_) if type_ else aggregate

        return aggregate.values_list('keywords__value', flat=True)


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
    objects = RepositoryDocumentImpactManager()

    class Meta:
        constraints = (
            UniqueConstraint(fields=('document', 'impact'), name='unique_repository_document_impact'),
        )

    strength = FloatField(validators=(MinValueValidator(0.0), MaxValueValidator(1.0)))
    document = ForeignKey('core.RepositoryDocument', CASCADE, related_name='repository_document_impacts')
    impact = ForeignKey('core.Impact', CASCADE, related_name='impact_repository_documents')
    keywords = ManyToManyField('core.ImpactKeyword', related_name='repository_document_impacts')
