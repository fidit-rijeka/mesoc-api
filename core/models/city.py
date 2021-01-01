from django.db.models import CASCADE, CharField, DecimalField, ForeignKey, Model
# from django.contrib.gis.db.models import PointField
# from django.contrib.gis.geos import Point


class City(Model):
    name = CharField(max_length=58)
    # TODO: implement GIS support
    # location = PointField(geography=True, default=Point(43.700278, 15.489444))
    longitude = DecimalField(max_digits=22, decimal_places=16, default=43.700278)
    latitude = DecimalField(max_digits=22, decimal_places=16, default=15.489444)
    country = ForeignKey('core.Country', CASCADE, related_name='cities')
