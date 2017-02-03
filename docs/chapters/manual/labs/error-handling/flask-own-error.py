
"""
In Flask, abort(404) is a common idiom.
However that seems to be fairly diffcult to trap higher up
in the code.  I therefore prefer to do the following - create and
raise an error which I can catch normally.

Unhandled such an error will bubble up and produce ::

  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
  <title>404 Not Found</title>
  <h1>Not Found</h1>
  Missed me!

If flask is run in debug, it still bubbles up.

If you dont see it, something else is in the way.

http://localhost:5000/fffff ::

   404 = missed me !

http://localhost:5000/401 ::

   500 / Some change I want handled
   (THis just shows I can catch the original error
    in try/except and output a new one as needed)

http://localhost:5000/hello ::

   Hello World!

"""


from werkzeug.exceptions import HTTPException

### raising our own errors
class Rhaptos2HTTPError(HTTPException):
    code = 500
    description = "Default Description"

from flask import Flask
app = Flask(__name__)

@app.route('/<foo>')
def hello_world(foo):
    try:
        if foo == "hello":
            return "Hello world"
        elif foo == "401":
            e = Rhaptos2HTTPError()
            e.code=401
            e.description="Fake error"
            raise e
        else:
            e = Rhaptos2HTTPError()
            e.code=404
            e.description="Missed me!"
            raise e
    except Rhaptos2HTTPError, e:
        if e.code == 401:
            e.code = 500
            e.description = "Some change I want handled"
            raise e
        else:
            raise e
            
        
    

if __name__ == '__main__':
    app.run(debug=True)