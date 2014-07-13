import os
from ConfigParser import SafeConfigParser

def config_app_from_file(app):
    parsed_cfg = get_config()
    return extract_config(app, parsed_cfg,'appmeta_config')

def parse_config(file_name):
    parser = SafeConfigParser()
    parser.read(file_name)
    return parser

def print_config(parser):
    for section_name in parser.sections():
        print 'Section:', section_name
        print '  Options:', parser.options(section_name)
        for name, value in parser.items(section_name):
            print '  %s = %s' % (name, value)
        print '\n'

def get_config():
    #return parse_config('config.ini')
    c = parse_config('config.ini')
    print_config(c)
    return c

def extract_config(app_obj, parser, section_name):
    for name, value in parser.items(section_name):
        app_obj.config[name.upper()] = value
        print name.upper()
    return app_obj







