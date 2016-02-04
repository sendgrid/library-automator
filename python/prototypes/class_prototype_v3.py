"""
Using the template endpoint as an example:
/templates
/templates/{template_id}
/templates/{template_id}/versions
/templates/{template_id}/versions/{version_id}
/templates/{template_id}/versions/{version_id}/activate
"""

class Templates(object):
    
    def __init__(self):
        pass
    
    def get(self, template_id=None):
        if template_id != None:
            return "Inside Templates Object, ID = " + str(template_id)
        else:
            return "Inside Templates Object"
    
    def versions_get():
        pass
        
    def versions_activate_get()

class Client(object):
    templates = Templates()
    
    def __init__(self):
        pass
        
# Usage
client = Client()
template_id = 1
version_id = 2
print client.templates.get()
print client.templates.get(template_id)
print client.templates.versions.get(template_id, version_id)
print client.templates.versions.activate.get(template_id, version_id)