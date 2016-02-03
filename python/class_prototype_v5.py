"""
Using the template endpoint as an example:
/templates
/templates/{template_id}
/templates/{template_id}/versions
/templates/{template_id}/versions/{version_id}
/templates/{template_id}/versions/{version_id}/activate
"""

client.templates.get()
client.templates['template_id'].get()
client.templates['template_id'].versions.get()
client.templates['template_id'].versions['versions_id'].get()

https://github.com/inueni/birdy#ok-im-sold-but-how-do-i-use-it-how-does-this-dynamic-api-construction-work