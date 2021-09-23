from django.urls import path

from .views import barplot, mapplot

urlpatterns = [
    path("bbar", barplot, name='bbar'),
    path("bmap", mapplot, name='bmap'),
]