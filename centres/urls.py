from os import name
from django.urls import path

from . import views

app_name = 'centres'

urlpatterns = [
    path('', views.CentreMapView.as_view(), name='map'),
    path('ajax/filter/', views.filter_view, name='filter'),
    path('ajax/centres/test/', views.test_centre_list_view, name='test_centre_list'),
]