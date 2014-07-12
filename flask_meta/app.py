# -*- coding: utf-8 -*-

"""
This is the app that the appmeta will be run from.

"""


from flask import Flask as Flask
from flask.ext import admin, login, sqlalchemy

def init_app(app_name=__name__):
    return Flask(app_name)

def test_init_app():
    app = init_app()
    appmeta = init_app('appmeta')
    assert app.name == __name__
    assert appmeta.name == 'appmeta'

