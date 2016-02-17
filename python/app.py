from code_generator import CodeGenerator
from swagger import Swagger
import json

code_generator = CodeGenerator()
swagger = Swagger()
class_names = code_generator.get_class_names()
generated_test_class = code_generator.generate_test_class_header()

for key in sorted(class_names): # Loop through all sorted endpoints
    if key == "ApiKeys":
        for endpoint in class_names[key]: 
            # print key + ": " + endpoint # Print all sorted endpoints
            objects = swagger.get_endpoint_objects(endpoint)
            for method in objects:
                if method != "parameters":
                    test_name = code_generator.generate_test_name(endpoint, method)
                    # print test_name
                    response_codes = swagger.get_response_codes(endpoint, method)
                    response_code = response_codes[0]
                    data = swagger.get_example_data(endpoint, method, response_code)
                    if data != None:
                        data = json.dumps(data)
                    api_call = code_generator.generate_api_call(endpoint, method)
                    # params = code_generator.generate_params(response_code, {"hello": "world", "bye": 2})
                    params = code_generator.generate_params(response_code)
                    url_params = code_generator.generate_url_params(endpoint)
                    # print response_code
                    #TODO: get from config
                    test_id="test_id"
                    generated_test_class += code_generator.generate_test_class_function(test_name,
                                                                                        endpoint, 
                                                                                        method,
                                                                                        response_code,
                                                                                        api_call,
                                                                                        test_id=None,
                                                                                        params=params,
                                                                                        url_params=url_params,
                                                                                        data=data
                                                                                        )

"""
init = False
for key in sorted(class_names):
    for endpoint in class_names[key]:
        #API Keys
        if key == "ApiKeys" and endpoint == "/api_keys":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "api_key_id"
            methods = ['post', 'get', 'get_specific', 'patch', 'put', 'delete_specific']
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods)
        
        #API Key Permissions
        init = False
        mocked_methods = None
        if key == "Scopes" and endpoint == "/scopes":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = ""
            methods = ['get']
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods)          
        
        #Bounces API
        init = False
        mocked_methods = None
        if key == "Suppression" and endpoint == "/suppression/bounces":
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "email"
            methods = ['get', 'get_specific', 'delete', 'delete_specific']
            mocked_methods = ['delete', 'delete_specific']
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods, mocked_methods)
        
        #Transactional Templates        
        init = False
        mocked_methods = None
        if key == "Templates" and endpoint == "/templates":
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "template_id"
            methods = ['post', 'get', 'get_specific', 'patch', 'delete_specific']
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods)
            
        #Campaigns       
        init = False
        mocked_methods = None
        if key == "Campaigns" and endpoint == "/campaigns":
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "campaign_id"
            methods = ['post', 'get', 'get_specific', 'patch', 'delete_specific']
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods)
        if key == "Campaigns" and endpoint == "/campaigns/{campaign_id}/schedules/now":
            init = True
            mocked_methods = None
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "campaign_id"
            methods = ['post']
            mocked_methods = ['post']
            end = "now"
            appended_endpoint = code_generator.config.get_appended_endpoint(base_endpoint, end)
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods, mocked_methods, appended_endpoint)
        if key == "Campaigns" and endpoint == "/campaigns/{campaign_id}/schedules":
            init = True
            mocked_methods = None
            class_name = key
            base_endpoint = endpoint.split("/")[1]
            endpoint_id = "campaign_id"
            methods = ['get', 'post', 'patch', 'delete']
            mocked_methods = ['get', 'post', 'patch', 'delete']
            end = "schedules"
            appended_endpoint = code_generator.config.get_appended_endpoint(base_endpoint, end)
            generated_test_class += code_generator.build_test(init, key, base_endpoint, endpoint, endpoint_id, methods, mocked_methods, appended_endpoint, end)
"""
print generated_test_class