from django.conf import settings
from django.db.models import Model, CharField, DateField, DecimalField, TextField

from core.geo_api.geo_api import GooglePlacesAPI


class Location(Model):
    location_id = TextField()
    address = CharField(max_length=250)
    longitude = DecimalField(max_digits=22, decimal_places=16, default=43.700278)
    latitude = DecimalField(max_digits=22, decimal_places=16, default=15.489444)
    # Used for tracking Google ID expiration. Should be moved along with the ID in its own class.
    updated_at = DateField(auto_now=True, null=True)

    api = GooglePlacesAPI(settings.CORE_GOOGLE_GEO_API_KEY)

    @classmethod
    def search_api(cls, address):
        locations = []
        for loc in cls.api.search(address):
            obj = cls(
                location_id=loc.id_,
                address=loc.address,
                latitude=loc.latitude,
                longitude=loc.longitude
            )

            locations.append(obj)

        return locations

    @classmethod
    def search_api_suggestions(cls, address):
        locations = [cls(location_id=loc.id_, address=loc.address) for loc in cls.api.search_autocomplete(address)]

        return locations

    @classmethod
    def search_api_by_id(cls, id_):
        loc = cls.api.search_place_id(id_)
        return cls(location_id=loc.id_, address=loc.address, latitude=loc.latitude, longitude=loc.longitude)

    @classmethod
    def verify_place_id(cls, id_):
        return cls.api.verify_place_id(id_)

    def __str__(self):
        return self.address
