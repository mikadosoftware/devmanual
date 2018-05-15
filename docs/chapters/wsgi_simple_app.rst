=========================
Writing a simple WSGI app
=========================

WSGI Server
===========

WSGI is an amazingly cool ... idea.  It just reminds you that *all* web servers are doing
is passing text strings up and down a request/response cycle.  Remeber CGI? Its still that
simple.

(all WSGI stuff in here)




https://bitbucket.org/vithon/vithon-forum/src/abab8f2a7aef/viforum/forum.py

What should have happend?

start_response probably should have been left out, and ...
well thats the hard part - you need to be able to send back up
the chain a stream of bytes (body) *and* a environ / header dict
So it does need two channels.

Support for non-blocking requests?
A (thread) in an event-based server needs to have mechanisms for
halting its own processing while an I/O event occurs, and then restarting

This leads to rewrites of pretty much everything.

Application
-----------

An "app" is *only* a piece of code that calls start_response and so begins the
response process.

This is how middleware can operate - by deciding if or not to respond instead of
the "officially configured" app.

I think this "officially configured" app is also the source of much confusion.::

    >>> from doctest2.doclit import doclit
    ... def paul_app(environ, start_response):
    ...     """ """
    ...     #do something with environ
    ...     resp_headers = {'Content-Type': 'text/html'}
    ...     start_response("200 OK",
    ...     return "Hello World"



Serving the app
---------------

::

    >>> from waitress import serve
    ... serve(paul_app)


Adjusting a environ on way in
-----------------------------

TBC

Adjusting environ on way out
----------------------------

TBC

Setting and unsetting cookies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See RSSSO

Secure cookies
~~~~~~~~~~~~~~

Some people think that secure cookies is about encrypting the text on the
cookie so bad guys cannot read it.  Frankly, this is nonsense.  You will
make a mistake, and they will read it.  So we have an issue - which is faster
an in-memory redis lookup or a decryption of a *really secure* piece of text.

This looks like an interesting test...
