import os


config = {}
config['SECRET_KEY']                ='dev_key'
config['SQLALCHEMY_DATABASE_URI']   = 'sqlite://{}/test.db'.format(os.getcwd())
config['SQLALCHEMY_BINDS']          = { 'appmeta' : 'sqlite://{}/appmeta.db'.format(os.getcwd()) }
config['SERVER_URL']                = "http://localhost:5000"
config['SQLALCHEMY_ECHO']           = True


