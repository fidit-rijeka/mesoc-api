# Generated by Django 3.1.3 on 2022-08-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20220513_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
