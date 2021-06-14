from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from . import views


class TestCentreUrls(SimpleTestCase):

    def test_centre_map_view_url_resolves_correct_view(self):
        url = reverse('centres:map')
        self.assertEquals(resolve(url).func.view_class, views.CentreMapView)

