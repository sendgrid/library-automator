from code_generator import CodeGenerator

code_generator = CodeGenerator()

class_names = code_generator.get_class_names()

generated_test_class = code_generator.generate_test_class_header()
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

print generated_test_class