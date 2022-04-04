import decimal


class Location:
    def __init__(self, id_, city, country, latitude, longitude):
        self.id_ = id_
        self.city = city
        self.country = country
        self.latitude = decimal.Decimal(latitude)
        self.longitude = decimal.Decimal(longitude)

    @property
    def address(self):
        return '{}, {}'.format(self.city, self.country) if self.city is not None else self.country

    def __str__(self):
        return self.address

    def __eq__(self, other):
        return self.id_ == other.id_
