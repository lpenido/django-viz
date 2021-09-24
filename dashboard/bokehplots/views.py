from django.shortcuts import render
from django.db.models import Count

from d3.models import Record, ScavengerPin
from .utils import create_map_figure, create_bar_figure

import pandas as pd
import geopandas as gpd
import numpy as np

from bokeh.embed import components
from bokeh.models import ColumnDataSource, GeoJSONDataSource
from bokeh.layouts import gridplot

import os
import json

# Create your views here.
def barplot(request):
    """
    """
    # Load up data
    result = ScavengerPin.objects.values('classification').annotate(dcount=Count('pin')).order_by()
    data = {
        "classification": [str(x["classification"]) for x in result],
        "dcount": [x["dcount"] for x in result]
    }

    source = ColumnDataSource(data=data)

    # Config the plot
    args = {
        "x_labs": "classification",# set(data["classification"]),
        "top": "dcount", # data["dcount"],
        "title": "Scavenger PINs by Classification",
        "tooltips": [
            ("Classification","@classification"),
            ("PINs", "@dcount")
        ],
        "tools": "help,box_select,tap"
    }

    p = create_bar_figure(source, args)

    script, div = components(p)

    context = {
        "div": div, 
        "script": script,
    }
    return render(request, "bokehplots/barplot.html", context=context)

def scatterplot(request):
    pass

def histogram(request):
    pass

def boxplot(request):
    pass

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

    # Make sure the same source if you want to enable linking
    # across multiple maps 
    w = create_map_figure(geosource, args)

    script, div = components(w)

    context = {
        "div": div, 
        "script": script,
    }
    return render(request, "bokehplots/map.html", context=context)