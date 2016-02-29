import os
import github3
import base64
import json
from config import Config


class Swagger(object):
    def __init__(self):
        self._config = Config()
        self._swagger_json = self._get_swagger_json()

    def _get_swagger_json(self):
        github_token = os.environ.get('GITHUB_TOKEN')
        gh = github3.login(token=github_token)
        repo = gh.repository(self.config.github_user, self.config.swagger_source)
        
        content = repo.file_contents(self.config.swagger_filename)
        swagger = base64.b64decode(content.content)
        return json.loads(swagger)

    def get_endpoints(self, method=None):
        endpoints = []
        if method == None:
            # Return all endpoints
            for key in sorted(self.swagger_json["paths"]):
                endpoints.append(key)
        else:
            # Return all endpoints for a given method
            for key in sorted(self.swagger_json["paths"]):
                try:
                    exists = self.swagger_json["paths"][key][method]
                    endpoints.append(key)
                except KeyError, e:
                    pass
        return endpoints
        
    def get_endpoint_object(self, endpoint, method):
        return self.swagger_json["paths"][endpoint][method]

    def get_endpoint_objects(self, endpoint):
        return self.swagger_json["paths"][endpoint]
        
    def get_endpoint_description(self, endpoint, method):
        return self.swagger_json["paths"][endpoint][method]["description"]

    def get_endpoint_short_description(self, endpoint, method):
        return self.swagger_json["paths"][endpoint][method]["operationId"]
    
    def get_response_codes(self, endpoint, method):
        return sorted(self.swagger_json["paths"][endpoint][method]["responses"].keys())
        
    def get_query_parameters(self, endpoint, method):
        query_params = self.swagger_json["paths"][endpoint][method]["parameters"]
        qparams = {}
        try:
            for param in query_params:
                if param[u'in'] == u'query':
                    if param[u'type'] == u'string':
                        type_test_data = "test_string"
                    elif param[u'type'] == u'number' or u'integer':
                        type_test_data = 0
                    elif param[u'type'] == u'boolean':
                        type_test_data = True
                    else:
                        type_test_data = "default_test_data"   
                    qparams[str(param[u'name'])] = type_test_data
        except KeyError, e:
            qparams = None
        return qparams

    def get_example_data(self, endpoint, method, response_code):
        try:
            #TODO: This should come from requests instead of responses
            #data = self.swagger_json["paths"][endpoint][method]["responses"][response_code]["examples"]["application/json"]
            #return json.dumps(data)
            return {"sample": "data"}
        except KeyError, e:
            return None

    @property
    def config(self):
        return self._config

    @property
    def swagger_json(self):
        return self._swagger_json