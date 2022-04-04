import abc
import logging

import googlemaps

import core.geo_api.location

logger = logging.getLogger(__name__)


class BaseGeoAPI(abc.ABC):
    @abc.abstractmethod
    def search(self, address):
        raise NotImplementedError


class GooglePlacesAPI(BaseGeoAPI):
    def __init__(self, api_key):
        self._client = googlemaps.Client(api_key)
        self._filter = {'country', 'locality', 'administrative_area_level_3'}

    def search(self, address):
        locations = self._search_places(address)
        locations = self._filter_places(locations)

        return [self._create_location(location) for location in locations] if locations else []

    def _search_places(self, address):
        try:
            locations = self._client.places(address)['results']
        except (googlemaps.exceptions.TransportError, googlemaps.exceptions.ApiError) as e:
            logger.error(e)

        logger.debug('Found {} locations.'.format(len(locations)))
        return locations

    def _filter_places(self, locations):
        places = []
        for location in locations:
            types = set(location['types'])
            if len(types & self._filter) > 0:
                places.append(location)

        return places

    def _create_location(self, location):
        id_ = location['place_id']

        formatted_address = location['formatted_address'].split()
        if len(formatted_address) > 0:
            city = formatted_address[-2]
            country = formatted_address[-1]
        else:
            city = ''
            country = formatted_address[0]

        latitude = location['geometry']['location']['lat']
        longitude = location['geometry']['location']['lng']

        return core.geo_api.location.Location(id_, city, country, latitude, longitude)
