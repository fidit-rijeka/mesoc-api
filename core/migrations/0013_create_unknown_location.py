from django.db import migrations


def create_unknown_location(apps, schema_editor):
    Location = apps.get_model('core', 'Location')
    Location.objects.get_or_create(
        city='Unknown', country='Unknown', longitude=15.4894440000000000, latitude=43.7002780000000000
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_user_can_use_export_api')
    ]

    operations = [
        migrations.RunPython(create_unknown_location)
    ]
