=============================
Useful command line utilities
=============================

learn the command line
======================
::
  # echo day | sed s/day/night/
  night
  # echo daylight | sed s/day/night/
  nightlight

Oh yeah baby. Power.

Let me show you how Linus [#]_ did a simple check of his bash history

::
    history
            | grep git
            | sed 's/[ 0-9]*(git[ ]*[a-z-]*).*/1/'
            | sort
            | uniq -c
            | sort -n

so lets go through that and see what is worth learning

::

 #!/bin/ksh

 mystring="01.Driver Report|userid@company.com"
 echo "$mystring"|while IFS="|" read f1 f2
 do
 name="$f1"
 email="$f2"
 done
 echo "$name"
 echo "$email"


bibliography
------------

http://www.grymoire.com/Unix/Sed.html#uh-0


.. [#] http://www.linux-mag.com/cache/7314/1.html
