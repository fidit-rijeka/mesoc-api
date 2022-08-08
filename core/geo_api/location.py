import decimal


class Location:
    def __init__(self, id_, address):
        self.id_ = id_
        self.address = address

    def __str__(self):
        return self.address

    def __eq__(self, other):
        return self.id_ == other.id_


class GeocodedLocation(Location):
    def __init__(self, id_, address, latitude, longitude):
        super().__init__(id_, address)

        self.latitude = decimal.Decimal(latitude)
        self.longitude = decimal.Decimal(longitude)
