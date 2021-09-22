from bokeh.plotting import figure
from bokeh.models import LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import viridis

def chicago_map(geosource, low, high):
    
    TOOLS = "help,box_select,tap"
    p = figure(title="Chicago Community Areas", toolbar_location=None, tools=TOOLS)
    hover = HoverTool(tooltips = [
        ("Community Area","@community"),
        ("Random Number", "@rand")
    ])
    p.add_tools(hover)

    p.multi_line('x', 'y', source=geosource, color="black", line_width=2)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    color_mapper = LinearColorMapper(
        palette = viridis(10), 
        low = low, 
        high = high, 
    )

    color_bar = ColorBar(
        color_mapper = color_mapper, 
        width = 20, 
        height = 300,
        border_line_color = None,
        location = (0,0), 
        orientation = "vertical",
        label_standoff=12
    )
    p.add_layout(color_bar, "right")

    p.patches(
        "xs","ys", 
        source = geosource, 
        fill_color = {"field": "rand", "transform" : color_mapper}, 
        line_color = "black", 
        line_width = 0.25, 
        fill_alpha = 1
    )
    
    return p