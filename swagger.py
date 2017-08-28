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
        contents = repo.contents('/')
        content = repo.blob(contents[self.config.swagger_filename].sha)
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
        try:
            return self.swagger_json["paths"][endpoint][method]["description"]
        except KeyError, e:
            return ""

    def get_endpoint_short_description(self, endpoint, method):
        return self.swagger_json["paths"][endpoint][method]["summary"]

    def get_response_codes(self, endpoint, method):
        return sorted(self.swagger_json["paths"][endpoint][method]["responses"].keys())

    def get_query_parameters(self, endpoint, method, language=None):
        qparams = {}
        try:
            query_params = self.swagger_json["paths"][endpoint][method]["parameters"]
            for param in query_params:
                is_int = False
                if param[u'in'] == u'query':
                    if param[u'type'] == u'string':
                        if str(param[u'name']) == "start_date":
                            type_test_data = "2016-01-01"
                        elif str(param[u'name']) == "end_date":
                            type_test_data = "2016-04-01"
                        else:
                            type_test_data = "test_string"
                    elif param[u'type'] == u'number':
                        type_test_data = 0
                        is_int = True
                    elif param[u'type'] == u'integer':
                        type_test_data = 1
                        is_int = True
                    elif param[u'type'] == u'boolean':
                        type_test_data = "true"
                    else:
                        type_test_data = "default_test_data"
                    if is_int is True:
                        qparams[str(param[u'name'])] = int(type_test_data)
                    else:
                        if str(param[u'name']) == "aggregated_by":
                            qparams[str(param[u'name'])] = "day"
                        elif str(param[u'name']) == "sort_by_direction":
                            qparams[str(param[u'name'])] = "asc"
                        elif str(param[u'name']) == "country":
                            qparams[str(param[u'name'])] = "US"
                        elif str(param[u'name']) == "email_address":
                            qparams[str(param[u'name'])] = "example@example.com"
                        else:
                            qparams[str(param[u'name'])] = type_test_data
                    is_int = False
        except KeyError, e:
            if(language == 'nodejs'):
                if param[u'$ref']:
                    pass
                else:
                    qparams = None
        return qparams

    def get_example_data(self, endpoint, method, response_code):
        try:
            try:
                count = 0
                while self.swagger_json["paths"][endpoint][method]["parameters"][count]["in"] != "body":
                    count = count + 1
                data = self.swagger_json["paths"][endpoint][method]["parameters"][count]["schema"]["example"]
            except IndexError:
                return None
            return data
        except KeyError, e:
            return None

    @property
    def config(self):
        return self._config

    @property
    def swagger_json(self):
        return self._swagger_json