:rm
An example of running doclit
============================

We can see

>>> from doctest2.doclit import doclit
>>> starting_wsgi = doclit.import_docs("starting_wsgi.rst", "starting_wsgi")
>>> starting_wsgi.foo('HH')
'HH'

from gunicorn.app.pasterapp import paste_server
from paste.deploy import loadapp

app = loadapp('config:foobar/foobar.ini', relative_to='.')
paste_server(app, host='0.0.0.0', port=8002)
