import github3
import os
import base64
import json
from jinja2 import Environment, FileSystemLoader

base_path = os.path.abspath(os.path.dirname(__file__))
if os.path.exists(base_path + '/.env'):
    for line in open(base_path + '/.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]
github_token = os.environ.get('GITHUB_TOKEN')
gh = github3.login(token=github_token)
repo = gh.repository('sendgrid', 'sendgrid-swagger')

#Get swagger
content = repo.contents('swagger-stoplight.json')
swagger = base64.b64decode(content.content)
swagger_json = json.loads(swagger)

print "=================================================================================================="
print "All Endpoints:\n"
print "=================================================================================================="

#Get all endpoints
for key in sorted(swagger_json["paths"]):
    print(key)
    
#Get all DELETE objects
delete_objects = {}
for key in swagger_json["paths"]:
    try:
        delete_objects[key] = swagger_json["paths"][key]["delete"]
    except KeyError, e:
        pass

print "=================================================================================================="
print "DELETE Endpoints:\n"
print "=================================================================================================="

#Print all DELETE endpoints     
for key in sorted(delete_objects):
    print key

print "=================================================================================================="
print "DELETE Endpoints with their Objects:\n"
print "=================================================================================================="

#Print all DELETE endpoints and their objects
for key in sorted(delete_objects):
    print key
    print "\n"
    print delete_objects[key]
    print "\n"

print "=================================================================================================="
print "Grouped by URL:\n"
print "=================================================================================================="

#Group by URL
for key in sorted(swagger_json["paths"]):
    k = key.split('/')
    for i in k:
        print i # Separated URL
    for i in k:
        if '{' in i:
            print i # URI parameters

print "=================================================================================================="
print "Generated Class:\n"
print "=================================================================================================="
      
env = Environment(loader=FileSystemLoader('templates'))
t = env.get_template('api_keys.jinja')
print t.render(class_name = "APIKeys",
         class_description = "The API Keys feature allows customers to be able to generate an API Key credential\n    which can be used for authentication with the SendGrid v3 Web API or the Mail API Endpoint",
         class_constructor_definition = "Constructs SendGrid APIKeys object.",
         url_to_documentation = "https://sendgrid.com/docs/API_Reference/Web_API_v3/API_Keys/index.html",
         base_endpoint = "api_keys",
         function_description = "Delete a API key",
         params = "api_key_id", # TODO: cover the case of multiple params
         endpoint = "api_key_id"
         )