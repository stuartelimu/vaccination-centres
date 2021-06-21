from django.contrib.gis.db.models import PointField
from django.db import models


class Centre(models.Model):
    '''A centre with a name, district and location'''
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    location = PointField()


class TestCentre(models.Model):
    '''A test centre with a name, street address, contact, fee and location'''
    name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    fee = models.FloatField(default=0.0)
    location = PointField()

    class Meta:
        verbose_name = 'Test Centres'
