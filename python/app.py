from code_generator import CodeGenerator
from swagger import Swagger
from config import Config
import json

code_generator = CodeGenerator()
swagger = Swagger()
config = Config()
class_names = code_generator.get_class_names()

if config.is_proxied:
    host = config.proxy_url
else:
    host = config.host
api_key = config.api_key

generated_test_class = code_generator.generate_test_class_header(host=host, api_key=api_key)

for key in sorted(class_names): # Loop through all sorted endpoints, grouped by class name
    for endpoint in class_names[key]: 
        objects = swagger.get_endpoint_objects(endpoint)
        for method in objects:
            if method != "parameters":
                test_name = code_generator.generate_test_name(endpoint, method)
                response_codes = swagger.get_response_codes(endpoint, method)
                response_code = response_codes[0]
                data = swagger.get_example_data(endpoint, method, response_code)
                api_call = code_generator.generate_api_call(endpoint, method)
                params = code_generator.generate_params(response_code)
                url_params = code_generator.generate_url_params(endpoint)
                if response_code != "default": # schema undefined in swagger
                    generated_test_class += code_generator.generate_test_class_function(test_name,
                                                                                        endpoint, 
                                                                                        method,
                                                                                        response_code,
                                                                                        api_call,
                                                                                        params=params,
                                                                                        url_params=url_params,
                                                                                        data=data
                                                                                        )
print generated_test_class