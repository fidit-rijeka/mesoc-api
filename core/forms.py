from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField, ChoiceField, Form, IntegerField, ModelChoiceField

from core.models import Impact, Location, RepositoryDocument


class AggregateHeatmapForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    location_id = ChoiceField(
        choices=[(id_, id_) for id_ in Location.objects.values_list('location_id', flat=True)],
        required=False
    )


class AggregateCellSimilarityForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    cell = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    location_id = ChoiceField(choices=[(id_, id_) for id_ in Location.objects.values_list('location_id', flat=True)])


class AggregateImpactForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    location_id = ChoiceField(
        choices=[(id_, id_) for id_ in Location.objects.values_list('location_id', flat=True)],
        required=False
    )
    column = IntegerField(min_value=0, max_value=2)


class AggregateImpactSimilarityForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    location_id = ChoiceField(choices=[(id_, id_) for id_ in Location.objects.values_list('location_id', flat=True)])
    impact = ModelChoiceField(queryset=Impact.objects.all())


class DocumentImpactsForm(Form):
    column = IntegerField(min_value=0, max_value=2)


class LocationForm(Form):
    address = CharField(max_length=150)
