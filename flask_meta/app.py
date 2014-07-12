# -*- coding: utf-8 -*-

"""
This is the app that the appmeta will be run from.

"""


from flask import Flask as Flask
from flask.ext import admin, login, sqlalchemy

def init_app(app_name=__name__):
    return Flask(app_name)



