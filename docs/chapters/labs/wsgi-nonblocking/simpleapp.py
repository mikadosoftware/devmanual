
### SImplest app we can provide
### using yields
import time

class myapp(object):
    """
    Stolen from PEP333
    NB - same applies here - we are returning an instance of a class that
    is an iterable - we do not return the class)
    """
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        status = "200 OK"
        response_headers = [('Content-type', 'text/plain'),
                            ('X-paul','pbrian')]
        self.start_response(status, response_headers)
        yield "Hello"
        time.sleep(0.1)
        yield "World"
        