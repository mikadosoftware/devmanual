'''
I am just creating simple geometric art, for book illustrations.
I could just type something into CHatGPT but that kind of spoils it.

There is a Craig Kaplan paper, https://archive.bridgesmathart.org/2000/bridges2000-105.pdf
that describes creating simple Islamic inspired artwork.

lines
- Recaman sequence

FIrstly this is learning to use matplotlib
recaman sequence



'''

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon
from matplotlib.tri import Triangulation
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np


def generate_recaman():
    '''Generate the recaman sequence (https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence)

    Start at 0, and always add 1.
    However the function then always tries to go back (to 1)
    but if that results in < 1 then go frowards (add)

    [ ] make a recursive version
    [ ] draw semicircles
    [ ] play music
    '''
    NUMS = []
    def recaman(currentnumber, nextstep):
        backwards = currentnumber - nextstep
        forwards = currentnumber + nextstep
        if  backwards > 1 and backwards not in NUMS:
            return backwards
        else:
            return forwards
    currentnumber = 0
    for step in range(0, 100):
        currentnumber = recaman(currentnumber, step)
        NUMS.append(currentnumber)
    return NUMS


def draw_semicircle(x1, y1, x2, y2, color='black', lw=1, ax=None):
    '''
    draw a semicircle between the points x1,y1 and x2,y2
    the semicircle is drawn to the left of the segment
    '''
    ax = ax or plt.gca()
    startangle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
    diameter = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  # pythagorean distance
    ax.add_patch(Arc(((x1 + x2) / 2, (y1 + y2) / 2), diameter,
                     diameter, theta1=startangle, theta2=startangle + 180,
                     edgecolor=color, facecolor='none', lw=lw, zorder=0))
    
def draw_line(ax, xs, ys):
    ax.plot(xs,ys)
    
def drawcanvas():
    fig, ax = plt.subplots()
    seq = generate_recaman()
    #for i in range(0, len(seq), 2):
    y = 5
    for i in range(len(seq)-1):
        x = seq[i]
        xx = seq[i+1]
        draw_semicircle(x, y, xx, y, color='black', lw=1, ax=ax)
    #draw_line(ax, [1,2],[1,2])
    print(ax.patches)
    #ax.set_xlim(-200,200)
    #ax.set_ylim(-200,200)
    #fig.tight_layout()
    #plt.show()
    #plt.imshow(aspect='auto')
    f = "/home/pbrian/image.png"
    # recompute the ax.dataLim
    ax.relim()
    # update ax.viewLim using the new dataLim
    ax.autoscale_view()
    plt.savefig(f,bbox_inches='tight',dpi=100)
    import webbrowser;webbrowser.open(f)
    
if __name__ == '__main__':
    drawcanvas()
