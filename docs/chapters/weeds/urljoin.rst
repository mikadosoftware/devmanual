================================
The unusual behaviour of urljoin
================================

os.path.join behaves in a pretty robust ways.

(examples)

urlparse.urljoin seems not to do so.

::

    >>> urlparse.urljoin("http://localhost/module/", "cnx1234")
    'http://localhost/module/cnx1234'

I expect the above behaviour.::

    >>> urlparse.urljoin("http://localhost:8000/module", "cnx1234")
    'http://localhost:8000/cnx1234'

Woooo.  What happened to module?::

    >>> urlparse.urljoin("http://localhost.com/module/", "cnx1234")
    'http://localhost.com/module/cnx1234'

one last gotcha::

    >>> urlparse.urljoin("http://localhost.com/module/", "/cnx1234")
    'http://localhost.com/cnx1234'


http://stackoverflow.com/questions/10893374/python-confusions-with-urljoin

So for RESTful navigation we want something else...
