import github3
import os
import base64
import json

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

#Get all endpoints
for key in swagger_json["paths"]:
    print(key)
    
#Get all DELETE objects
delete_objects = {}
for key in swagger_json["paths"]:
    try:
        delete_objects[key] = swagger_json["paths"][key]["delete"]
    except KeyError, e:
        pass

#Print all DELETE endpoints     
for key in delete_objects:
    print key
    
#Print all DELETE endpoints and their objects
for key in delete_objects:
    print key
    print "\n"
    print delete_objects[key]
    print "\n"
