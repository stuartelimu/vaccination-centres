from django.views.generic.base import TemplateView


class SiteMapView(TemplateView):

    template_name = 'map.html'