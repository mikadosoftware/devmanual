"""
I am doing a lot of changes to larg numebr of file

TODO: see the diffs I jsut made

"""
import os
import shutil
from pprint import pprint as pp

ROOTPATH='/home/pbrian/projects/devmanual/docs'
BACKUPLOCATION="/tmp/chaptertools/"

def mkdir_backup():
    try:
        os.makedirs(BACKUPLOCATION)
    except OSError:
        pass #ignore we want to recreate idempotent


def update_a_file(filepath, fn):
    """Grab the text in filepath, pass text to `fn` and write the result back to filepath
    """
    #: check exists
    if not os.path.isfile(filepath):
        raise Exception("File not found at {0}".format(filepath))
    #: backup file
    shutil.copyfile(filepath, os.path.join(BACKUPLOCATION, os.path.basename(filepath)))
    #: get text
    txt = open(filepath).read()
    try:
        newtxt = fn.__call__(txt)
    except Exception, e:
        print e

    fo = open(filepath, 'w')
    fo.write(newtxt)
    fo.close()

def walk_apply(fn):
    files_to_use = []
    notin = ['.git', '_build']
    for dirpath, dirnames, filenames in os.walk(ROOTPATH):
        for notintoken in notin:
            for dirname in dirnames:
                if dirname.find(notintoken) >= 0:
                    #get rid
                    dirnames.remove(dirname)

        for file in filenames:
            if file.endswith(".rst"):
                files_to_use.append(os.path.join(dirpath, file))
    for filepath in files_to_use:
        update_a_file(filepath, fn)

def clear_tokens(text):
    """
    >>> clear_tokens(':main fskjdkfjsdlkkfjsdlfj')
    ':main fskjdkfjsdlkkfjsdlfj'
    >>> clear_tokens(':mind fskjdkfjsdlkkfjsdlfj')
    ' fskjdkfjsdlkkfjsdlfj'
    """
    tokens = [':mind',]
    for token in tokens:
        if text[:len(token)] == token:
            text = text[len(token):]
    return text

def run():
    mkdir_backup()
    #update_a_file('/home/pbrian/projects/devmanual/docs/conf.py', None)
    walk_apply(clear_tokens)

def test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    run()
