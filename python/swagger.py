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
        
        content = repo.contents(self.config.swagger_filename)
        swagger = base64.b64decode(content.content)
        return json.loads(swagger)

    def get_endpoints(self, method=None):
        endpoints = []
        if method == None:
            # Return all endpoints
            for key in sorted(self.swagger_json["paths"]):
                endpoints.append(key)
            # endpoints.remove('/')
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
        
    def get_response_codes(self, endpoint, method):
        return sorted(self.swagger_json["paths"][endpoint][method]["responses"].keys())

    def get_example_data(self, endpoint, method, response_code):
        try:
            #TODO: This should come from requests instead of responses
            return self.swagger_json["paths"][endpoint][method]["responses"][response_code]["examples"]["application/json"]
        except KeyError, e:
            return None

    @property
    def config(self):
        return self._config

    @property
    def swagger_json(self):
        return self._swagger_json