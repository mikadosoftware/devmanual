from wsgiref.simple_server import make_server
from simpleapp import methodapp

httpd = make_server('localhost', 5000, methodapp)
httpd.serve_forever()
