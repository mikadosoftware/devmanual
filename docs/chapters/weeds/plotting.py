from bokeh.plotting import figure, output_file, show
import numpy as np

# prepare some data
# We get an evenly spaced array of 100 values between pi and -pi
arrx = np.linspace(np.pi, -np.pi, 100)
# and the y axis is the sin of each degree
arry = [np.sin(x) for x in arrx]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(arrx, arry, legend="Sine", line_width=2)

# show the results
show(p)
