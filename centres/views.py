import json
from django.core import serializers

from django.core.serializers import serialize
from django.views.generic.base import TemplateView
from django.contrib.gis.geos import Polygon
from django.http import JsonResponse

from .models import Centre, TestCentre


class CentreMapView(TemplateView):

    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['centres'] = json.loads(serialize("geojson", Centre.objects.all()))
        context['centers'] = Centre.objects.all()
        return context


def filter_view(request):
    if request.is_ajax and request.method == 'GET':
        # get value from client side
        district = request.GET.get('district', None)
        # return centres in that district
        centres = Centre.objects.filter(district=district)
        data = json.loads(serialize("geojson", centres))
        return JsonResponse({"data": data})

def test_centre_list_view(request):
    if request.is_ajax and request.method == 'GET':
        # check the section i.e test
        section = request.GET.get('section', None)
        if section == 'test':
            # return test centres
            centres = json.loads(serialize("geojson", TestCentre.objects.all()))
            return JsonResponse({"data": centres})
    return JsonResponse({}, status = 400)

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     ne = (0.3737, 32.6509)
#     sw = (0.2480, 32.4363)
#     bbox = (sw[1], sw[0], ne[1], ne[0])

#     geom = Polygon.from_bbox(bbox)

#     context['centres'] = json.loads(serialize("geojson", Centre.objects.filter(location__contained=geom)))
#     context['centers'] = Centre.objects.filter(location__contained=geom)
#     return context