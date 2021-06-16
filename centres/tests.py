import json
from django.http import response
from django.test import TestCase, SimpleTestCase
from django.test.client import Client
from django.urls import reverse, resolve
from django.contrib.gis.geos import Point
from . import views
from .models import Centre


class TestCentreUrls(SimpleTestCase):

    def test_centre_map_view_url_resolves_correct_view(self):
        url = reverse('centres:map')
        self.assertEquals(resolve(url).func.view_class, views.CentreMapView)


class TestFilterView(TestCase):

    def setUp(self):
        self.test_centre = Centre.objects.create(
            name='Test',
            district='Test',
            location = Point(1,1)
        )
        self.client = Client()

    def test_url_resolves_correct_view(self):
        response = self.client.get(reverse('centres:filter'))
        url = reverse('centres:filter')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(resolve(url).func, views.filter_view)

    def test_view_returns_correct_queryset(self):
        data = {'district': 'Test'}
        response = self.client.get('/ajax/filter', data)
        self.assertEquals(response.status_code, 301)



