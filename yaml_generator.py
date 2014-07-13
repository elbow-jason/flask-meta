import os

def generate_default_yaml_cfg():
    my_yml_path = os.getcwd()
    yml_text = """
    SECRET_KEY: 'appmeta_dev_key'
    META_CREDENTIALS: 'metaadmin,password'
    ADMIN_CREDENTIALS: 'admin,password'
    SQLALCHEMY_DATABASE_URI: sqlite://{}/test.db
    SQLALCHEMY_BINDS: 
     - appmeta: sqlite://{}/appmeta.db
    SERVER_URL: "http://localhost:5000"
    SQLALCHEMY_ECHO: True
    DEBUG: True
    SECURITY_PASSWORD_HASH: bcrypt

    # Upon creation I am going to make sure that the user selects a desired
    # database before proceeding to ensure no hangups upon attempting
    # to go to production. See comments below for further production 
    # directives.

    # Also, using a password protected database as your 
    # database (i.e. MySQL or my favorite PostgreSQL) will
    # make your database much more secure than using SQLite (as 
    # is the default). SQLite itself has no concept of users or
    # permissions, and instead relies on OS permissions for
    # security.


    # this config should absolutely be changed before 
    # production. Specifically, the SECRET_KEY, META_CREDENTIALS,
    # and ADMIN_CREDENTIALS.
    """.format(my_yml_path, my_yml_path)

    with open('config.yaml', 'w') as y:
        y.write(yml_text)


