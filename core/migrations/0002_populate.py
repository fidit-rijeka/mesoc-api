from django.db import migrations

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


def populate_languages(apps, schema_editor):
    Language = apps.get_model('core', 'Language')
    Language.objects.all().delete()
    for language in LANGUAGES:
        Language.objects.create(**language)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_languages)
    ]
