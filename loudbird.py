#!/usr/bin/env python

# Author: Sam Hart <hartsn@gmail.com>

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import os
import time

import pyttsx
from twython import Twython

config_file = os.path.expanduser("~/.loudbird.conf")

config = configparser.SafeConfigParser()

def backup_config():
    backup_file = "%s.backup-%i" % (configFile % int(time.time()))
    os.rename(configFile, backup_file)

def create_config():
    if not config.has_section('twatter'):
        config.add_section('twatter')

    config.set('twatter', 'APP_KEY', "HEY_CHUMP_PUT_YOUR_APP_KEY_HERE")
    config.set('twatter', 'APP_SECRET', "HEY_CHUMP_PUT_YOUR_SECRET_HERE")

def load_config():
    if os.path.isdir(config_file):
        try:
            config.readfp(open(config_file))
            if(config.has_option('twatter', 'APP_KEY') and config.has_option('twatter', 'APP_SECRET')):
                pass
            else:
                backup_config()
                create_config()