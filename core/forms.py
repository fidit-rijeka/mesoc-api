from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField, ChoiceField, DecimalField, Form, IntegerField, ModelChoiceField

from core.models import Impact, Location, RepositoryDocument


class AggregateHeatmapForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    longitude = DecimalField(max_digits=22, decimal_places=16, required=False)
    latitude = DecimalField(max_digits=22, decimal_places=16, required=False)

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude', None)
        if longitude is not None and not Location.objects.filter(longitude=longitude).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return longitude

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude', None)
        if latitude is not None and not Location.objects.filter(latitude=latitude).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return latitude

    def clean(self):
        cleaned_data = super().clean()
        longitude = cleaned_data.get('longitude', None)
        latitude = cleaned_data.get('latitude', None)
        if longitude and latitude is None:
            self.add_error('latitude', 'latitude must be specified along with longitude.')

        if latitude and longitude is None:
            self.add_error('longitude', 'longitude must be specified along with latitude.')

        return cleaned_data


class AggregateCellSimilarityForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    cell = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    longitude = DecimalField(max_digits=22, decimal_places=16)
    latitude = DecimalField(max_digits=22, decimal_places=16)

    def clean_longitude(self):
        if not Location.objects.filter(longitude=self.cleaned_data['longitude']).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return self.cleaned_data['longitude']

    def clean_latitude(self):
        if not Location.objects.filter(latitude=self.cleaned_data['latitude']).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return self.cleaned_data['latitude']


class AggregateImpactForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    longitude = DecimalField(max_digits=22, decimal_places=16, required=False)
    latitude = DecimalField(max_digits=22, decimal_places=16, required=False)
    column = IntegerField(min_value=0, max_value=2)

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude', None)
        if longitude is not None and not Location.objects.filter(longitude=longitude).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return longitude

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude', None)
        if latitude is not None and not Location.objects.filter(latitude=latitude).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return latitude

    def clean(self):
        cleaned_data = super().clean()
        longitude = cleaned_data.get('longitude', None)
        latitude = cleaned_data.get('latitude', None)
        if longitude and latitude is None:
            self.add_error('latitude', 'latitude must be specified along with longitude.')
        
        if latitude and longitude is None:
            self.add_error('longitude', 'longitude must be specified along with latitude.')

        return cleaned_data


class AggregateImpactSimilarityForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    longitude = DecimalField(max_digits=22, decimal_places=16)
    latitude = DecimalField(max_digits=22, decimal_places=16)
    impact = ModelChoiceField(queryset=Impact.objects.all())

    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if not Location.objects.filter(longitude=longitude).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return longitude

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if not Location.objects.filter(latitude=latitude).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return latitude


class DocumentImpactsForm(Form):
    column = IntegerField(min_value=0, max_value=2)


class LocationForm(Form):
    address = CharField(max_length=150)
