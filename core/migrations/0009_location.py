# Generated by Django 3.1.3 on 2021-10-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210928_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('longitude', models.DecimalField(decimal_places=16, default=43.700278, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, default=15.489444, max_digits=22)),
            ],
        ),
    ]
