# Generated by Django 3.2.7 on 2021-09-29 09:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0002_uploadfolder_synth_index_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfolder',
            name='synth_index_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
