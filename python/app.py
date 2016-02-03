from code_generator import CodeGenerator
from swagger import Swagger

swagger = Swagger()
code_generator = CodeGenerator(swagger.swagger_json)

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
print "Generated Classes (APIKeys for first example):"
print "==================================================================================================\n"

for key in sorted(class_names):
    for endpoint in class_names[key]:
        if endpoint in delete_objects:
            if key == "ApiKeys":
                class_name = key
                class_description = code_generator.get_description("get", "/" + endpoint.split("/")[1]) # TODO: conform to PEP 8 rules for line length
                class_constructor_definition = "Contructs the SendGrid " + key + " object."
                base_endpoint = endpoint.split("/")[1]
                generated_class = code_generator.generate_class(class_name, class_description, class_constructor_definition, base_endpoint)
                function_description = code_generator.get_operation_id("delete", endpoint)
                params = endpoint.split("/")[2].strip("{}")
                # TODO: Implement https://github.com/sendgrid/sendgrid-python/blob/master/sendgrid/resources/asm_suppressions.py to cover case with multiple parameters
                generated_class += code_generator.generate_delete_endpoint(function_description, params)
print generated_class