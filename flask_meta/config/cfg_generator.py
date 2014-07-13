import os

def yaml_cfg():
    current_dir = os.getcwd()
    yaml_text = """
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

# this line is for testing (do not remove)
""".format(current_dir, current_dir)
    return str(yaml_text)

def ini_cfg():
    current_dir = os.getcwd()
    text = """
[appmeta_config]
SECRET_KEY = 'appmeta_dev_key'
META_CREDENTIALS = {'name':'metaadmin','password':'password'}
ADMIN_CREDENTIALS = {'name':'admin','password':'password'}
SQLALCHEMY_DATABASE_URI = 'sqlite://%s/test.db'
SQLALCHEMY_BINDS = {'appmeta' : 'sqlite://%s/appmeta.db' }
SERVER_URL: "http://localhost:5000"
SQLALCHEMY_ECHO: True
DEBUG: True
SECURITY_PASSWORD_HASH: 'bcrypt'

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

# this line is for testing (do not remove)
""" % (current_dir, current_dir)
    return str(text)

def write_file_safe(text, file_name, overwrite=False):
    if not overwrite:
        if not os.path.isfile(file_name):
            new_file = open(file_name, 'w+')
            new_file.write(text)
            new_file.close()
        else:
            print "The file '{}' already exists. To overwrite\
                pass overwrite=True as a kwarg.".format(file_name))
            print "No action taken."

def write_yaml_cfg():
    write_file_safe(yml_cfg(), 'config.yaml')

def write_ini_cfg():
    write_file_safe(ini_cfg(), 'config.ini')

if __name__ == '__main__':
    write_ini_cfg()
