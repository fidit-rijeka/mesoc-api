# Generated by Django 3.1.3 on 2021-09-22 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210905_0408_squashed_0007_auto_20210905_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cell',
            name='variables',
        ),
        migrations.DeleteModel(
            name='CellVariable',
        ),
        migrations.DeleteModel(
            name='Variable',
        ),
    ]