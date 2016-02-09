import os
import yaml


class Config(object):
    """All configuration for this app is loaded here"""
    def __init__(self):
        if (os.environ.get('ENV') != 'prod'):  # We are not in Heroku
            self.init_environment()

        """Allow variables assigned in config.yml available the following variables
           via properties"""
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        with open(self.base_path + '/config.yml') as stream:
            self.config = yaml.load(stream)
            self._github_user = self.config['github_user']
            self._swagger_source = self.config['swagger_source']
            self._swagger_filename = self.config['swagger_filename']

    @staticmethod
    def init_environment():
        """Allow variables assigned in .env available using
           os.environ.get('VAR_NAME')"""
        base_path = os.path.abspath(os.path.dirname(__file__))
        if os.path.exists(base_path + '/.env'):
            for line in open(base_path + '/.env'):
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]

    @property
    def github_user(self):
        return self._github_user

    @property
    def swagger_source(self):
        return self._swagger_source

    @property
    def swagger_filename(self):
        return self._swagger_filename
        
    def get_custom_init(self, endpoint):
        return self.config[endpoint]['custom_init']
    
    def get_data(self, endpoint):
        return self.config[endpoint]['data']
    
    def get_patched_data(self, endpoint):
        return self.config[endpoint]['patched_data']

    def get_put_data(self, endpoint):
        return self.config[endpoint]['put_data']
        
    def get_id(self, endpoint):
        return self.config[endpoint]['id']