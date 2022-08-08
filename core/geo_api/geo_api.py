import abc
import logging

import django.utils.crypto
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
        self._filter = {
            'country', 'locality', 'administrative_area_level_1',
            'administrative_area_level_2', 'administrative_area_level_3'
        }

        self._session = django.utils.crypto.get_random_string(64)

    def search(self, address):
        locations = self._search_places(address)

        locs = []
        for location in locations:
            try:
                place = self._client.place(location['place_id'], session_token=self._session)['result']
                locs.append(self._create_location(place))
            except (googlemaps.exceptions.TransportError,
                    googlemaps.exceptions.ApiError,
                    googlemaps.exceptions.Timeout) as e:
                logger.error('An error occurred during Google Places call: %s.', e)

        return locs

    def search_autocomplete(self, address):
        locations = self._search_places(address)
        locations = [
            core.geo_api.location.Location(location['place_id'], location['description']) for location in locations
        ]

        return locations

    def search_place_id(self, id_):
        try:
            loc = self._client.place(id_, session_token=self._session)['result']
        except (googlemaps.exceptions.TransportError,
                googlemaps.exceptions.ApiError,
                googlemaps.exceptions.Timeout) as e:
            loc = None
            logger.error('An error occurred during Google Places call: %s.', e)

        return self._create_location(loc) if loc is not None else None

    def verify_place_id(self, id_):
        try:
            status = self._client.place(id_, session_token=self._session, fields=('place_id',))['status']
            if status == 'OK':
                verification = True
            else:
                if status == 'NOT FOUND':
                    logger.info('Place ID %s expired, needs refresh.', id_)
                else:
                    logger.warning('Google Places API call returned status %s.', status)

                verification = False
        except googlemaps.exceptions.ApiError:
            verification = False
        except (googlemaps.exceptions.TransportError, googlemaps.exceptions.Timeout) as e:
            verification = False
            logger.error('An error occurred during Google Places call: %s.', e)

        return verification

    def _search_places(self, address):
        try:
            locations = self._client.places_autocomplete(
                address, types='|'.join(self._filter),
                session_token=self._session
            )
            logger.debug('Found {} locations.'.format(len(locations)))
        except (googlemaps.exceptions.TransportError,
                googlemaps.exceptions.ApiError,
                googlemaps.exceptions.Timeout) as e:
            locations = []
            logger.error('An error occurred during Google Places call: %s.', e)

        return locations

    def _create_location(self, location):
        id_ = location['place_id']
        formatted_address = location['formatted_address']
        latitude = location['geometry']['location']['lat']
        longitude = location['geometry']['location']['lng']

        return core.geo_api.location.GeocodedLocation(id_, formatted_address, latitude, longitude)
