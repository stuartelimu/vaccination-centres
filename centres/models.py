from django.contrib.gis.db.models import PointField
from django.db import models


class Centre(models.Model):
    '''A centre with a name, district and location'''
    name = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    location = PointField()
