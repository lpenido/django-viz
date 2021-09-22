from django.urls import path

from .views import home, bar_plot, network_plot, multi_plot, record_api

urlpatterns = [
    path("", home, name='home'),
    path("bar", bar_plot, name='barplot'),
    path("network", network_plot, name='networkplot'),
    path("multi", multi_plot, name='multi'),
    
    path("api", record_api, name='api'),
]