
import os
import shutil
from pprint import pprint as pp

BACKUPLOCATION="/tmp/resttools/"

def update_a_file(filepath, fn):
    """Grab the text in filepath, pass text to `fn` and write the result back to filepath
    """
    #: check exists
    if not os.path.isfile(filepath):
        raise Exception("File not found at {0}".format(filepath))
    #: backup file
    shutil.copy_file(filepath, os.path.join(BACKUPLOCATION, os.path.basename(filepath)))



if __name__ == '__main__':
    update_a_file('/home/pbrian/projects/devmanual/docs/conf.py', None)
