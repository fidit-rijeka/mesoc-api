from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import DecimalField, Form, IntegerField

from .models import City


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
