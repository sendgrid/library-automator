import re
import os
from jinja2 import Environment, FileSystemLoader
from swagger import Swagger
from config import Config
import json

class CodeGenerator(object):
    def __init__(self, language):
        self._env = Environment(loader=FileSystemLoader(language + '/templates'), trim_blocks=True, lstrip_blocks=True)
        self._swagger = Swagger()
        self._swagger_json = self.swagger.swagger_json
        self._test_count = 0
        self._config = Config()
        self._language = language

    @staticmethod
    def to_camelcase(string):
        return re.sub(r'(?!^)_([a-zA-Z])', lambda m: m.group(1).upper(), string)

###############################################################################
####### GENERATE TESTS
###############################################################################

    def generate_tests(self):
        if self.config.is_proxied:
            host = self.config.proxy_url
        else:
            host = self.config.host
        api_key = self.config.api_key

        class_names = self.get_class_names()
        generated_test_class = self.generate_test_class_header()
        for key in sorted(class_names): # Loop through all sorted endpoints, grouped by class name
            for endpoint in class_names[key]:
                objects = self.swagger.get_endpoint_objects(endpoint)
                for method in objects:
                    if method != "parameters":
                        test_name = self.generate_test_name(endpoint, method)
                        response_codes = self.swagger.get_response_codes(endpoint, method)
                        response_code = response_codes[0]
                        data = self.swagger.get_example_data(endpoint, method, response_code)
                        if self._language == "python":
                            try:
                                if "true" in data:
                                    data = data.replace("true", "True")
                                if "false" in data:
                                    data = data.replace("false", "False")
                            except TypeError, e:
                                pass
                        if data:
                            data = data.replace("<img src='cid:ii_139db99fdb5c3704'>", "<img src=[CID GOES HERE]>")
                        api_call = self.generate_api_call(endpoint, method)
                        query_params = self.swagger.get_query_parameters(endpoint, method)
                        params = self.generate_params(response_code, query_params, mock=False)
                        url_params = self.generate_url_params(endpoint)
                        if self._language == "python":
                            headers = self.generate_headers(response_code)
                        if self._language == "php":
                            headers = "X-Mock: " + response_code
                        if response_code != "default": # schema undefined in swagger
                            generated_test_class += self.generate_test_class_function(test_name,
                                                                                      endpoint,
                                                                                      method,
                                                                                      response_code,
                                                                                      api_call,
                                                                                      params=params,
                                                                                      url_params=url_params,
                                                                                      data=data,
                                                                                      headers=headers
                                                                                      )
        if self._language == "php":
            generated_test_class += "}"
        return generated_test_class

    def generate_test_class_header(self):
        t = self.env.get_template('test_header.jinja')
        return t.render()

    def generate_test_class_function(self,
                                    test_name,
                                    endpoint,
                                    method,
                                    response_code,
                                    api_call,
                                    data=None,
                                    params=None,
                                    url_params=None,
                                    headers=None
                                    ):
        t = self.env.get_template('test_class_function.jinja')
        return t.render(test_name = test_name,
                        endpoint = endpoint,
                        method = method,
                        response_code = response_code,
                        api_call = api_call,
                        data = data,
                        params = params,
                        url_params = url_params,
                        headers = headers
                        )

    def generate_test_name(self, endpoint, method):
       endpoint = endpoint.replace("/", "_").replace("{", "_").replace("}", "_")
       call = ""
       if self._language == "python":
           call = "(self):"
       if self._language == "php":
           call = "()"
       return "test" + endpoint + "_" + method + call

    def generate_api_call(self, endpoint, method):
       if self._language == "python":
           endpoint = endpoint.replace("/", ".").replace("{", "_(").replace("}", ")")
           # Account for Python reserved word
           endpoint = endpoint.replace("global", "_(\"global\")")
       if self._language == "php":
           endpoint = endpoint.replace("{", "_($").replace("}/", ")->")
           endpoint = endpoint.replace("}", ")->")
           endpoint = endpoint[1:]
           endpoint = endpoint.replace("/", "()->")
       seperator = ""
       if self._language == "python":
           seperator = "."
       if self._language == "php":
           if endpoint.endswith(">"):
               seperator = ""
           else:
               seperator = "()->"
       return endpoint + seperator + method

    def generate_headers(self, response_code):
        header = {}
        header["X-Mock"] = int(response_code)
        return header

