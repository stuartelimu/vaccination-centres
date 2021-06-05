from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from .models import Centre


@admin.register(Centre)
class CentreAdmin(OSMGeoAdmin):
    '''Centre admin'''
    list_display = ('district', 'name', 'location')