import sendgrid
import json
import os

sg = sendgrid.SendGridAPIClient()

##################################################
# Create a batch ID #
# POST /mail/batch #

data = {'sample': 'data'}
response = self.sg.client.mail.batch.post(request_body=data)
print(response.status_code)
print(response.response_body)
print(response.response_headers)

##################################################
# Validate batch ID #
# GET /mail/batch/{batch_id} #

batch_id = "test_url_param"
response = self.sg.client.mail.batch._(batch_id).get()
print(response.status_code)
print(response.response_body)
print(response.response_headers)

