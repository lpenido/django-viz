from django.shortcuts import render

from .models import Record
from .utils import chicago_map

import pandas as pd
import geopandas as gpd
import numpy as np

from bokeh.embed import components
from bokeh.models import GeoJSONDataSource
from bokeh.layouts import gridplot

import os
import json

# Create your views here.
def barplot(request):
    data = Record.objects.all()
    api_list = [d.to_dict() for d in data]
    names = [d.name for d in data]
    counts = [d.count for d in data]

    plot = figure()
    plot.circle([1,2], [3,4])

    script, div = components(plot)

    context = {
        "names": json.dumps(names),
        "counts": json.dumps(counts),
        "div": div, 
        "script": script,
    }

    return render(request, "bokehplots/barplot.html", context=context)


def mapplot(request):
    
    com_areas = os.getenv("COM_AREAS")

    chicago = gpd.read_file(com_areas)
    chicago["rand"] = pd.Series(np.random.randint(0,100,size=77))
    low, high = chicago["rand"].min(), chicago["rand"].max()
    
    # Read data to json and convert to string for Bokeh
    chicago_json = json.loads(chicago.to_json())
    json_data = json.dumps(chicago_json)
    geosource = GeoJSONDataSource(geojson = json_data)

    # Make sure the same source to enable linking 
    p = chicago_map(geosource, low, high)
    q = chicago_map(geosource, low, high)

    # Side by sides 
    w = gridplot([[p, q]])
    script, div = components(w)

    context = {
        "div": div, 
        "script": script,
    }
    return render(request, "bokehplots/map.html", context=context)