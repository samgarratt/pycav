#here begins bokehplotting.py
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

x = [0.1*i for i in range(10)]
y1 = [i/(i+1) for i in x]
y2 = [i/(i+2) for i in x]
y3 = [i/(i+3) for i in x]

output_notebook()

#create a figure object
p = figure(x_range = [0,1.0], tools = "pan, box_zoom, reset, save", title = "scale dependence")

#plot some graphs
p.grid
p.line(x, y1, legend = "y=x/(x+1)", line_color = "red")
p.circle(x, y1, fill_color = "white", size = 8)
p.line(x, y2, legend = "y=x/(x+2)", line_color = "blue")
p.circle(x, y2, fill_color = "white", size = 8)
p.line(x, y3, legend = "y=x/(x+3)", line_color = "green")
p.circle(x, y3, fill_color = "white", size = 8)
show(p)
