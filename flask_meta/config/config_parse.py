from ConfigParser import SafeConfigParser



def read_config(file_name):
    parser = SafeConfigParser()
    parser.read(file_name)



