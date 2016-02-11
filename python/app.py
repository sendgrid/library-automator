from code_generator import CodeGenerator
from swagger import Swagger
from config import Config
import json

swagger = Swagger()
code_generator = CodeGenerator(swagger.swagger_json)
config = Config()

endpoints = swagger.get_endpoints()
delete_endpoints = swagger.get_endpoints("delete")
delete_objects = {}
for endpoint in delete_endpoints:
    delete_objects[endpoint] = swagger.get_endpoint_object(endpoint, "delete")
class_names = code_generator.get_class_names()

print "=================================================================================================="
print "All Endpoints:"
print "==================================================================================================\n"

for endpoint in endpoints:
    print endpoint
    endpoint_objects = swagger.get_endpoint_objects(endpoint)
    for key in endpoint_objects.keys():
        if key != 'parameters':
            print key

print "\n=================================================================================================="
print "Generated Test Class:"
print "==================================================================================================\n"

def build_test(init, class_name, base_endpoint, endpoint_id, methods, mocked_methods=None):
    generated_test_class = ""
    if init == "false":
        test_id = config.get_id(base_endpoint)
        custom_init = config.get_custom_init(base_endpoint)
        custom_init = custom_init.translate(None, '"')
        custom_class_name = config.get_custom_class_name(base_endpoint)
        init_id_value = config.get_init_id_value(base_endpoint)
        if config.is_proxied():
            proxy_url = config.get_proxy_url()
        else:
            proxy_url = None
        final_endpoint = config.get_final_endpoint(base_endpoint)
        full_endpoint_path = config.get_full_endpoint_path(base_endpoint)
        if final_endpoint:
            base_endpoint = final_endpoint
        generated_test_class += code_generator.generate_test_class_init(class_name, 
                                                                        base_endpoint, 
                                                                        test_id, 
                                                                        custom_init, 
                                                                        custom_class_name, 
                                                                        init_id_value,
                                                                        proxy_url,
                                                                        final_endpoint,
                                                                        full_endpoint_path
                                                                        )
        init = "true"
    try:
        if "post" in methods:
            test_number = "00"
            method = "post"
            data = config.get_data(base_endpoint)
            params = config.get_params(base_endpoint)
            endpoint_post = swagger.get_endpoint_object(endpoint, method)
            response_codes = swagger.get_response_codes(endpoint, method)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_codes[0],
                                                                    test_id = test_id,
                                                                    data = data,
                                                                    params = params
                                                                    )
        if "get" in methods:
            test_number = "01"
            method = "get"
            endpoint_post = swagger.get_endpoint_object(endpoint, method)
            response_codes = swagger.get_response_codes(endpoint, method)
            params = config.get_params(base_endpoint)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_codes[0],
                                                                    params = params
                                                                    )
        if "get_specific" in methods:
            test_number = "02"
            method = "get"
            endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
            response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
            specific = True
            params = config.get_params(base_endpoint)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_codes[0],
                                                                    test_id = test_id,
                                                                    params = params,
                                                                    specific = specific
                                                                    )
        if "patch" in methods:
            test_number = "03"
            method = "patch"
            data = config.get_patched_data(base_endpoint)
            params = config.get_params(base_endpoint)
            endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
            response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_codes[0],
                                                                    test_id = test_id,
                                                                    data = data,
                                                                    params = params
                                                                    )
        if "put" in methods:
            test_number = "04"
            method = "put"
            data = config.get_put_data(base_endpoint)
            params = config.get_params(base_endpoint)
            endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
            response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_codes[0],
                                                                    test_id = test_id,
                                                                    data = data,
                                                                    params = params
                                                                    )
        if "delete" in methods:
            test_number = "05"
            method = "delete"
            try:
                if "delete" in mocked_methods:
                    params = config.get_mocked_params(base_endpoint, "delete")
                    j = json.loads(params)
                    response_code = j['mock']
            except TypeError, e:
                params = config.get_params(base_endpoint)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                response_code = response_codes[0]
            endpoint_post = swagger.get_endpoint_object(endpoint, method)
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_code,
                                                                    params = params
                                                                    )
        if "delete_specific" in methods:
            test_number = "06"
            method = "delete"
            try:
                if "delete_specific" in mocked_methods:
                    params = config.get_mocked_params(base_endpoint, "delete_specific")
                    j = json.loads(params)
                    response_code = j['mock']
            except TypeError, e:
                params = config.get_params(base_endpoint)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                response_code = response_codes[0]
            endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
            specific = True
            generated_test_class += code_generator.generate_test_class_function(
                                                                    test_number = test_number, 
                                                                    endpoint = base_endpoint, 
                                                                    method = method,
                                                                    response_code = response_code,
                                                                    test_id = test_id,
                                                                    params = params,
                                                                    specific = specific
                                                                    )
        return generated_test_class
    except KeyError, e:
        pass

generated_test_class = code_generator.generate_test_class_header()
init = "false"
for key in sorted(class_names):
    for endpoint in class_names[key]:
        #API Keys
        if key == "ApiKeys" and endpoint == "/api_keys":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "api_key_id"
            methods = ['post', 'get', 'get_specific', 'patch', 'put', 'delete_specific']
            generated_test_class += build_test(init, key, base_endpoint, endpoint_id, methods)
        
        #API Key Permissions
        init = "false"
        if key == "Scopes" and endpoint == "/scopes":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = ""
            methods = ['get']
            generated_test_class += build_test(init, key, base_endpoint, endpoint_id, methods)          
        
        #Bounces API
        init = "false"
        if key == "Suppression" and endpoint == "/suppression/bounces":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "email"
            methods = ['get', 'get_specific', 'delete', 'delete_specific']
            mocked_methods = ['delete', 'delete_specific']
            generated_test_class += build_test(init, key, base_endpoint, endpoint_id, methods, mocked_methods)
        
        #Transactional Templates        
        init = "false"
        if key == "Templates" and endpoint == "/templates":
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "template_id"
            methods = ['post', 'get', 'get_specific', 'patch', 'delete_specific']
            generated_test_class += build_test(init, key, base_endpoint, endpoint_id, methods)

print generated_test_class