import os
import configparser

config_path = os.path.join( os.path.dirname(__file__), '..', 'conf/config.ini')

cfg = configparser.ConfigParser
cfg.read(config_path)
print(config_path)