from django.conf import settings
from django.db.models import Model, CharField, DecimalField

from core.geo_api.geo_api import GoogleGeoAPI


class Location(Model):
    city = CharField(max_length=70, blank=True)
    country = CharField(max_length=70)
    longitude = DecimalField(max_digits=22, decimal_places=16, default=43.700278)
    latitude = DecimalField(max_digits=22, decimal_places=16, default=15.489444)

    @property
    def address(self):
        return '{}, {}'.format(self.city, self.country) if self.city else self.country

    @classmethod
    def search_api(cls, address):
        api = GoogleGeoAPI(settings.CORE_GOOGLE_GEO_API_KEY)
        locations = []
        for loc in api.search(address):
            try:
                obj = Location.objects.filter(
                    city=loc.city,
                    country=loc.country,
                    latitude=loc.latitude,
                    longitude=loc.longitude
                ).get()
            except cls.DoesNotExist:
                obj = cls(city=loc.city, country=loc.country, latitude=loc.latitude, longitude=loc.longitude)

            locations.append(obj)

        return locations

    def __str__(self):
        return self.address