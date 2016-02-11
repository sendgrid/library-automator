import re
from jinja2 import Environment, FileSystemLoader

class CodeGenerator(object):
    def __init__(self, swagger_json):
        self._env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
        self._swagger_json = swagger_json

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
    def generate_test_class_function(self, 
                                    test_number, 
                                    endpoint, 
                                    method,
                                    response_code,
                                    test_id=None,
                                    data=None,
                                    params=None,
                                    specific=False
                                    ):
        t = self.env.get_template('test_class_function.jinja')
        return t.render(test_number = test_number, 
                        endpoint = endpoint,
                        method = method,
                        response_code = response_code,
                        test_id = test_id,
                        data = data,
                        params = params,
                        specific = specific
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

    def get_description(self, method, key):
        return self.swagger_json["paths"][key][method]["description"]
    
    def get_summary(self, method, key):
        return self.swagger_json["paths"][key][method]["summary"]
    
    def get_operation_id(self, method, key):
        return self.swagger_json["paths"][key][method]["operationId"]

    @property
    def env(self):
        return self._env

    @property
    def swagger_json(self):
        return self._swagger_json