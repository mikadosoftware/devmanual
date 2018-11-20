============
Non blocking
============

============

How can we simply improve the performance (concurrent requests)
of a WSGI server?

The simplest issue is - threads.  OS level threads are realtively speaking,
cumbersome and high process.  Our Python interpreter already sits in one
happily churning away, and to create another is an "expensive" process.

Pseudo-threads, like greenlets, can provide an answer.

installing gevent (FreeBSD)
---------------------------

Firstly install system-wide libevent2 - I find simplest to
install /devel/py-gevent and ensure all compile well outisde pip.

Then - pip does not look for the libevent system files so we tell it where to look.

  $ export CFLAGS=-I/usr/local/include
  $ export LDFLAGS=-L/usr/local/lib
  (http://kdl.nobugware.com/post/2011/11/15/compile-gevent-osx-or-freebsd-pip)

Now pip install inside the venv and all should be well.


Start simple
------------

Simplest app we can

.. literalinclude:: simpleapp.py
   :linenos:
   :lines: 7-25

We run it using wsgiref

.. literalinclude:: run.py
   :linenos:


We can run the funkload ... (funkload needs a seperate article)
fl-run-test testcase.py

Bench - concurrent users
~~~~~~~~~~~~~~~~~~~~~~~~

  fl-run-bench <unittestfile> <ClassinFile>.<testmethodinclass>

  fl-run-bench testcase.py MyWSGITest.test_simple


Results
-------

I can see my plain WSGI server work quite acceptably at 20+ concurrent users if
total response time < 0.01 seconds However when response time hits 0.1 seconds,
I get a 90% fail rate, as threads are sleeping (ie processing) whilst the new
requests come in.


Ok, sprinkle on magic pixie dust
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

lets add in greenlets to the application...

.. literalinclude:: greenapp.py
   :linenos:

And, nothing much changes in the bench tests...

This is because the thread that decides to sleep is able to be a greenlet,
the server is still creating OS threads, becasue the server does not know
about greenlets.  Lets fix that/

.. literalinclude:: greenrun.py


Now, we can go from 10 to 100 threads before seeing any problems.

An order of magnitude improvement on the same laptop.



Follow on
---------

How many threads are spun up?
How do i see those threads
Will dtrace help



Biblio
------

http://bottlepy.org/docs/dev/async.html
