# Generated by Django 3.1.3 on 2022-03-29 10:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20220318_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.0)])),
                ('cell', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(29)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='reclassified',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterUniqueTogether(
            name='cell',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='cell',
            constraint=models.UniqueConstraint(fields=('document', 'cell'), name='core_cell_unique_cell'),
        ),
        migrations.AddField(
            model_name='historicalcell',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_cells', to='core.document'),
        ),
        migrations.AddConstraint(
            model_name='historicalcell',
            constraint=models.UniqueConstraint(fields=('document', 'cell'), name='core_historicalcell_unique_cell'),
        ),
    ]