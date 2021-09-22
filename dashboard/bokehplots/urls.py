from django.urls import path

from .views import barplot, mapplot

urlpatterns = [
    path("bbar", barplot, name='bbarplot'),
    path("map", mapplot, name='mapplot'),
]