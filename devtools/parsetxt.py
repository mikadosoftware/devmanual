'''
parse a text file into chunks basaed on underscore
'''

import re

def parse_txt(txt):
    '''
    >>> txt="\\ntest\\n====\\nPara1\\n\\ntest2\\n=====\\nPara2\\nPara3"
    >>> parse_txt(txt)

    '''

    res = {}
    pattern = '(\n.*?\n=+\n)'

    rgx = re.compile(pattern) # anytxt, then newline,then ==== then non greedy all
    lst = rgx.split(txt)
    lst = [l for l in lst if l.strip() != '']

    for i in range(0, len(lst), 2):
        hdr = lst[i]
        body = lst[i+1]
        title = hdr.strip().replace("/","").replace("\n", "").replace("=","").replace(" ","_").lower()
        print "chapters/%s"%title

        fo = open("/tmp/foo/%s.rst" % title, 'w')
        fo.write(hdr+"\n"+body)
        fo.close()







def reals():
    txt = open('docs/index.rst').read()
    parse_txt(txt)

def runtests():
#    import doctest
#    doctest.testmod()
    txt="""
test
====
Para1

dfdsjflkds
kjdsf
test2
=====
Para2

Para3
"""
    parse_txt(txt)

if __name__ == '__main__':
    reals()
    #runtests()
