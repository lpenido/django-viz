from django.urls import path

from .views import home, bar_plot, network_plot, multi_plot, record_api, debug

urlpatterns = [
    path("", home, name='home'),
    path("api", record_api, name='api'),
    path("debug", debug, name='debug'),

    path("bar", bar_plot, name='d3bar'),
    path("network", network_plot, name='d3network'),
    path("multi", multi_plot, name='d3multi'),
]