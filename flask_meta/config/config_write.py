try:
    from flask_meta.config.cfg_generator import write_ini_cfg
    print "app offline, importing config writer locally"
except:
    from .cfg_generator import write_ini_cfg
finally:
    write_ini_cfg()