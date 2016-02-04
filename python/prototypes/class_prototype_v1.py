"""
Using the template endpoint as an example:
/templates
/templates/{template_id}
/templates/{template_id}/versions
/templates/{template_id}/versions/{version_id}
/templates/{template_id}/versions/{version_id}/activate
"""

class Templates(object):
    versions = Versions()
    
    def __init__(self):
        pass
    
    def get(self, template_id=None):
        if template_id != None:
            return "Inside Templates Object, ID = " + str(template_id)
        else:
            return "Inside Templates Object"
            
class Versions(Templates):
    def __init__(self):
        pass

    def get(self, template_id=None, version_id=None):
        if template_id != None and version_id != None:
            return "Inside Versions Object, ID = " + str(template_id) + ", Version ID: " + str(version_id)
        else:
            return "Inside Versions Object"
    
class Activate(Versions):
    def __init__(self):
        pass

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
print client.templates.versions(template_id, version_id)
#print client.templates.versions.activate(template_id, version_id)