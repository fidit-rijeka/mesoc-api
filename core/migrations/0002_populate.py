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
        migrations.RunPython(populate_users),
    ]
