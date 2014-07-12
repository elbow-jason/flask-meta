from .app import init_app

def test_init_app():
    app = init_app()
    appmeta = init_app('appmeta')
    assert app.name == __name__
    assert appmeta.name == 'appmeta'