import sys, os

if __name__ == '__main__':

    folder = sys.argv[1:][0]
    pkg = os.path.basename(folder)
    raw_input(pkg)
    files = os.listdir(folder)
    destfolder = "/tmp/%s" % os.path.basename(folder)
    try:
        os.mkdir(destfolder)
    except:
        pass
    
    for f in [i for i in files if os.path.splitext(i)[1] == ".py"]:
        filename,ext = os.path.splitext(f)
        fo = open(os.path.join(destfolder, "stub_" + filename + ".rst"),'w') 
        title = filename
        title_underline = "=" * len(title)
        fo.write("""
%s
%s
%s

.. automodule:: %s.%s
   :members:
""" % (title_underline, title, title_underline, pkg, filename))
        fo.close()

