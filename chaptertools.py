"""
THis is a grep / find / awk replacement.
I just want to be more careful than a few lines of awk when changing
all the files, and maybe all I need to do is awk.

I could use subprocess and awk.
And I could do it and just show me the likely outcomes. seems a nice compromise
"""
import os
import shutil
from pprint import pprint as pp

ROOTPATH='/home/pbrian/projects/devmanual/docs'
BACKUPLOCATION="/tmp/chaptertools/"

def build_one_pager():
    """Build a single page (does pdf???) """
    

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

def run():
    """We want to backup our files (incase) and apply a fn to each file
    """
    mkdir_backup()
    walk_apply(mktitle)

def test():
    import doctest
    doctest.testmod()

############################ text altering functions to call
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

def rmblankline(txt):
    firstline = txt.split("\n")[0]
    if firstline.strip() == '':
        newtxt = '\n'.join(txt.split("\n")[1:])
    else:
        newtxt = txt
    return newtxt

def mktitle(txt):
    newtxt = ''
    firstline = txt.split("\n")[0]
    if firstline.find("===") == 0:
        newtxt = txt
    else:
        newtxt = "="*len(firstline) + '\n'
        newtxt += firstline + '\n'
        newtxt += '='*len(firstline) + '\n'
        newtxt += txt[len(firstline):]
    return newtxt


def mk_review_html():
    """pront the rst as HTML for mass print out and review
    """
    tgtfilepath = '/home/pbrian/projects/devmanual/all.txt'
    html = ''
    toc = ''
    rootpath = '/home/pbrian/projects/devmanual/docs/chapters'
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            if filename.find(".rst") == -1:
                continue
            html += "\n                 ##### %s ####\n" % filename
            txt = open(os.path.join(root, filename)).read()
            #txt = txt.replace("\n","<br/>")
            html += txt
            toc += "- %s\n" % filename
    htmlout = "%s\n#######\n %s" % (toc, html)
    fo = open(tgtfilepath, 'w')
    fo.write(htmlout)
    fo.close()
    import webbrowser;webbrowser.open(tgtfilepath)


############################ end


if __name__ == '__main__':
    #run()
    mk_review_html()
