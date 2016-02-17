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

    def generate_class(self, 
                    class_name, 
                    class_description, 
                    class_constructor_definition, 
                    base_endpoint
                    ):
        t = self.env.get_template('endpoint_class.jinja')
        return t.render(class_name = class_name,
                        class_description = class_description,
                        class_constructor_definition = class_constructor_definition,
                        base_endpoint = base_endpoint
                        )

    def generate_test_class_header(self):
        t = self.env.get_template('test_header.jinja')
        return t.render()
    
    def generate_test_class_init(self, 
                                class_name, 
                                base_endpoint,
                                test_id,
                                custom_init,
                                custom_class_name=None,
                                init_id_value=None,
                                proxy_url=None,
                                final_endpoint=None,
                                full_endpoint_path=None
                                ):
        t = self.env.get_template('test_class_init.jinja')
        if custom_class_name:
            class_name = custom_class_name #TODO:config this
        return t.render(class_name = class_name, 
                        base_endpoint = base_endpoint,
                        test_id = test_id,
                        custom_init = custom_init,
                        init_id_value = init_id_value,
                        proxy_url = proxy_url,
                        final_endpoint = final_endpoint,
                        full_endpoint_path = full_endpoint_path
                        )

    def build_test(self, init, class_name, base_endpoint, endpoint, endpoint_id, methods, mocked_methods=None, appended_endpoint=None, end=None):
        generated_test_class = ""
        test_id = self.config.get_id(base_endpoint)
        if init == False:
            self._test_count = 0
            custom_init = self.config.get_custom_init(base_endpoint)
            custom_init = custom_init.translate(None, '"')
            custom_class_name = self.config.get_custom_class_name(base_endpoint)
            init_id_value = self.config.get_init_id_value(base_endpoint)
            if self.config.is_proxied():
                proxy_url = self.config.get_proxy_url()
            else:
                proxy_url = None
            final_endpoint = self.config.get_final_endpoint(base_endpoint)
            full_endpoint_path = self.config.get_full_endpoint_path(base_endpoint)
            if final_endpoint:
                base_endpoint = final_endpoint
            generated_test_class += self.generate_test_class_init(class_name, 
                                                                            base_endpoint, 
                                                                            test_id, 
                                                                            custom_init, 
                                                                            custom_class_name, 
                                                                            init_id_value,
                                                                            proxy_url,
                                                                            final_endpoint,
                                                                            full_endpoint_path,
                                                                            )
            init = True
        try:
            if "post" in methods:
                test_number = self.test_count_to_string()
                method = "post"
                try:
                    if "post" in mocked_methods:
                        params = self.config.get_mocked_params(base_endpoint, "post")
                        j = json.loads(params)
                        response_code = j['mock']
                        specific = True
                        data = None
                    else:
                        params = self.config.get_params(base_endpoint)
                        response_codes = self.swagger.get_response_codes(endpoint, method)
                        response_code = response_codes[0]
                        data = self.config.get_data(base_endpoint)
                        specific = False
                except TypeError, e:
                    params = self.config.get_params(base_endpoint)
                    response_codes = self.swagger.get_response_codes(endpoint, method)
                    response_code = response_codes[0]
                    data = self.config.get_data(base_endpoint)
                    specific = False
            
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_code,
                                                                        test_id = test_id,
                                                                        data = data,
                                                                        params = params,
                                                                        specific = specific,
                                                                        appended_endpoint = appended_endpoint
                                                                        )
                self.test_count += 1
            if "get" in methods:
                response_code = ""
                params = None
                specific = None
                test_number = self.test_count_to_string()
                method = "get"
                try:
                    if "get" in mocked_methods:
                        params = self.config.get_mocked_params(base_endpoint, "get")
                        j = json.loads(params)
                        response_code = j['mock']
                        specific = True
                        data = None
                    else:
                        params = self.config.get_params(base_endpoint)
                        response_codes = self.swagger.get_response_codes(endpoint, method)
                        response_code = response_codes[0]
                        data = self.config.get_data(base_endpoint)
                        specific = False
                except TypeError, e:
                    params = self.config.get_params(base_endpoint)
                    response_codes = self.swagger.get_response_codes(endpoint, method)
                    response_code = response_codes[0]
                    data = self.config.get_data(base_endpoint)
                    specific = False
                    
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_code,
                                                                        test_id = test_id,
                                                                        params = params,
                                                                        specific = specific,
                                                                        appended_endpoint = appended_endpoint
                                                                        )
                self.test_count += 1
            if "get_specific" in methods:
                test_number = self.test_count_to_string()
                method = "get"
                endpoint_post = self.swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                specific = True
                params = self.config.get_params(base_endpoint)
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        params = params,
                                                                        specific = specific
                                                                        )
                self.test_count += 1
            if "patch" in methods:
                test_number = self.test_count_to_string()
                method = "patch"
                try:
                    if "patch" in mocked_methods:
                        params = self.config.get_mocked_params(base_endpoint, "patch")
                        j = json.loads(params)
                        response_code = j['mock']
                        specific = True
                        data = None
                    else:
                        params = self.config.get_params(base_endpoint)
                        response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                        response_code = response_codes[0]
                        specific = False
                except TypeError, e:
                    params = self.config.get_params(base_endpoint)
                    response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                    response_code = response_codes[0]
                    specific = False
                
                if appended_endpoint:
                    data = self.config.get_patched_params_appended(end)
                else:
                    data = self.config.get_data(base_endpoint)
                       
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_code,
                                                                        test_id = test_id,
                                                                        data = data,
                                                                        params = params,
                                                                        appended_endpoint = appended_endpoint
                                                                        )
                self.test_count += 1
            if "put" in methods:
                test_number = self.test_count_to_string()
                method = "put"
                data = self.config.get_put_data(base_endpoint)
                params = self.config.get_params(base_endpoint)
                endpoint_post = self.swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data,
                                                                        params = params
                                                                        )
                self.test_count += 1
            if "delete" in methods:
                test_number = self.test_count_to_string()
                method = "delete"
                try:
                    if "delete" in mocked_methods:
                        params = self.config.get_mocked_params(base_endpoint, "delete")
                        j = json.loads(params)
                        response_code = j['mock']
                        specific = True
                    else:
                        params = self.config.get_params(base_endpoint)
                        response_codes = self.swagger.get_response_codes(endpoint, method)
                        response_code = response_codes[0]
                        specific = False
                except TypeError, e:
                    params = self.config.get_params(base_endpoint)
                    response_codes = self.swagger.get_response_codes(endpoint, method)
                    response_code = response_codes[0]
                    specific = False
                    
                if appended_endpoint:
                    data = self.config.get_patched_params_appended(end)
                else:
                    data = self.config.get_data(base_endpoint)

                endpoint_post = self.swagger.get_endpoint_object(endpoint, method)
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_code,
                                                                        test_id = test_id,
                                                                        params = params,
                                                                        specific = specific,
                                                                        appended_endpoint = appended_endpoint
                                                                        )
                self.test_count += 1
            if "delete_specific" in methods:
                test_number = self.test_count_to_string()
                method = "delete"
                try:
                    if "delete_specific" in mocked_methods:
                        params = self.config.get_mocked_params(base_endpoint, "delete_specific")
                        j = json.loads(params)
                        response_code = j['mock']
                    else:
                        params = self.config.get_params(base_endpoint)
                        response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                        response_code = response_codes[0]
                except TypeError, e:
                    params = self.config.get_params(base_endpoint)
                    response_codes = self.swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                    response_code = response_codes[0]
                endpoint_post = self.swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                specific = True
                generated_test_class += self.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_code,
                                                                        test_id = test_id,
                                                                        params = params,
                                                                        specific = specific
                                                                        )
                self.test_count += 1
            return generated_test_class 
        except KeyError, e:
            return None
    
    def generate_test_class_function(self, 
                                    test_name,
                                    endpoint, 
                                    method,
                                    response_code,
                                    api_call,
                                    test_id=None,
                                    data=None,
                                    params=None,
                                    url_params=None,
                                    specific=False,
                                    appended_endpoint=None
                                    ):
        t = self.env.get_template('test_class_function.jinja')
        return t.render(test_name = test_name,
                        endpoint = endpoint,
                        method = method,
                        response_code = response_code,
                        api_call = api_call,
                        test_id = test_id,
                        data = data,
                        params = params,
                        url_params = url_params,
                        specific = specific,
                        appended_endpoint = appended_endpoint
                        )
    
    def generate_delete_endpoint(self, function_description, params):
        t = self.env.get_template('delete_function.jinja')
        return t.render(function_description = function_description,
                params = params,
                endpoint = "\"/" + params + "\""
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
       return endpoint + "." + method
       
    def generate_params(self, response_code, params=None):
        all_params = {}
        all_params["mock"] = int(response_code)
        if params != None:
            for param in params:
                all_params[param] = params[param]
        return all_params

    def generate_url_params(self, endpoint, value=None):
        if value == None:
            value = "test_url_param"
        if endpoint.count('{') < 1:
            return None
        elif endpoint.count('{') == 1:
            return endpoint.split('{', 1)[-1][:-1] + " = " + "\"" + value + "\""
        else:
            return None    
    
    def get_description(self, method, key):
        return self.swagger_json["paths"][key][method]["description"]
    
    def get_summary(self, method, key):
        return self.swagger_json["paths"][key][method]["summary"]
    
    def get_operation_id(self, method, key):
        return self.swagger_json["paths"][key][method]["operationId"]

    def test_count_to_string(self):
        if self._test_count < 9:
            return "0" + str(self._test_count)
        return str(self._test_count)
    
    @property
    def env(self):
        return self._env

    @property
    def swagger_json(self):
        return self._swagger_json

    @property
    def test_count(self):
        return self._test_count

    @test_count.setter
    def test_count(self, value):
        self._test_count = value

    @property
    def config(self):
        return self._config
        
    @property
    def swagger(self):
        return self._swagger