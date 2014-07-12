import os

def configure(app):
    """
    This file is used for configuration of app.py's Flask app.
    :params: app
        The flask app is passed immediately after it is declared/initialized(e.g. 'project', 'appmeta', etc.)
    """
    app.config['SECRET_KEY']                ='dev_key'
    app.config['SQLALCHEMY_DATABASE_URI']   = 'sqlite://{}/test.db'.format(os.getcwd())
    app.config['SQLALCHEMY_BINDS']          = {'appmeta' : 'sqlite://{}/appmeta.db'.format(os.getcwd())}
    app.config['SERVER_URL']                = "http://localhost:5000"
    app.config['SQLALCHEMY_ECHO']           = True
    return app
