#!/usr/bin/env python
# -*- coding:utf-8 -*-

## trivial WSGI example


import datetime
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! " + datetime.datetime.today().isoformat()

if __name__ == "__main__":
    app.run(port=5003)
