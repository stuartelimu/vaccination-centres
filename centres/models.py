from django.contrib.gis.db.models import PointField
from django.db import models


class Centre(models.Model):
    '''A centre with a name, district and location'''
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    location = PointField()


class TestCentre(models.Model):
    '''A test centre with a name, district, street address, contact, fee and location'''
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    fee = models.FloatField(default=0.0)
    district = models.CharField(max_length=255, null=True, blank=True)
    location = PointField()

    class Meta:
        verbose_name = 'Test Centres'
