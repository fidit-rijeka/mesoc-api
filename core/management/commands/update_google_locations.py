import datetime

from django.conf import settings
from django.core.management import BaseCommand

from core.models import Location
from core.geo_api.geo_api import GooglePlacesAPI


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('days', help='Update locations older than specified number of days.', type=int)

    def handle(self, *args, **options):
        diff = datetime.date.today() - datetime.timedelta(days=int(options['days']))
        locations = Location.objects.exclude(location_id='unknown').filter(updated_at__lte=diff)

        api = GooglePlacesAPI(settings.CORE_GOOGLE_GEO_API_KEY)

        count = 0
        for loc in locations:
            if not api.verify_place_id(loc.location_id):
                new_loc = api.search(loc.address)

                if len(new_loc) == 1:
                    loc.location_id = new_loc[0].id_
                    loc.save()
                    count += 1
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            'Multiple locations returned for address {}, requires manual update of location id.'.format(
                                loc.address
                            )
                        )
                    )
            else:
                count += 1
                loc.save()

        self.stdout.write(self.style.SUCCESS('Successfully updated {} location identifiers.'.format(count)))

        failed = len(locations) - count
        if failed > 0:
            self.stdout.write(self.style.WARNING('Failed to updated {} location identifiers.'.format(failed)))
