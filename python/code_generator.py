import re
from jinja2 import Environment, FileSystemLoader
from config import Config
from swagger import Swagger
import json

class CodeGenerator(object):
    def __init__(self):
        self._env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
        self._swagger = Swagger()
        self._swagger_json = self.swagger.swagger_json
        self._test_count = 0
        self._config = Config()
        
    @staticmethod
    def to_camelcase(string):
        return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), string)

    def generate_test_class_header(self, host, api_key):
        t = self.env.get_template('test_header.jinja')
        return t.render(host=host, api_key=api_key)
    
    def generate_test_class_function(self, 
                                    test_name,
                                    endpoint, 
                                    method,
                                    response_code,
                                    api_call,
                                    data=None,
                                    params=None,
                                    url_params=None
                                    ):
        t = self.env.get_template('test_class_function.jinja')
        return t.render(test_name = test_name,
                        endpoint = endpoint,
                        method = method,
                        response_code = response_code,
                        api_call = api_call,
                        data = data,
                        params = params,
                        url_params = url_params
                        )
    
    def get_class_names(self):
        class_names = {}
        for endpoint in sorted(self.swagger_json["paths"]):
            split_endpoint = endpoint.split('/')
            class_name = self.to_camelcase(split_endpoint[1].capitalize())
            try:
                class_names[class_name].append(endpoint)
            except KeyError, e:
                class_names[class_name] = []
                class_names[class_name].append(endpoint)
        return class_names

    def generate_test_name(self, endpoint, method):
       endpoint = endpoint.replace("/", "_").replace("{", "_").replace("}", "_")
       return "test" + endpoint + "_" + method + "(self):"

    def generate_api_call(self, endpoint, method):
       endpoint = endpoint.replace("/", ".").replace("{", "_(").replace("}", ")")
       endpoint = endpoint.replace("global", "global_")
       return endpoint + "." + method
       
    # params should be formatted like: {"hello": "world", "bye": 2}
    def generate_params(self, response_code, params=None):
        all_params = {}
        if response_code == "default":
            all_params["mock"] = 0 # Means the response code is undefined in swagger
        else:
            all_params["mock"] = int(response_code)
        if params != None:
            for param in params:
                all_params[param] = params[param]
        return all_params

    def generate_url_params(self, endpoint, value=None):
        if value == None:
            value = "test_url_param"
            #TODO: grab these from stoplight, can override with config
        if endpoint.count('{') < 1:
            return None
        elif endpoint.count('{') == 1:
            return endpoint.split('{', 1)[-1].split('}')[0] + " = " + "\"" + value + "\""
        else:
            split_endpoint = endpoint.split('{')
            url_params = split_endpoint[1].split('}')[0] + " = " + "\"" + value + "\"\n"
            url_params += "        " + split_endpoint[2].split('}')[0] + " = " + "\"" + value + "\""
            return url_params  
    
    @property
    def env(self):
        return self._env

    @property
    def swagger_json(self):
        return self._swagger_json

    @property
    def config(self):
        return self._config
        
    @property
    def swagger(self):
        return self._swagger