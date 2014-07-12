from .app import init_app

def test_init_app():
    app = init_app()
    appmeta = init_app('appmeta')
    assert app.name == 'flask_meta.app'
    assert appmeta.name == 'appmeta'
    assert str(type(app)) == "<class 'flask.app.Flask'>"