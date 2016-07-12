import sendgrid
import json
import os


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

##################################################
# Create a Sender Identity #
# POST /v3/senders #

data = {
  "address": "123 Elm St.", 
  "address_2": "Apt. 456", 
  "city": "Denver", 
  "country": "United States", 
  "from": {
    "email": "from@example.com", 
    "name": "Example INC"
  }, 
  "nickname": "My Sender ID", 
  "reply_to": {
    "email": "replyto@example.com", 
    "name": "Example INC"
  }, 
  "state": "Colorado", 
  "zip": "80202"
}
response = sg.client.v3.senders.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Get all Sender Identities #
# GET /v3/senders #

response = sg.client.v3.senders.get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Update a Sender Identity #
# PATCH /v3/senders/{sender_id} #

data = {
  "address": "123 Elm St.", 
  "address_2": "Apt. 456", 
  "city": "Denver", 
  "country": "United States", 
  "from": {
    "email": "from@example.com", 
    "name": "Example INC"
  }, 
  "nickname": "My Sender ID", 
  "reply_to": {
    "email": "replyto@example.com", 
    "name": "Example INC"
  }, 
  "state": "Colorado", 
  "zip": "80202"
}
sender_id = "test_url_param"
response = sg.client.v3.senders._(sender_id).patch(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# View a Sender Identity #
# GET /v3/senders/{sender_id} #

sender_id = "test_url_param"
response = sg.client.v3.senders._(sender_id).get()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Delete a Sender Identity #
# DELETE /v3/senders/{sender_id} #

sender_id = "test_url_param"
response = sg.client.v3.senders._(sender_id).delete()
print(response.status_code)
print(response.body)
print(response.headers)

##################################################
# Resend Sender Identity Verification #
# POST /v3/senders/{sender_id}/resend_verification #

sender_id = "test_url_param"
response = sg.client.v3.senders._(sender_id).resend_verification.post()
print(response.status_code)
print(response.body)
print(response.headers)

