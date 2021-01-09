from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('places/<int:place_id>/', get_place, name='place'),
]