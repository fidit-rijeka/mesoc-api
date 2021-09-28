from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
from django.forms import ChoiceField, DecimalField, Form, IntegerField, ModelChoiceField

from .models import City, Impact, RepositoryDocument


class AggregateCellSimilarityForm(Form):
    cell = IntegerField(validators=(MinValueValidator(0), MaxValueValidator(29)))
    longitude = DecimalField(max_digits=22, decimal_places=16)
    latitude = DecimalField(max_digits=22, decimal_places=16)

    def clean_longitude(self):
        if not City.objects.filter(longitude=self.cleaned_data['longitude']).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return self.cleaned_data['longitude']

    def clean_latitude(self):
        if not City.objects.filter(latitude=self.cleaned_data['latitude']).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return self.cleaned_data['latitude']


class AggregateImpactForm(Form):
    type = ChoiceField(choices=RepositoryDocument.TYPES.items(), required=False)
    longitude = DecimalField(max_digits=22, decimal_places=16, required=False)
    latitude = DecimalField(max_digits=22, decimal_places=16, required=False)
    column = IntegerField(min_value=0, max_value=2)

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude', None)
        if longitude and not City.objects.filter(longitude=longitude).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return longitude

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude', None)
        if latitude and not City.objects.filter(latitude=latitude).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return latitude

    def clean(self):
        cleaned_data = super().clean()
        longitude = cleaned_data['longitude']
        latitude = cleaned_data['latitude']
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
        if not City.objects.filter(longitude=longitude).exists():
            self.add_error('longitude', 'Invalid longitude value.')

        return longitude

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if not City.objects.filter(latitude=latitude).exists():
            self.add_error('latitude', 'Invalid latitude value.')

        return latitude
