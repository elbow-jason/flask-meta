import os
from flask_meta import appmeta

def run_appmeta():
    """
    Runs the flask-meta appmeta server.
    """
    host = '0.0.0.0'
    port = 5000
    debug = True
    if debug:
        print ' * debug is active'
    appmeta.run(debug=debug, port=port, host=host)

if __name__ == '__main__':
    run_appmeta()
