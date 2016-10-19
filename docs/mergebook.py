"""
This is a simple script to take an original text `fulllist.rst`
which holds many ``{{links}}``.  The links reference other rst files
in the directory, and we replace/merge the text from those files into the 
{{link}} and hey presto a chapter based book

"""
import re
import os

#: constants
TGTFILENAME = 'index.rst'
SRCFILENAME = 'fulllist.rst'
CHAPTERDIR  = 'chapters'

def matchline(line):
   """
   >>> matchline("{{teet}}")
   'teet'
   >>> matchline("teet")


   """
   rg = re.compile("{{(\S*)}}")
   m = rg.match(line.strip())
   if m:
       return m.group(1)
   else:
      return

def getTextFromFile(filename):
   """
   """
   filepath = os.path.join(CHAPTERDIR, filename)
   txt = open(filepath).read()
   return txt

def mergebook(bookpath):
    txtnew = ''
    txt = open(bookpath).read()
    
    for line in txt.split('\n'):
        
        m = matchline(line)
        if m:
           txtnew += "\n" + getTextFromFile(m) + "\n"
        else:
           txtnew += line + '\n'
           
           
    open(TGTFILENAME,'w').write( txtnew)
    
    
if __name__ == '__main__':
#   import doctest
#   doctest.testmod()
    mergebook(SRCFILENAME)
