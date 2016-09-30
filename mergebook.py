
import re

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
   txt = open(filename).read()
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
           
           
    open("newbook.rst",'w').write( txtnew)
    
    


if __name__ == '__main__':
#   import doctest
#   doctest.testmod()
    mergebook('fulllist.rst')
