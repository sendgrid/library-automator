require 'sendgrid-ruby'


sg = SendGrid::API.new(api_key: ENV['SENDGRID_API_KEY'])

##################################################
# Create a Custom Field #
# POST /contactdb/custom_fields #

data = JSON.parse('{
  "name": "pet", 
  "type": "text"
}')
response = sg.client.contactdb.custom_fields.post(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve all custom fields #
# GET /contactdb/custom_fields #

response = sg.client.contactdb.custom_fields.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve a Custom Field #
# GET /contactdb/custom_fields/{custom_field_id} #

custom_field_id = "test_url_param"
response = sg.client.contactdb.custom_fields._(custom_field_id).get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete a Custom Field #
# DELETE /contactdb/custom_fields/{custom_field_id} #

custom_field_id = "test_url_param"
response = sg.client.contactdb.custom_fields._(custom_field_id).delete()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Create a List #
# POST /contactdb/lists #

data = JSON.parse('{
  "name": "your list name"
}')
response = sg.client.contactdb.lists.post(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve all lists #
# GET /contactdb/lists #

response = sg.client.contactdb.lists.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete Multiple lists #
# DELETE /contactdb/lists #

response = sg.client.contactdb.lists.delete(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Update a List #
# PATCH /contactdb/lists/{list_id} #

data = JSON.parse('{
  "name": "newlistname"
}')
params = JSON.parse('{"list_id": 0}')
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).patch(request_body: data, query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve a single list #
# GET /contactdb/lists/{list_id} #

params = JSON.parse('{"list_id": 0}')
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete a List #
# DELETE /contactdb/lists/{list_id} #

params = JSON.parse('{"delete_contacts": "true"}')
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).delete(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Add Multiple Recipients to a List #
# POST /contactdb/lists/{list_id}/recipients #

data = JSON.parse('[
  "recipient_id1", 
  "recipient_id2"
]')
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients.post(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve all recipients on a List #
# GET /contactdb/lists/{list_id}/recipients #

params = JSON.parse('{"page": 1, "page_size": 1, "list_id": 0}')
list_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients.get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Add a Single Recipient to a List #
# POST /contactdb/lists/{list_id}/recipients/{recipient_id} #

list_id = "test_url_param"
        recipient_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients._(recipient_id).post()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete a Single Recipient from a Single List #
# DELETE /contactdb/lists/{list_id}/recipients/{recipient_id} #

params = JSON.parse('{"recipient_id": 0, "list_id": 0}')
list_id = "test_url_param"
        recipient_id = "test_url_param"
response = sg.client.contactdb.lists._(list_id).recipients._(recipient_id).delete(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Update Recipient #
# PATCH /contactdb/recipients #

data = JSON.parse('[
  {
    "email": "jones@example.com", 
    "first_name": "Guy", 
    "last_name": "Jones"
  }
]')
response = sg.client.contactdb.recipients.patch(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Add recipients #
# POST /contactdb/recipients #

data = JSON.parse('[
  {
    "age": 25, 
    "email": "example@example.com", 
    "first_name": "", 
    "last_name": "User"
  }, 
  {
    "age": 25, 
    "email": "example2@example.com", 
    "first_name": "Example", 
    "last_name": "User"
  }
]')
response = sg.client.contactdb.recipients.post(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve recipients #
# GET /contactdb/recipients #

params = JSON.parse('{"page": 1, "page_size": 1}')
response = sg.client.contactdb.recipients.get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete Recipient #
# DELETE /contactdb/recipients #

response = sg.client.contactdb.recipients.delete(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve the count of billable recipients #
# GET /contactdb/recipients/billable_count #

response = sg.client.contactdb.recipients.billable_count.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve a Count of Recipients #
# GET /contactdb/recipients/count #

response = sg.client.contactdb.recipients.count.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve recipients matching search criteria #
# GET /contactdb/recipients/search #

params = JSON.parse('{"{field_name}": "test_string"}')
response = sg.client.contactdb.recipients.search.get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve a single recipient #
# GET /contactdb/recipients/{recipient_id} #

recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete a Recipient #
# DELETE /contactdb/recipients/{recipient_id} #

recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).delete()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve the lists that a recipient is on #
# GET /contactdb/recipients/{recipient_id}/lists #

recipient_id = "test_url_param"
response = sg.client.contactdb.recipients._(recipient_id).lists.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve reserved fields #
# GET /contactdb/reserved_fields #

response = sg.client.contactdb.reserved_fields.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Create a Segment #
# POST /contactdb/segments #

data = JSON.parse('{
  "conditions": [
    {
      "and_or": "", 
      "field": "last_name", 
      "operator": "eq", 
      "value": "Miller"
    }, 
    {
      "and_or": "and", 
      "field": "last_clicked", 
      "operator": "gt", 
      "value": "01/02/2015"
    }, 
    {
      "and_or": "or", 
      "field": "clicks.campaign_identifier", 
      "operator": "eq", 
      "value": "513"
    }
  ], 
  "list_id": 4, 
  "name": "Last Name Miller"
}')
response = sg.client.contactdb.segments.post(request_body: data)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve all segments #
# GET /contactdb/segments #

response = sg.client.contactdb.segments.get()
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Update a segment #
# PATCH /contactdb/segments/{segment_id} #

data = JSON.parse('{
  "conditions": [
    {
      "and_or": "", 
      "field": "last_name", 
      "operator": "eq", 
      "value": "Miller"
    }
  ], 
  "list_id": 5, 
  "name": "The Millers"
}')
params = JSON.parse('{"segment_id": "test_string"}')
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).patch(request_body: data, query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve a segment #
# GET /contactdb/segments/{segment_id} #

params = JSON.parse('{"segment_id": 0}')
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Delete a segment #
# DELETE /contactdb/segments/{segment_id} #

params = JSON.parse('{"delete_contacts": "true"}')
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).delete(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

##################################################
# Retrieve recipients on a segment #
# GET /contactdb/segments/{segment_id}/recipients #

params = JSON.parse('{"page": 1, "page_size": 1}')
segment_id = "test_url_param"
response = sg.client.contactdb.segments._(segment_id).recipients.get(query_params: params)
puts response.status_code
puts response.response_body
puts response.response_headers

