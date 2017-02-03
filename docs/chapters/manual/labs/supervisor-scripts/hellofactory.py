#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from flask import Flask


def hello():
    return "Hello World! " + datetime.datetime.today().isoformat()

'''
supervisor-scripts(master)$ /usr/home/pbrian/venvs/test-rc/bin/waitress-serve --call hellofactory:appfactory
serving on http://0.0.0.0:8080

#https://github.com/Pylons/waitress/blob/master/waitress/runner.py
'''


def appfactory():
    """
    an attempt at an app_factory
    """
    app = Flask(__name__)
    app.add_url_rule("/", view_func=hello)
    return app

