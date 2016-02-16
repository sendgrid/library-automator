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
        try:
            return self.config[endpoint]['custom_init']
        except KeyError, e:
            return None
    
    def get_data(self, endpoint):
        try:
            return self.config[endpoint]['data']
        except KeyError, e:
            return None

    def get_params(self, endpoint, method=None):
        try:
            if method:
                return self.config[endpoint]['params'][method]
            else:
                return self.config[endpoint]['params']
        except KeyError, e:
            return None

    def get_mocked_params(self, endpoint, method=None):
        try:
            if method:
                return self.config[endpoint]['mocked_params'][method]
            else:
                return self.config[endpoint]['mocked_params']
        except KeyError, e:
            return None
        
    def get_patched_data(self, endpoint):
        try:
            return self.config[endpoint]['patched_data']
        except KeyError, e:
            return None

    def get_put_data(self, endpoint):
        try:
            return self.config[endpoint]['put_data']
        except KeyError, e:
            return None

    def get_custom_class_name(self, endpoint):
        try:
            return self.config[endpoint]['custom_class_name']
        except KeyError, e:
            return None
        
    def get_id(self, endpoint):
        try:
            return self.config[endpoint]['id']
        except KeyError, e:
            return None
            
    def get_init_id_value(self, endpoint):
        try:
            return self.config[endpoint]['init_id_value']
        except KeyError, e:
            return None
            
    def is_proxied(self):
        return self.config["global"]["is_proxied"]

    def get_proxy_url(self):
        return self.config["global"]["proxy_url"]
        
    def get_final_endpoint(self, endpoint):
        try:
            return self.config[endpoint]['final_endpoint']
        except KeyError, e:
            return None
 
    def get_full_endpoint_path(self, endpoint):
        try:
             return self.config[endpoint]['full_endpoint_path']
        except KeyError, e:
             return None    

    def get_appended_endpoint(self, endpoint, end):
        try:
             return self.config[endpoint]['appended_endpoint'][end]
        except KeyError, e:
             return None         

    def get_patched_params_appended(self, end):
        try:
             return self.config[end]['patched_data']
        except KeyError, e:
             return None       