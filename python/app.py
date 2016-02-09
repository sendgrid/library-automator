from code_generator import CodeGenerator
from swagger import Swagger
from config import Config

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
print "DELETE Endpoints:"
print "==================================================================================================\n"

for endpoint in delete_endpoints:
    print endpoint

print "\n=================================================================================================="
print "DELETE Endpoints with their Objects:"
print "==================================================================================================\n"

for key in sorted(delete_objects):
    print key
    print "\n"
    print delete_objects[key]
    print "\n"

print "\n=================================================================================================="
print "Generated Test Class:"
print "==================================================================================================\n"

generated_test_class = code_generator.generate_test_class_header()
init = "false"
for key in sorted(class_names):
    for endpoint in class_names[key]:
        if key == "ApiKeys" and endpoint == "/api_keys":
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            if init == "false":
                test_id = config.get_id(base_endpoint)
                endpoint_id = "api_key_id"
                custom_init = config.get_custom_init(base_endpoint)
                custom_init = custom_init.translate(None, '"')
                generated_test_class += code_generator.generate_test_class_init(class_name, base_endpoint, test_id, custom_init)
                init = "true"
            try:
                test_number = "00"
                method = "post"
                data = config.get_data(base_endpoint)
                endpoint_post = swagger.get_endpoint_object(endpoint, method)
                response_codes = swagger.get_response_codes(endpoint, method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data
                                                                        )
                test_number = "01"
                method = "get"
                endpoint_post = swagger.get_endpoint_object(endpoint, method)
                response_codes = swagger.get_response_codes(endpoint, method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0]
                                                                        )
                test_number = "02"
                method = "get"
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                specific = True
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        specific = specific
                                                                        )
                test_number = "03"
                method = "patch"
                data = config.get_patched_data(base_endpoint)
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data
                                                                        )
                test_number = "04"
                method = "put"
                data = config.get_put_data(base_endpoint)
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data
                                                                        )
                test_number = "05"
                method = "delete"
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[1],
                                                                        test_id = test_id
                                                                        )
            except KeyError, e:
                pass
                
        init = "false"
        if key == "Templates" and endpoint == "/templates":
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            if init == "false":
                test_id = config.get_id(base_endpoint)
                endpoint_id = "template_id"
                custom_init = config.get_custom_init(base_endpoint)
                custom_init = custom_init.translate(None, '"')
                generated_test_class += code_generator.generate_test_class_init(class_name, base_endpoint, test_id, custom_init)
                init = "true"
            try:
                test_number = "00"
                method = "post"
                data = config.get_data(base_endpoint)
                endpoint_post = swagger.get_endpoint_object(endpoint, method)
                response_codes = swagger.get_response_codes(endpoint, method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data
                                                                        )
                test_number = "01"
                method = "get"
                endpoint_post = swagger.get_endpoint_object(endpoint, method)
                response_codes = swagger.get_response_codes(endpoint, method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0]
                                                                        )
                test_number = "02"
                method = "get"
                
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                specific = True
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        specific = specific
                                                                        )
                test_number = "03"
                method = "patch"
                data = config.get_patched_data(base_endpoint)
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id,
                                                                        data = data
                                                                        )
                test_number = "04"
                method = "delete"
                endpoint_post = swagger.get_endpoint_object(endpoint + "/{" + endpoint_id + "}", method)
                response_codes = swagger.get_response_codes(endpoint + "/{" + endpoint_id + "}", method)
                generated_test_class += code_generator.generate_test_class_function(
                                                                        test_number = test_number, 
                                                                        endpoint = base_endpoint, 
                                                                        method = method,
                                                                        response_code = response_codes[0],
                                                                        test_id = test_id
                                                                        )
            except KeyError, e:
                pass
print generated_test_class