###############################################################################
####### GENERATE USAGE.md
###############################################################################

    def generate_docs(self):
        class_names = self.get_raw_class_names()
        generated_documentation = self.generate_documenation_title()
        generated_documentation += self.generate_documentation_toc(self.get_raw_class_names())
        for key in sorted(class_names):
            heading = self.generate_heading_name(key.upper().replace('_', ' '))
            heading_link = heading.lower().replace(' ', '_')
            generated_documentation += self.generate_documentation_header(heading, heading_link)
            for endpoint in class_names[key]:
                objects = self.swagger.get_endpoint_objects(endpoint)
                for method in objects:
                    if method != "parameters":
                        generated_documentation += self.generate_documentation_endpoint(endpoint, method)

        return generated_documentation.encode('ascii', 'ignore')

    def generate_documenation_title(self):
        t = self.env.get_template('documentation_title.jinja')
        return t.render()

    def generate_documentation_toc(self, class_names):
        toc = ''
        for key in sorted(class_names):
            heading = self.generate_heading_name(key.upper().replace('_', ' '))
            heading_link = heading.lower().replace(' ', '_')
            toc += "* [" + heading + "]" + "(#" + heading_link + ")\n"
        t = self.env.get_template('documentation_toc.jinja')
        return t.render(toc=toc)

    def generate_documentation_header(self, heading, heading_link):
        t = self.env.get_template('documentation_header.jinja')
        return t.render(heading=heading, heading_link=heading_link)

    def generate_documentation_endpoint(self, endpoint, method):
        t = self.env.get_template('documentation_endpoint.jinja')
        title = self.swagger.get_endpoint_short_description(endpoint, method)
        description = self.swagger.get_endpoint_description(endpoint, method)
        api_call = self.generate_api_call(endpoint, method)
        response_codes = self.swagger.get_response_codes(endpoint, method)
        response_code = response_codes[0]
        data = self.swagger.get_example_data(endpoint, method, response_code)
        if data:
            data = data.replace("<img src='cid:ii_139db99fdb5c3704'>", "<img src=[CID GOES HERE]>")
        if self._language == "python":
            try:
                if "true" in data:
                    data = data.replace("true", "True")
                if "false" in data:
                    data = data.replace("false", "False")
            except TypeError, e:
                pass
        query_params = self.swagger.get_query_parameters(endpoint, method)
        params = self.generate_params(response_code, query_params, mock=False)
        url_params = self.generate_url_params(endpoint, None, True)
        return t.render(title=title,
                        description=description,
                        endpoint=endpoint,
                        method_title=method.upper(),
                        method=method,
                        api_call=api_call,
                        params=params,
                        url_params=url_params,
                        data=data
                        )

    def generate_heading_name(self, heading_name):
        #TODO: allow for customizations through the config file
        return heading_name

    def get_raw_class_names(self):
        class_names = {}
        for endpoint in sorted(self.swagger_json["paths"]):
            split_endpoint = endpoint.split('/')
            class_name = split_endpoint[1].capitalize()
            try:
                class_names[class_name].append(endpoint)
            except KeyError, e:
                class_names[class_name] = []
                class_names[class_name].append(endpoint)
        return class_names

