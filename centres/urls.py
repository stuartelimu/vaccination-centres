from os import name
from django.urls import path

from . import views

app_name = 'centres'

urlpatterns = [
    path('map/', views.CentreMapView.as_view(), name='map'),
]