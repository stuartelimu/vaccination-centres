import json

from django.core.serializers import serialize
from django.views.generic.base import TemplateView

from .models import Centre


class CentreMapView(TemplateView):

    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['centres'] = json.loads(serialize("geojson", Centre.objects.all()))
        return context