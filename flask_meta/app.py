# -*- coding: utf-8 -*-

"""
This is the app that the appmeta will be run from.

"""

from flask import Flask as Flask
from flask.ext import admin, login, sqlalchemy
from flask_meta.config import config


def init_app(app_name=__name__):
    """
    returns a flask app object.
    """
    return Flask(app_name)

def config_app(app):
    """
    Configures the app that is passed, then returns the app.
    Should be called directly after init_app() so extensions will work
    properly.

    :params: app
        The flask app is passed immediately after it is declared/initialized
        (e.g. 'project', 'appmeta', etc.)
    """
    for key in config.keys():
        app.config[key] = config[key]
    return app


def create_app():
    """
    Using the previous functions, creates the app, adds extensions to the app, and returns the app and 
    extension variables.
    """
    app = init_app()
    app = config_app(app)
    return app

app = create_app()
