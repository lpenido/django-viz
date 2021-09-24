from django.http import JsonResponse
from django.shortcuts import render

from .models import Record, ScavengerPin
from .utils import load_data

import json

# Create your views here.

def home(request):
    
    if ScavengerPin.objects.filter(id=1).first() == None:
        load_data()
    
    return render(request, "home.html", context={})

def bar_plot(request):
    return render(request, "d3/barplot.html")

def network_plot(request):
    return render(request, "d3/network.html")

def multi_plot(request):
    return render(request, "d3/multi_plot.html")

def record_api(request):
    data = Record.objects.all()
    api_list = [d.to_dict() for d in data]
    return JsonResponse(list(api_list), safe=False)

def debug(request):
    return render(request, "debug.html")