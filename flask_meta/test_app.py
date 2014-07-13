from flask_meta.app import init_app, config_app
from flask_meta.config import config

def test_init_app():
    app = init_app()
    appmeta = init_app('appmeta')
    assert app.name == 'flask_meta.app'
    assert appmeta.name == 'appmeta'
    assert str(type(app)) == "<class 'flask.app.Flask'>"

def test_config_app():
    app = init_app()
    app.config = config_app(app)
    assert str(type(app)) == "<class 'flask.app.Flask'>"
    assert app.config.keys() == config.keys()
    