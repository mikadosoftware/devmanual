=======
webtest
=======

=======

Writing a WSGI app
Writing a WSGI *server*
Testing a WSGI server -
http://wsgi.readthedocs.org/en/latest/learn.html
Writing WSGI Middleware


Testing the whole thing::

  Locally
  On HTTP
  Load test



Let us imagine we have a nice wsgi app.  Lets imagine it is a Flask app.
We want to test that the "hello world" actually returns hello world.::




    >>> from flask import Flask
    >>> app = Flask("myapp")
    >>> wapp = app.wsgi_app

::


    def build_environ():
        """
        We are playing at a low level with WSGI - wanting to wrap repoze.
        http://www.python.org/dev/peps/pep-0333/

        To test manually we need to generate correct HTTP Headers
        """
        import StringIO
        request_fo = StringIO.StringIO()
        err_fo = StringIO.StringIO()

        ###wsgi reqd keys and default valus
        wsgi_specific_headers = {"wsgi.version": (1,0),
                                 "wsgi.url_scheme": "http",
                                 "wsgi.input": request_fo,
                                 "wsgi.errors": err_fo,
                                 "wsgi.multithread": False,
                                 "wsgi.multiprocess": False,
                                 "wsgi.run_once": False
                                }

        ### key = HEADER (RFCLOC, NOTNULL, validvalues)
        HTTP_HEADERS = {"REQUEST_METHOD": "GET",
                        "SCRIPT_NAME": "module",
                        "PATH_INFO": "/cnxmodule:1234/",
                        "QUERY_STRING": "",
                        "CONTENT_TYPE": "",
                        "CONTENT_LENGTH": "",
                        "SERVER_NAME": "1.2.3.4",
                        "SERVER_PORT": "80",
                        "SERVER_PROTOCOL": "HTTP/1.1"
                        }
        d = {}
        d.update(wsgi_specific_headers)
        d.update(HTTP_HEADERS)
        return d
