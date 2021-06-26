# Generated by Django 3.2.4 on 2021-06-26 02:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centres', '0002_auto_20210605_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street_address', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(blank=True, max_length=10, null=True)),
                ('fee', models.FloatField(default=0.0)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'Test Centres',
            },
        ),
    ]