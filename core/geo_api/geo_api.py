import abc
import logging
import re

import geopy.exc
import geopy.geocoders

import core.geo_api.location

logger = logging.getLogger(__name__)


class BaseGeoAPI(abc.ABC):
    @abc.abstractmethod
    def search(self, address):
        raise NotImplementedError


class GoogleGeoAPI(BaseGeoAPI):
    def __init__(self, api_key):
        self._api = geopy.geocoders.GoogleV3(api_key=api_key)

    def search(self, address):
        locations = self._geocode_address(address)
        filtered_locations = self._filter_political(locations)
        extracted = self._extract_names(filtered_locations)

        return extracted

    def _geocode_address(self, address):
        try:
            response = self._api.geocode(address, exactly_one=False)
        except geopy.exc.GeocoderQueryError as e:
            response = None
            logger.error(e, exc_info=True)

        if response is not None:
            logger.info('Listing locations: {}.'.format(response))
            locations = response
        else:
            locations = []

        logger.debug('Found {} locations.'.format(len(locations)))

        return locations

    def _filter_political(self, locations):
        political_list = [
            x for x in locations if ('political' in x.raw['types'])  # or ('natural_feature' in x.raw['types'])
        ]
        return political_list

    def _extract_names(self, locations):
        extracted = []
        raw_list = [x.raw for x in locations]
        for loc in raw_list:
            address = loc['formatted_address']
            address = ''.join([i for i in address if not i.isdigit()])
            location = loc['geometry']
            latitude = location['location']['lat']
            longitude = location['location']['lng']

            address = re.split(r',| - ', address)
            address = [x.strip() for x in address]
            address = [a for a in address if a]

            if len(address) == 1:
                city = None
                country = address[0]
            else:
                city = address[0]
                country = address[-1]

            entry = core.geo_api.location.Location(city if city else '', country, latitude, longitude)
            extracted.append(entry)

        return extracted
