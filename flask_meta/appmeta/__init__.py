# -*- coding: utf-8 -*-


import os, sys, inspect
# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

"""
This is the app that the appmeta will be run from.
"""
__name__ = 'appmeta'
from flask import Flask as Flask
from flask.ext import admin, login, sqlalchemy
from config import config

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
    config.config_app_from_file(app, 'config.ini')
    return app

def init_db(app):
    """
    Initializes sqlalchemy with the flask app after the app is configured.

    :params: app
        The flask app is passed immediately after it is declared/initialized
        (e.g. 'project', 'appmeta', etc.)
    """
    return sqlalchemy.SQLAlchemy(app)


def create_app():
    """
    Using the previous functions, creates the app, adds extensions to the
    app, and returns the app and extension variables.
    """
    
    app = init_app()
    app = config_app(app)
    db  = init_db(app)
    return app, db

(appmeta, db) = create_app()

