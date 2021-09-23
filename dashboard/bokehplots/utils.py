from bokeh.plotting import figure
from bokeh.models import LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import viridis

def create_bar_figure():
    p = figure()
    p.circle([1,2], [3,4])
    return p

def create_map_figure(source, args):
    """
    """
    p = figure(
        title = args["title"], 
        tools = args["tools"],
        toolbar_location = "above",
    )

    hover = HoverTool(tooltips=args["tooltips"])
    p.add_tools(hover)

    p.multi_line('x', 'y', source=source, color="black", line_width=2)
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    color_mapper = LinearColorMapper(
        palette = viridis(10), 
        low = args["low"], 
        high = args["high"], 
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
        source = source, 
        fill_color = {"field": args["field"], "transform" : color_mapper}, 
        line_color = "black", 
        line_width = 0.25, 
        fill_alpha = 1
    )
    
    return p