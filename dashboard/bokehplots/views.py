from django.shortcuts import render

from .models import Record
from .utils import create_map_figure, create_bar_figure

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

    p = create_bar_figure()

    script, div = components(p)

    context = {
        "names": json.dumps(names),
        "counts": json.dumps(counts),
        "div": div, 
        "script": script,
    }

    return render(request, "bokehplots/barplot.html", context=context)


def mapplot(request):
    """
    """
    # Load up the polygon
    polygons = os.getenv("COM_AREAS")
    chicago = gpd.read_file(polygons)

    # Some random data to make the map pretty
    chicago["rand"] = pd.Series(np.random.randint(0,100, size=len(chicago)))
    low, high = chicago["rand"].min(), chicago["rand"].max()
    
    # Read data to json and convert to string for Bokeh
    chicago_json = json.loads(chicago.to_json())
    json_data = json.dumps(chicago_json)
    geosource = GeoJSONDataSource(geojson = json_data)

    # Config the plot
    args = {
        "title": "Chicago Community Areas",
        "tooltips": [
            ("Community Area","@community"),
            ("Random Number", "@rand")
        ],
        "low": low,
        "high": high,
        "field": "rand",
        "tools": "help,box_select,tap"
    }

    # Make sure the same source to enable linking 
    w = create_map_figure(geosource, args)

    script, div = components(w)

    context = {
        "div": div, 
        "script": script,
    }
    return render(request, "bokehplots/map.html", context=context)