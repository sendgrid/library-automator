"""
Using the template endpoint as an example:
/templates
/templates/{template_id}
/templates/{template_id}/versions
/templates/{template_id}/versions/{version_id}
/templates/{template_id}/versions/{version_id}/activate
"""

client.templates.get()
client.templates.get(template_id)
client.templates.versions.get(template_id, version_id)
client.templates.versions.activate.get(template_id, version_id)

# We can also have three parameters be passed
# url_params = list
# query_params = list
# headers = list
client.templates.get()
url_params = [template_id]
client.templates.get(url_params)
url_params = [template_id, version_id]
client.templates.versions.get(url_params)
client.templates.versions.activate.get(url_params)

# or how about having the url params embedded like this:
client.templates._template_id.versions._version_id.activate.get(url_params)