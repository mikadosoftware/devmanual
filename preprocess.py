#! -*- coding: utf-8 -*-

import docopt
import os

help = """Preprocess my book index files. Designed
solely to convert index.pre to index.rst. {{ <filename> }} will get repplaceed
with contenst of filename.

Usage:
  preprocess.py <index>

Options:
  -h --help Help



"""



def gettext(readfrom):
    """ 
    """
    print(readfrom)
    txt = open(readfrom, encoding='utf-8').read()
    print(len(txt))
    return txt

def run(args):
    indexfile = args['<index>']
    indexfilename = os.path.basename(os.path.abspath(indexfile))
    rootpath = os.path.dirname(os.path.abspath(indexfile))
    outfile = os.path.join(rootpath, indexfilename.replace(".pre",".rst"))
    outtext = ''
    with open(indexfile, encoding='utf-8') as indexfo:
        for line in indexfo:
            if line.strip().find("{{") == 0: #must be forst thing on a line
                readfrom = line.replace("{","").replace("}","").strip()
                readfrompath = os.path.join(rootpath, readfrom)
                val = gettext(readfrompath)
            else:
                val = line
            outtext += val
    fo = open(outfile, 'w', encoding='utf-8')
    fo.write(outtext)
    fo.close()
    

def main():
    args = docopt.docopt(help)
    run(args)

if __name__ == '__main__':
    main()
