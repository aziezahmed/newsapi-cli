"""An Object to store and retrive user settings"""

import os, configparser

from os.path import expanduser

class UserSettings(object):
    def __init__(self):

        self.basedir = "~/.newsapi-cli"

        if not os.path.exists(expanduser(self.basedir)):
            print("Creating base dir %s"%self.basedir)
            os.makedirs(expanduser(self.basedir))

        self.user_config_dir = os.path.expanduser(self.basedir);
        self.user_config_path = self.user_config_dir + "/newsapi-cli.ini"

        self.config = configparser.ConfigParser()
        self.config.add_section('newsapi-cli')
        self.config['newsapi-cli']['api-key'] = "none"

        if not os.path.isfile(self.user_config_path):
            with open(self.user_config_path, 'w') as f:
                self.config.write(f)

        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(self.user_config_path)

    def get_api_key(self):
        NEWSAPI_KEY = os.environ.get("NEWSAPI_KEY", self.config['newsapi-cli']['api-key'])
        return NEWSAPI_KEY

    def set_api_key(self, api_key):
        self.config.set('newsapi-cli','api-key',api_key)
        with open(self.user_config_path, 'w') as configfile:
            self.config.write(configfile)
