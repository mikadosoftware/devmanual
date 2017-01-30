
import os
from pprint import pprint as pp

def movefiles():
    """
    """
    d = {}
    rootdir = '/home/pbrian/projects/devmanual/docs/chapters/manual'
    for file in os.listdir(rootdir):
        fo = open(os.path.join(rootdir, file))
        line = fo.readline()
        if line[0] == ":":
            filedest = line[1:].strip().lower()
            d.setdefault(filedest, []).append(file)
    pp(d)
    print d.keys()

if __name__ == '__main__':
    movefiles()
