# Generated by Django 3.1.3 on 2021-01-31 16:45

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('verified', models.BooleanField(blank=True, default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)])),
                ('num_keywords', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('order', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(29)])),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=58)),
                ('longitude', models.DecimalField(decimal_places=16, default=43.700278, max_digits=22)),
                ('latitude', models.DecimalField(decimal_places=16, default=15.489444, max_digits=22)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='documents/')),
                ('file_title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(1)])),
                ('document_title', models.CharField(blank=True, default='', max_length=200, validators=[django.core.validators.MinLengthValidator(1)])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(blank=True, choices=[(0, 'processing'), (1, 'failed'), (2, 'processed'), (3, 'dismissed')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=60, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2021, 2, 14, 16, 45, 36, 598539, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2021, 2, 14, 16, 45, 36, 598042, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='cities',
            field=models.ManyToManyField(related_name='cities', through='core.DocumentCity', to='core.City'),
        ),
        migrations.AddField(
            model_name='document',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.language'),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.country'),
        ),
        migrations.CreateModel(
            name='CellVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ontology_categories', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('num_keyword_vars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('strength', models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)])),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cell')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.variable')),
            ],
            options={
                'unique_together': {('cell', 'variable')},
            },
        ),
        migrations.AddField(
            model_name='cell',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='core.document'),
        ),
        migrations.AddField(
            model_name='cell',
            name='variables',
            field=models.ManyToManyField(through='core.CellVariable', to='core.Variable'),
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together={('file_title', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='cell',
            unique_together={('document', 'order')},
        ),
    ]