###############################################################################
####### GENERATE EXAMPLES
###############################################################################

    def generate_examples(self):
        class_names = self.get_class_names()
        for key in sorted(class_names):
            path = '{0}'.format(os.path.abspath(os.path.dirname(__file__)))
            newpath = '{0}/{1}/generated_files/examples/{2}'.format(path, self._language, key.lower())
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            suffix = ""
            if self._language == "python":
                suffix = ".py"
            if self._language == "php":
                suffix = ".php"
            file = open(str(newpath + '/' + key.lower() + suffix), 'w')
            generated_examples = self.generate_example_title()
            for endpoint in class_names[key]:
                objects = self.swagger.get_endpoint_objects(endpoint)
                for method in objects:
                    if method != "parameters":
                        generated_examples += self.generate_examples_endpoint(endpoint, method)
            file.write(generated_examples.encode('ascii', 'ignore'))
            file.close()
            print generated_examples
        return generated_examples.encode('ascii', 'ignore')

    def generate_example_title(self):
        t = self.env.get_template('examples_header.jinja')
        return t.render()

    def generate_examples_endpoint(self, endpoint, method):
        t = self.env.get_template('examples_endpoint.jinja')
        title = self.swagger.get_endpoint_short_description(endpoint, method)
        description = self.swagger.get_endpoint_description(endpoint, method)
        api_call = self.generate_api_call(endpoint, method)
        response_codes = self.swagger.get_response_codes(endpoint, method)
        response_code = response_codes[0]
        data = self.swagger.get_example_data(endpoint, method, response_code)
        if data:
            data = data.replace("<img src='cid:ii_139db99fdb5c3704'>", "<img src=[CID GOES HERE]>")
        if self._language == "python":
            try:
                if "true" in data:
                    data = data.replace("true", "True")
                if "false" in data:
                    data = data.replace("false", "False")
            except TypeError, e:
                pass
        query_params = self.swagger.get_query_parameters(endpoint, method)
        params = self.generate_params(response_code, query_params, mock=False)
        url_params = self.generate_url_params(endpoint)
        return t.render(title=title,
                        description=description,
                        endpoint=endpoint,
                        method_title=method.upper(),
                        method=method,
                        api_call=api_call,
                        params=params,
                        url_params=url_params,
                        data=data
                        )

###############################################################################
####### UTILITY FUNCTIONS
###############################################################################

    # Used in tests and examples
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

    # Used in tests, docs and examples
    # params should be formatted like: {"hello": "world", "bye": 2}
    def generate_params(self, response_code, params=None, mock=None):
        all_params = {}
        if mock:
            if response_code == "default":
                all_params["mock"] = 0 # Means the response code is undefined in swagger
            else:
                all_params["mock"] = int(response_code)
        if params:
            for param in params:
                all_params[param] = params[param]
        if all_params == {}:
            all_params = None
        if (self._language == "php") and (all_params != None):
            all_params = json.dumps(all_params)
        return all_params

    # Used in tests, docs and examples
    def generate_url_params(self, endpoint, value=None, docs=None):
        if value == None:
            value = "test_url_param"
            #TODO: grab these from stoplight, can override with config
        if endpoint.count('{') < 1:
            return None
        elif endpoint.count('{') == 1:
            if self._language == "python":
                return endpoint.split('{', 1)[-1].split('}')[0] + " = " + "\"" + value + "\""
            if self._language == "php":
                return "$" + endpoint.split('{', 1)[-1].split('}')[0] + " = " + "\"" + value + "\""
        else:
            split_endpoint = endpoint.split('{')
            if self._language == "python":
                url_params = split_endpoint[1].split('}')[0] + " = " + "\"" + value + "\"\n"
                url_params += "        " + split_endpoint[2].split('}')[0] + " = " + "\"" + value + "\""
            if self._language == "php":
                url_params = "$" + split_endpoint[1].split('}')[0] + " = " + "\"" + value + "\";\n"
                if docs:
                    url_params += "$" + split_endpoint[2].split('}')[0] + " = " + "\"" + value + "\""
                else:
                    url_params += "        $" + split_endpoint[2].split('}')[0] + " = " + "\"" + value + "\""
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