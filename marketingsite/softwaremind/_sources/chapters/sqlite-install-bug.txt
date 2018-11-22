===========================
Installing Sqlite in a venv
===========================

===========================

Seems to be painful - best answer so far seems to be
to link or mv.

So we build sqlite database as usual in local.
Then build the venv and link externally, or copy in the .so
into venv site-packages.


$ ln -s /usr/local/lib/python2.7/site-packages/_sqlite3.so .

>> import sqlite3
