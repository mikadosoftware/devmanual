
### Now we need to run a server that co-operates in threads

import greenapp

#from wsgiref.simple_server import make_server
from gevent import pywsgi

app = greenapp.myapp


httpd = pywsgi.WSGIServer(('localhost', 5000), app)
httpd.serve_forever()

