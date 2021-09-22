from django.http import JsonResponse
from django.shortcuts import render

from .models import Record

import json

# Create your views here.

def home(request):
    data = Record.objects.all()
    api_list = [d.to_dict() for d in data]
    names = [d.name for d in data]
    counts = [d.count for d in data]

    context = {
        "names": json.dumps(names),
        "counts": json.dumps(counts)
    }

    return render(request, "home.html", context=context)

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