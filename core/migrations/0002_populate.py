from django.contrib import auth
from django.db import migrations
from django.db.models import signals

from ..signals import send_verification_email

LANGUAGES = (
    {
        'code': 'bg',
        'name': 'Bulgarian'
    },
    {
        'code': 'hr',
        'name': 'Croatian'
    },
    {
        'code': 'cs',
        'name': 'Czech'
    },
    {
        'code': 'da',
        'name': 'Danish'
    },
    {
        'code': 'nl',
        'name': 'Dutch'
    },
    {
        'code': 'en',
        'name': 'English'
    },
    {
        'code': 'ek',
        'name': 'Estonian'
    },
    {
        'code': 'fi',
        'name': 'Finish'
     },
    {
        'code': 'fr',
        'name': 'French'
    },
    {
        'code': 'de',
        'name': 'German'
    },
    {
        'code': 'el',
        'name': 'Greek'
    },
    {
        'code': 'hu',
        'name': 'Hungarian'
    },
    {
        'code': 'ga',
        'name': 'Irish'
    },
    {
        'code': 'it',
        'name': 'Italian'
    },
    {
        'code': 'lv',
        'name': 'Latvian'
    },
    {
        'code': 'lt',
        'name': 'Lithuanian'
    },
    {
        'code': 'mt',
        'name': 'Maltese'
    },
    {
        'code': 'pl',
        'name': 'Polish'
    },
    {
        'code': 'pt',
        'name': 'Portuguese'
    },
    {
        'code': 'ro',
        'name': 'Romanian'
    },
    {
        'code': 'sk',
        'name': 'Slovak'
    },
    {
        'code': 'sl',
        'name': 'Slovenian'
    },
    {
        'code': 'es',
        'name': 'Spanish'
    },
    {
        'code': 'sv',
        'name': 'Swedish'
    }
)

COUNTRIES = (
    {
        'name': 'Unknown',
    },
    {
        'name': 'Germany',
    },
    {
        'name': 'Croatia',
    },
    {
        'name': 'United Kingdom of Great Britain and Ireland'
    },
    {
        'name': 'France'
    }
)

CITIES = (
    {
        'name': 'Berlin',
        'latitude': 52.520008,
        'longitude': 13.404954,
        'country': COUNTRIES[1],
    },
    {
        'name': 'London',
        'latitude': 51.509865,
        'longitude': -0.118092,
        'country': COUNTRIES[3],
    },
    {
        'name': 'Paris',
        'latitude': 48.856613,
        'longitude': 2.352222,
        'country': COUNTRIES[1],
    },
    {
        'name': 'Rijeka',
        'latitude': 45.34306,
        'longitude': 14.40917,
        'country': COUNTRIES[2],
    },
    {
        'name': 'Unknown',
        'latitude': 15.489444,
        'longitude': 43.700278,
        'country': COUNTRIES[0],
    }
)


USERS = (
    {
        'email': 'dev@mesoc.dev',
        'password': 'devtest123',
        'verified': True
    },
    {
        'email': 'mulder@mesoc.dev',
        'password': 'devtest123',
        'verified': True
    },
    {
        'email': 'scully@mesoc.dev',
        'password': 'devtest123',
        'verified': True
    },
)


def populate_languages(apps, schema_editora):
    Language = apps.get_model('core', 'Language')
    Language.objects.all().delete()
    for language in LANGUAGES:
        Language.objects.create(**language)


def populate_countries(apps, schema_editor):
    Country = apps.get_model('core', 'Country')
    Country.objects.all().delete()
    for country in COUNTRIES:
        Country.objects.create(**country)


def populate_cities(apps, schema_editor):
    City = apps.get_model('core', 'City')
    Country = apps.get_model('core', 'Country')
    City.objects.all().delete()
    for city in CITIES:
        country = Country.objects.get(**city.pop('country'))
        City.objects.create(**city, country=country)


def populate_users(apps, schema_editor):
    # Verification = apps.get_model('core', 'Verification')
    from ..models import Verification
    signals.post_save.disconnect(send_verification_email, Verification)

    User = auth.get_user_model()
    User.objects.all().delete()
    for user in USERS:
        u = User(**user)
        u.set_password(user['password'])
        u.save()
        u.verification.delete()

    signals.post_save.connect(send_verification_email, Verification)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_languages),
        migrations.RunPython(populate_countries),
        migrations.RunPython(populate_cities),
        migrations.RunPython(populate_users),
    ]
