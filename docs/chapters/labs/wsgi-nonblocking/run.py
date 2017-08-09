#import greenapp
import simpleapp
from wsgiref.simple_server import make_server

#app = greenap.myapp

app = simpleapp.myapp

httpd = make_server('localhost', 5000, app)
httpd.serve_forever()

