#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys, os
import datetime
from flask import Flask
from signal import SIGTERM
####
pid = os.getpid()


def hello():
    return "Hello World! My PID is : %s. Time is %s" % (pid,
                                                        datetime.datetime.today().strftime("%H%M%S"))
 

def killself():
    open("/tmp/foobar","w").write("killed")
    os.kill(pid, SIGTERM)    
    
'''
this one will need to kill

supervisor-scripts(master)$ /usr/home/pbrian/venvs/test-rc/bin/waitress-serve --call hellofactory:appfactory
serving on http://0.0.0.0:8080

#https://github.com/Pylons/waitress/blob/master/waitress/runner.py
.pth file in venv
add2virtualenv


'''


def appfactory():
    """
    an attempt at an app_factory
    """
    app = Flask(__name__)
    app.add_url_rule("/", view_func=hello)
    app.add_url_rule("/kill", view_func=killself)
    return app


if __name__=='__main__':
    appfactory().run(port=5003)

