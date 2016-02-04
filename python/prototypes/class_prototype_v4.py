"""
Using the template endpoint as an example:
/templates
/templates/{template_id}
/templates/{template_id}/versions
/templates/{template_id}/versions/{version_id}
/templates/{template_id}/versions/{version_id}/activate
"""

client.templates.get()
client.templates.versions.get(template_id, version_id)
client.templates.versions.activate(template_id, version_id)

client.get("/templates/{template_id}", template_id)
client.get("/templates/{template_id}/versions", template_id)
client.get("/templates/{template_id}/versions/{version_id}", template_id, version_id)
client.get("/templates/{template_id}/versions/{version_id}/activate", template_id, version_id)