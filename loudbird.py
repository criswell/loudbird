#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Sam Hart <hartsn@gmail.com>

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import os
import time
import re

import pyttsx
from twython import Twython

config_file = os.path.expanduser("~/.loudbird.conf")

config = configparser.SafeConfigParser()

match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)

def backup_config():
    backup_file = "%s.backup-%i" % (configFile % int(time.time()))
    os.rename(configFile, backup_file)

def create_config():
    if not config.has_section('twatter'):
        config.add_section('twatter')

    config.set('twatter', 'APP_KEY', "HEY_CHUMP_PUT_YOUR_APP_KEY_HERE")
    config.set('twatter', 'APP_SECRET', "HEY_CHUMP_PUT_YOUR_SECRET_HERE")
    config.set('twatter', 'OAUTH_TOKEN', "SAMESIES")
    config.set('twatter', 'OAUTH_TOKEN_SECRET', 'DUH')

    config.add_section('following')
    save_config()

def save_config():
    with open(config_file, 'w') as f:
        config.write(f)

def load_config():
    if os.path.isfile(config_file):
        with open(config_file, 'r') as f:
            config.readfp(f)
            if(config.has_option('twatter', 'APP_KEY') and config.has_option('twatter', 'APP_SECRET')):
                pass
            else:
                backup_config()
                create_config()
    else:
        create_config()

load_config()

twitter = Twython(config.get('twatter', 'APP_KEY'), \
    config.get('twatter', 'APP_SECRET'), \
    config.get('twatter', 'OAUTH_TOKEN'), \
    config.get('twatter', 'OAUTH_TOKEN_SECRET'))

engine = pyttsx.init()

follows = config.items('following')
for i in follows:
    name = i[0]
    value = int(i[1])
    print "Name: %s" % name

    if value < 0:
        timeline = twitter.get_user_timeline(screen_name=name, \
        count=abs(value), exclude_replies="true")
    else:
        timeline = twitter.get_user_timeline(screen_name=name, \
        since_id=value, exclude_replies="true")

    for t in timeline:
        test_line = []
        for item in t['text'].split(' '):
            result = match_urls.match(item)
            if result is None:
                test_line.append(item)
        line = ' '.join(test_line)
        print line
        engine.say(line)
        #engine.runAndWait()
        #time.sleep(5)
engine.runAndWait()