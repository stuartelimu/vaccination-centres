from django.urls import path

from . import views

app_name = 'sites'

urlpatterns = [
    path('map/', views.SiteMapView.as_view()),
]