from flask_meta.app import init_app, config_app
from flask_meta.config.configw import config

def test_init_app():
    app = init_app()
    appmeta = init_app('appmeta')
    assert app.name == 'flask_meta.app'
    assert appmeta.name == 'appmeta'
    assert str(type(app)) == "<class 'flask.app.Flask'>"

def test_config_app():
    apptester = init_app()
    apptester = config_app(apptester)
    assert str(type(apptester)) == "<class 'flask.app.Flask'>"
    for key in config.keys():
        #test that keys of config dict are in the app.config
        assert key in apptester.config.keys()
        #test that values of the app.config match the config dict
        assert apptester.config[key] == config[key]