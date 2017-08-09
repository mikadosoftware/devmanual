#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from flask import Flask
app = Flask(__name__)

## Just mark the log
open("/tmp/foobar","a").write("\nStarting: " 
                               + datetime.datetime.today().isoformat()
                              )



@app.route("/")
def hello():
    return "Hello World! " + datetime.datetime.today().isoformat()

### I want to have the app die, and so prove rc restarts it
@app.route("/kill")
def killself():
    open("/tmp/foobar","a").write("\nkilled: " 
                                  + datetime.datetime.today().isoformat()
                                  )
    #os._exit(1)    
    return "foo"

if __name__ == "__main__":
    app.run(port=5003)
