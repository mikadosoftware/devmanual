'''
I am just creating simple geometric art, for book illustrations.
I could just type something into CHatGPT but that kind of spoils it.

There is a Craig Kaplan paper, https://archive.bridgesmathart.org/2000/bridges2000-105.pdf
that describes creating simple Islamic inspired artwork.

lines
- divide the screen into cells, and in each cell draw a line from bottom 
- Recaman sequence

'''

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon
from matplotlib.tri import Triangulation


import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def draw_semicircle(x1, y1, x2, y2, color='black', lw=1, ax=None):
    '''
    draw a semicircle between the points x1,y1 and x2,y2
    the semicircle is drawn to the left of the segment
    '''
    ax = ax or plt.gca()
    # ax. Scatter([x1, x2], [y1, y2], s=100, c=color)
    startangle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
    diameter = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # Euclidian distance
    ax.add_patch(Arc(((x1 + x2) / 2, (y1 + y2) / 2), diameter, diameter, theta1=startangle, theta2=startangle + 180,
                     edgecolor=color, facecolor='none', lw=lw, zorder=0))

    
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))


def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'In triangle {tri}')
    event.canvas.draw()

def foo():
    # Create a Triangulation.
    n_angles = 16
    n_radii = 5
    min_radius = 0.25
    radii = np.linspace(min_radius, 0.95, n_radii)
    angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi / n_angles
    x = (radii*np.cos(angles)).flatten()
    y = (radii*np.sin(angles)).flatten()
    triang = Triangulation(x, y)
    triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                             y[triang.triangles].mean(axis=1))
                    < min_radius)

    # Use the triangulation's default TriFinder object.
    trifinder = triang.get_trifinder()

    # Setup plot and callbacks.
    fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
    ax.triplot(triang, 'bo-')
    polygon = Polygon([[0, 0], [0, 0]], facecolor='y')  # dummy data for (xs, ys)
    update_polygon(-1)
    ax.add_patch(polygon)
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
    plt.show()

def foo2():
    fig, ax = plt.subplots()
    y1 = 5
    y2 = 5
    x1 = 1
    x2 = 10
    draw_semicircle(x1, y1, x2, y2, color='black', lw=1, ax=ax)
    def func(x):
        #return (x - x^^2) * (x - 5) * (x - 7) + 85
        return x**2 + x**3

    x = np.linspace(0, 10)
    y = func(x)
    ax.plot(x, y, 'r', linewidth=2)
    ax.set_ylim(bottom=0)
    plt.show()

if __name__ == '__main__':
    seq = generate_recaman()
    print(seq)
    foo2()
