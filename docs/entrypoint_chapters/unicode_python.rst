========
Unicode
========

Unicode is both amazing and complex and challenging.

You know the whole Python 2, Python 3 thing? Where sane and sensible core python
developers just threw their hands in the air and wrote a backwards incompatible
version of python (3).  Yeah. The main reason for doing that.  Unicode.

Its that hard.

But now, using Python 3 *only*, unicode become much more ... understandable.


So lets try some things. Firstly, i like to use `emacs` the editor, and it has
OK unicode support. So if i want to print the chinese yuan symbol (¥) I use the key combinations `C-x 8 Y` - that is Ctrl-x, digit 8 and uppercase Y.  The C-x 8 gets me into the unicode "entry system" and capital Y is a common shortcut.

I can enter any unicode via (#TODO: C-x 8 entry how to)

Ok, so lets just see if I can print to my terminal, a non ascii character

foo.py ::

  print("That will be 10 ¥ please.")

I run it from my terminal (`python foo.py`), and hey presto. total fail::

  [pbrian@bluemountain ~]$ python foo.py
  File "foo.py", line 1
  SyntaxError: Non-ASCII character '\xc2' in file foo.py on line 1, but no
  encoding declared; see http://python.org/dev/peps/pep-0263/ for details

This is Python telling me that I loaded up a file (foo.py) but when it tried to
parse the file it hit a problem.  There was no encoding set for the file, and
it defaulted to ASCII. SO it read some bytes and hey presto - there is a byte above 128

So we need to declare that the module will be utf-8 encoded

foo.py ::

  #! -*- coding:utf-8 -*- 
  print("That will be 10 ¥ please.")

Now thats better - we get a print out in our terminal

(Oh having a unicode aware terminal. Different problem but mostly solved these days)


  
Biblio
------
https://docs.python.org/2/library/unicodedata.html

Usernames as identify and tripartite identify patter

https://www.b-list.org/weblog/2018/feb/11/usernames/

Simple test - test everything with a set of unicode poems - maybe omar kayyam and j'taime 
everything should be able to display it - terminals to web browsers to logs and so on

my goal is a fixed group of micro services running on docker that talk to each other securely http://www.daemonology.net/blog/2009-09-28-securing-https.html

https://security.stackexchange.com/questions/93886/dek-kek-and-master-key-simple-explanation

Rebuild docker tomunderstand it more

don't do JWT for sessions 
http://cryto.net/~joepie91/blog/attachments/jwt-flowchart.png

http://cryto.net/%7Ejoepie91/blog/2016/06/19/stop-using-jwt-for-sessions-part-2-why-your-solution-doesnt-work/
