import sendgrid

sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
host = os.environ.get('HOST') # e.g. https://api.sendgrid.com/v3
sg = sendgrid.SendGridAPIClient(sendgrid_api_key, host=host)

##################################################
# Create API keys #
# POST /api_keys #

# data = {'sample': 'data'}
# response = self.sg.client.api_keys.post(data=data)
# print response.status_code
# print response.text

##################################################
# List all API Keys belonging to the authenticated user #
# GET /api_keys #

# response = self.sg.client.api_keys.get()
# print response.status_code
# print response.text

##################################################
# Update the name & scopes of an API Key #
# PUT /api_keys/{api_key_id} #

# data = {'sample': 'data'}
# api_key_id = "test_url_param"
# response = self.sg.client.api_keys._(api_key_id).put(data=data)
# print response.status_code
# print response.text

##################################################
# Update API keys #
# PATCH /api_keys/{api_key_id} #

# data = {'sample': 'data'}
# api_key_id = "test_url_param"
# response = self.sg.client.api_keys._(api_key_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get an existing API Key #
# GET /api_keys/{api_key_id} #

# api_key_id = "test_url_param"
# response = self.sg.client.api_keys._(api_key_id).get()
# print response.status_code
# print response.text

##################################################
# Delete API keys #
# DELETE /api_keys/{api_key_id} #

# api_key_id = "test_url_param"
# response = self.sg.client.api_keys._(api_key_id).delete()
# print response.status_code
# print response.text

##################################################
# Create a Group #
# POST /asm/groups #

# data = {'sample': 'data'}
# response = self.sg.client.asm.groups.post(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve all suppression groups associated with the user. #
# GET /asm/groups #

# response = self.sg.client.asm.groups.get()
# print response.status_code
# print response.text

##################################################
# Get information on a single suppression group. #
# GET /asm/groups/{group_id} #

# group_id = "test_url_param"
# response = self.sg.client.asm.groups._(group_id).get()
# print response.status_code
# print response.text

##################################################
# Delete a suppression group. #
# DELETE /asm/groups/{group_id} #

# group_id = "test_url_param"
# response = self.sg.client.asm.groups._(group_id).delete()
# print response.status_code
# print response.text

##################################################
# Add Suppressions to a Group #
# POST /asm/groups/{group_id}/suppressions #

# data = {'sample': 'data'}
# group_id = "test_url_param"
# response = self.sg.client.asm.groups._(group_id).suppressions.post(data=data)
# print response.status_code
# print response.text

##################################################
# Get suppressed addresses for a given group. #
# GET /asm/groups/{group_id}/suppressions #

# group_id = "test_url_param"
# response = self.sg.client.asm.groups._(group_id).suppressions.get()
# print response.status_code
# print response.text

##################################################
# Delete a Suppression from a Group #
# DELETE /asm/groups/{group_id}/suppressions/{email} #

# group_id = "test_url_param"
        email = "test_url_param"
# response = self.sg.client.asm.groups._(group_id).suppressions._(email).delete()
# print response.status_code
# print response.text

##################################################
# Update unsubscribe groups #
# PATCH /asm/groups/{unsubscribe_group_id} #

# data = {'sample': 'data'}
# unsubscribe_group_id = "test_url_param"
# response = self.sg.client.asm.groups._(unsubscribe_group_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Add recipient addresses to the global suppression group. #
# POST /asm/suppressions/global #

# data = {'sample': 'data'}
# response = self.sg.client.asm.suppressions._("global").post(data=data)
# print response.status_code
# print response.text

##################################################
# Check if a recipient address is in the global suppressions group. #
# GET /asm/suppressions/global/{email_address} #

# email_address = "test_url_param"
# response = self.sg.client.asm.suppressions._("global")._(email_address).get()
# print response.status_code
# print response.text

##################################################
# Retrieve a Global Suppression #
# GET /asm/suppressions/{email} #

# email = "test_url_param"
# response = self.sg.client.asm.suppressions._(email).get()
# print response.status_code
# print response.text

##################################################
# Delete a Global Suppression #
# DELETE /asm/suppressions/{email} #

# email = "test_url_param"
# response = self.sg.client.asm.suppressions._(email).delete()
# print response.status_code
# print response.text

##################################################
# Gets email statistics by browser.  #
# GET /browsers/stats #

# params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.browsers.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Create a Campaign #
# POST /campaigns #

# data = {'sample': 'data'}
# response = self.sg.client.campaigns.post(data=data)
# print response.status_code
# print response.text

##################################################
# Get all Campaigns #
# GET /campaigns #

# params = {'limit': 0, 'offset': 0}
# response = self.sg.client.campaigns.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Update a Campaign #
# PATCH /campaigns/{campaign_id} #

# data = {'sample': 'data'}
# params = {'campaign_id': 'test_string'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).patch(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Get a single campaign #
# GET /campaigns/{campaign_id} #

# params = {'campaign_id': 0}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a Campaign #
# DELETE /campaigns/{campaign_id} #

# params = {'campaign_id': 'test_string'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Update a Scheduled Campaign #
# PATCH /campaigns/{campaign_id}/schedules #

# data = {'sample': 'data'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Schedule a Campaign #
# POST /campaigns/{campaign_id}/schedules #

# data = {'sample': 'data'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.post(data=data)
# print response.status_code
# print response.text

##################################################
# View Scheduled Time of a Campaign #
# GET /campaigns/{campaign_id}/schedules #

# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.get()
# print response.status_code
# print response.text

##################################################
# Unschedule a Scheduled Campaign #
# DELETE /campaigns/{campaign_id}/schedules #

# params = {'campaign_id': 'test_string'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Send a Campaign #
# POST /campaigns/{campaign_id}/schedules/now #

# data = {'sample': 'data'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.now.post(data=data)
# print response.status_code
# print response.text

##################################################
# Send a Test Campaign #
# POST /campaigns/{campaign_id}/schedules/test #

# data = {'sample': 'data'}
# params = {'campaign_id': 'test_string'}
# campaign_id = "test_url_param"
# response = self.sg.client.campaigns._(campaign_id).schedules.test.post(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Get categories #
# GET /categories #

# params = {'limit': 'test_string', 'order': 'test_string', 'sort_by': 'test_string'}
# response = self.sg.client.categories.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Category Stats provide all of your users email statistics for your categories. #
# GET /categories/stats #

# params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': 'test_string', 'categories': 'test_string'}
# response = self.sg.client.categories.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Get sums of a category's stats [Needs: Stats object defined, has category ID?] #
# GET /categories/stats/sums #

# params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 'test_string', 'sort_by_metric': 'test_string', 'offset': 'test_string', 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
# response = self.sg.client.categories.stats.sums.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve stats by client type #
# GET /clients/stats #

# params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
# response = self.sg.client.clients.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve stats by a specific client type #
# GET /clients/{client_type}/stats #

# params = {'aggregated_by': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string'}
# client_type = "test_url_param"
# response = self.sg.client.clients._(client_type).stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Create a Custom Field #
# POST /contactdb/custom_fields #

# data = {'sample': 'data'}
# response = self.sg.client.contactdb.custom_fields.post(data=data)
# print response.status_code
# print response.text

##################################################
# List All Custom Fields #
# GET /contactdb/custom_fields #

# response = self.sg.client.contactdb.custom_fields.get()
# print response.status_code
# print response.text

##################################################
# Get a Custom Field #
# GET /contactdb/custom_fields/{custom_field_id} #

# params = {'custom_field_id': 0}
# custom_field_id = "test_url_param"
# response = self.sg.client.contactdb.custom_fields._(custom_field_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a Custom Field #
# DELETE /contactdb/custom_fields/{custom_field_id} #

# custom_field_id = "test_url_param"
# response = self.sg.client.contactdb.custom_fields._(custom_field_id).delete()
# print response.status_code
# print response.text

##################################################
# Create a List #
# POST /contactdb/lists #

# data = {'sample': 'data'}
# response = self.sg.client.contactdb.lists.post(data=data)
# print response.status_code
# print response.text

##################################################
# List All Lists #
# GET /contactdb/lists #

# response = self.sg.client.contactdb.lists.get()
# print response.status_code
# print response.text

##################################################
# Delete Multiple lists #
# DELETE /contactdb/lists #

# response = self.sg.client.contactdb.lists.delete()
# print response.status_code
# print response.text

##################################################
# Update a List #
# PATCH /contactdb/lists/{list_id} #

# data = {'sample': 'data'}
# params = {'list_id': 0}
# list_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).patch(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Get a single list. #
# GET /contactdb/lists/{list_id} #

# params = {'list_id': 0}
# list_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a List #
# DELETE /contactdb/lists/{list_id} #

# params = {'delete_contacts': 0}
# list_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Add Multiple Recipients to a List #
# POST /contactdb/lists/{list_id}/recipients #

# data = {'sample': 'data'}
# params = {'list_id': 0}
# list_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).recipients.post(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# List Recipients on a List #
# GET /contactdb/lists/{list_id}/recipients #

# params = {'page': 0, 'page_size': 0, 'list_id': 0}
# list_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).recipients.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Add a Single Recipient to a List #
# POST /contactdb/lists/{list_id}/recipients/{recipient_id} #

# data = {'sample': 'data'}
# params = {'recipient_id': 'test_string', 'list_id': 0}
# list_id = "test_url_param"
        recipient_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).post(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a Single Recipient from a Single List #
# DELETE /contactdb/lists/{list_id}/recipients/{recipient_id} #

# params = {'recipient_id': 0, 'list_id': 0}
# list_id = "test_url_param"
        recipient_id = "test_url_param"
# response = self.sg.client.contactdb.lists._(list_id).recipients._(recipient_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Update Recipient #
# PATCH /contactdb/recipients #

# data = {'sample': 'data'}
# response = self.sg.client.contactdb.recipients.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Add recipients #
# POST /contactdb/recipients #

# data = {'sample': 'data'}
# response = self.sg.client.contactdb.recipients.post(data=data)
# print response.status_code
# print response.text

##################################################
# List Recipients [waiting on Bryan Adamson's response] #
# GET /contactdb/recipients #

# params = {'page': 0, 'page_size': 0}
# response = self.sg.client.contactdb.recipients.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete Recipient #
# DELETE /contactdb/recipients #

# response = self.sg.client.contactdb.recipients.delete()
# print response.status_code
# print response.text

##################################################
# Get the count of billable recipients #
# GET /contactdb/recipients/billable_count #

# response = self.sg.client.contactdb.recipients.billable_count.get()
# print response.status_code
# print response.text

##################################################
# Get a Count of Recipients #
# GET /contactdb/recipients/count #

# response = self.sg.client.contactdb.recipients.count.get()
# print response.status_code
# print response.text

##################################################
# Get Recipients Matching Search Criteria #
# GET /contactdb/recipients/search #

# params = {'{field_name}': 'test_string'}
# response = self.sg.client.contactdb.recipients.search.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve a single recipient #
# GET /contactdb/recipients/{recipient_id} #

# params = {'recipient_id': 'test_string'}
# recipient_id = "test_url_param"
# response = self.sg.client.contactdb.recipients._(recipient_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a Recipient #
# DELETE /contactdb/recipients/{recipient_id} #

# params = {'recipient_id': 'test_string'}
# recipient_id = "test_url_param"
# response = self.sg.client.contactdb.recipients._(recipient_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Get the Lists the Recipient Is On #
# GET /contactdb/recipients/{recipient_id}/lists #

# params = {'recipient_id': 'test_string'}
# recipient_id = "test_url_param"
# response = self.sg.client.contactdb.recipients._(recipient_id).lists.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Get reserved custom fields fields. #
# GET /contactdb/reserved_fields #

# response = self.sg.client.contactdb.reserved_fields.get()
# print response.status_code
# print response.text

##################################################
# Create a Segment #
# POST /contactdb/segments #

# data = {'sample': 'data'}
# response = self.sg.client.contactdb.segments.post(data=data)
# print response.status_code
# print response.text

##################################################
# List All Segments #
# GET /contactdb/segments #

# response = self.sg.client.contactdb.segments.get()
# print response.status_code
# print response.text

##################################################
# Update a segment #
# PATCH /contactdb/segments/{segment_id} #

# data = {'sample': 'data'}
# params = {'segment_id': 'test_string'}
# segment_id = "test_url_param"
# response = self.sg.client.contactdb.segments._(segment_id).patch(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve a Segment #
# GET /contactdb/segments/{segment_id} #

# params = {'segment_id': 0}
# segment_id = "test_url_param"
# response = self.sg.client.contactdb.segments._(segment_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a Segment #
# DELETE /contactdb/segments/{segment_id} #

# params = {'delete_contacts': 0}
# segment_id = "test_url_param"
# response = self.sg.client.contactdb.segments._(segment_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# List Recipients On a Segment #
# GET /contactdb/segments/{segment_id}/recipients #

# params = {'page': 'test_string', 'page_size': 'test_string'}
# segment_id = "test_url_param"
# response = self.sg.client.contactdb.segments._(segment_id).recipients.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Gets email statistics by device type. #
# GET /devices/stats #

# params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.devices.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Gets email statistics by country and state/province. #
# GET /geo/stats #

# params = {'end_date': 'test_string', 'country': 'test_string', 'aggregated_by': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': 'test_string'}
# response = self.sg.client.geo.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# List all IPs #
# GET /ips #

# params = {'subuser': 'test_string', 'ip': 'test_string', 'limit': 'test_string', 'exclude_whitelabels': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.ips.get(, params=params)
# print response.status_code
# print response.text

##################################################
# List all assigned IPs #
# GET /ips/assigned #

# response = self.sg.client.ips.assigned.get()
# print response.status_code
# print response.text

##################################################
# Create an IP pool. #
# POST /ips/pools #

# data = {'sample': 'data'}
# response = self.sg.client.ips.pools.post(data=data)
# print response.status_code
# print response.text

##################################################
# List all IP pools. #
# GET /ips/pools #

# response = self.sg.client.ips.pools.get()
# print response.status_code
# print response.text

##################################################
# Update an IP pools name. #
# PUT /ips/pools/{pool_name} #

# data = {'sample': 'data'}
# pool_name = "test_url_param"
# response = self.sg.client.ips.pools._(pool_name).put(data=data)
# print response.status_code
# print response.text

##################################################
# List the IPs in a specified pool. #
# GET /ips/pools/{pool_name} #

# pool_name = "test_url_param"
# response = self.sg.client.ips.pools._(pool_name).get()
# print response.status_code
# print response.text

##################################################
# Delete an IP pool. #
# DELETE /ips/pools/{pool_name} #

# pool_name = "test_url_param"
# response = self.sg.client.ips.pools._(pool_name).delete()
# print response.status_code
# print response.text

##################################################
# Assign an IP to a pool #
# POST /ips/pools/{pool_name}/ips #

# data = {'sample': 'data'}
# pool_name = "test_url_param"
# response = self.sg.client.ips.pools._(pool_name).ips.post(data=data)
# print response.status_code
# print response.text

##################################################
# Remove an IP address from a pool. #
# DELETE /ips/pools/{pool_name}/ips/{ip} #

# pool_name = "test_url_param"
        ip = "test_url_param"
# response = self.sg.client.ips.pools._(pool_name).ips._(ip).delete()
# print response.status_code
# print response.text

##################################################
# Add an IP to warmup. #
# POST /ips/warmup #

# data = {'sample': 'data'}
# response = self.sg.client.ips.warmup.post(data=data)
# print response.status_code
# print response.text

##################################################
# Get all IPs that are currently warming up. #
# GET /ips/warmup #

# response = self.sg.client.ips.warmup.get()
# print response.status_code
# print response.text

##################################################
# Get warmup status for a particular IP. #
# GET /ips/warmup/{ip_address} #

# ip_address = "test_url_param"
# response = self.sg.client.ips.warmup._(ip_address).get()
# print response.status_code
# print response.text

##################################################
# Remove an IP from warmup. #
# DELETE /ips/warmup/{ip_address} #

# ip_address = "test_url_param"
# response = self.sg.client.ips.warmup._(ip_address).delete()
# print response.status_code
# print response.text

##################################################
# See which pools an IP address belongs to. #
# GET /ips/{ip_address} #

# ip_address = "test_url_param"
# response = self.sg.client.ips._(ip_address).get()
# print response.status_code
# print response.text

##################################################
# Create a batch ID #
# POST /mail/batch #

# data = {'sample': 'data'}
# response = self.sg.client.mail.batch.post(data=data)
# print response.status_code
# print response.text

##################################################
# Validate batch ID #
# GET /mail/batch/{batch_id} #

# params = {'batch_id': 'test_string'}
# batch_id = "test_url_param"
# response = self.sg.client.mail.batch._(batch_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Get all mail settings #
# GET /mail_settings #

# params = {'limit': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.mail_settings.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Update address whitelist mail settings #
# PATCH /mail_settings/address_whitelist #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.address_whitelist.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get address whitelist mail settings #
# GET /mail_settings/address_whitelist #

# response = self.sg.client.mail_settings.address_whitelist.get()
# print response.status_code
# print response.text

##################################################
# Update BCC mail settings #
# PATCH /mail_settings/bcc #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.bcc.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get BCC mail settings #
# GET /mail_settings/bcc #

# response = self.sg.client.mail_settings.bcc.get()
# print response.status_code
# print response.text

##################################################
# Update bounce purge mail settings #
# PATCH /mail_settings/bounce_purge #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.bounce_purge.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get bounce purge mail settings #
# GET /mail_settings/bounce_purge #

# response = self.sg.client.mail_settings.bounce_purge.get()
# print response.status_code
# print response.text

##################################################
# Update footer mail settings #
# PATCH /mail_settings/footer #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.footer.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get footer mail settings [params can be null?] #
# GET /mail_settings/footer #

# response = self.sg.client.mail_settings.footer.get()
# print response.status_code
# print response.text

##################################################
# Update forward bounce mail settings #
# PATCH /mail_settings/forward_bounce #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.forward_bounce.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get forward bounce mail settings #
# GET /mail_settings/forward_bounce #

# response = self.sg.client.mail_settings.forward_bounce.get()
# print response.status_code
# print response.text

##################################################
# Update forward spam mail settings #
# PATCH /mail_settings/forward_spam #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.forward_spam.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get forward spam mail settings #
# GET /mail_settings/forward_spam #

# response = self.sg.client.mail_settings.forward_spam.get()
# print response.status_code
# print response.text

##################################################
# Update plain content mail settings #
# PATCH /mail_settings/plain_content #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.plain_content.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get plain content mail settings #
# GET /mail_settings/plain_content #

# response = self.sg.client.mail_settings.plain_content.get()
# print response.status_code
# print response.text

##################################################
# Update spam check mail settings #
# PATCH /mail_settings/spam_check #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.spam_check.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get spam check mail settings #
# GET /mail_settings/spam_check #

# response = self.sg.client.mail_settings.spam_check.get()
# print response.status_code
# print response.text

##################################################
# Update template mail settings #
# PATCH /mail_settings/template #

# data = {'sample': 'data'}
# response = self.sg.client.mail_settings.template.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get template mail settings #
# GET /mail_settings/template #

# response = self.sg.client.mail_settings.template.get()
# print response.status_code
# print response.text

##################################################
# Gets email statistics by mailbox provider. #
# GET /mailbox_providers/stats #

# params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.mailbox_providers.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Returns a list of all partner settings. #
# GET /partner_settings #

# params = {'limit': 0, 'offset': 0}
# response = self.sg.client.partner_settings.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Updates New Relic partner settings. #
# PATCH /partner_settings/new_relic #

# data = {'sample': 'data'}
# response = self.sg.client.partner_settings.new_relic.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Returns all New Relic partner settings. #
# GET /partner_settings/new_relic #

# response = self.sg.client.partner_settings.new_relic.get()
# print response.status_code
# print response.text

##################################################
# Update SendWithUs Settings #
# PATCH /partner_settings/sendwithus #

# data = {'sample': 'data'}
# response = self.sg.client.partner_settings.sendwithus.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get SendWithUs Settings #
# GET /partner_settings/sendwithus #

# response = self.sg.client.partner_settings.sendwithus.get()
# print response.status_code
# print response.text

##################################################
# Returns a list of scopes for which that user has access. #
# GET /scopes #

# response = self.sg.client.scopes.get()
# print response.status_code
# print response.text

##################################################
# Global Stats provide all of your users email statistics for a given date range. #
# GET /stats #

# params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Create Subuser #
# POST /subusers #

# data = {'sample': 'data'}
# response = self.sg.client.subusers.post(data=data)
# print response.status_code
# print response.text

##################################################
# List all Subusers #
# GET /subusers #

# params = {'username': 'test_string', 'limit': 0, 'offset': 0}
# response = self.sg.client.subusers.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve Subuser Reputations #
# GET /subusers/reputations #

# params = {'subuser_name': 'test_string'}
# response = self.sg.client.subusers.reputations.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Subuser Stats provide all of your users email statistics for your subuser accounts. #
# GET /subusers/stats #

# params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 'test_string', 'offset': 'test_string', 'start_date': 'test_string', 'subusers': 'test_string'}
# response = self.sg.client.subusers.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
#  Gets the total sums of each email statistic metric for all subusers over the given date range. #
# GET /subusers/stats/sums #

# params = {'end_date': 'test_string', 'aggregated_by': 'test_string', 'limit': 'test_string', 'sort_by_metric': 'test_string', 'offset': 'test_string', 'start_date': 'test_string', 'sort_by_direction': 'test_string'}
# response = self.sg.client.subusers.stats.sums.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Enable/disable a subuser #
# PATCH /subusers/{subuser_name} #

# data = {'sample': 'data'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Delete a subuser #
# DELETE /subusers/{subuser_name} #

# params = {'subuser_name': 'test_string'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Update IPs assigned to a subuser #
# PUT /subusers/{subuser_name}/ips #

# data = {'sample': 'data'}
# params = {'subuser_name': 'test_string'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).ips.put(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# Update Monitor Settings for a subuser #
# PUT /subusers/{subuser_name}/monitor #

# data = {'sample': 'data'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).monitor.put(data=data)
# print response.status_code
# print response.text

##################################################
# Create monitor settings #
# POST /subusers/{subuser_name}/monitor #

# data = {'sample': 'data'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).monitor.post(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve monitor settings for a subuser #
# GET /subusers/{subuser_name}/monitor #

# params = {'subuser_name': 'test_string'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).monitor.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete monitor settings #
# DELETE /subusers/{subuser_name}/monitor #

# params = {'subuser_name': 'test_string'}
# subuser_name = "test_url_param"
# response = self.sg.client.subusers._(subuser_name).monitor.delete(, params=params)
# print response.status_code
# print response.text

##################################################
# List all bounces #
# GET /suppression/bounces #

# params = {'start_time': 0, 'end_time': 0}
# response = self.sg.client.suppression.bounces.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete bounces #
# DELETE /suppression/bounces #

# response = self.sg.client.suppression.bounces.delete()
# print response.status_code
# print response.text

##################################################
# Get a Bounce #
# GET /suppression/bounces/{email} #

# email = "test_url_param"
# response = self.sg.client.suppression.bounces._(email).get()
# print response.status_code
# print response.text

##################################################
# Delete a bounce #
# DELETE /suppression/bounces/{email} #

# params = {'email_address': 'test_string'}
# email = "test_url_param"
# response = self.sg.client.suppression.bounces._(email).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Create a transactional template. #
# POST /templates #

# data = {'sample': 'data'}
# response = self.sg.client.templates.post(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve all transactional templates. #
# GET /templates #

# response = self.sg.client.templates.get()
# print response.status_code
# print response.text

##################################################
# Edit a transactional template. #
# PATCH /templates/{template_id} #

# data = {'sample': 'data'}
# template_id = "test_url_param"
# response = self.sg.client.templates._(template_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve a single transactional template. #
# GET /templates/{template_id} #

# template_id = "test_url_param"
# response = self.sg.client.templates._(template_id).get()
# print response.status_code
# print response.text

##################################################
# Delete a template. #
# DELETE /templates/{template_id} #

# template_id = "test_url_param"
# response = self.sg.client.templates._(template_id).delete()
# print response.status_code
# print response.text

##################################################
# Create a new transactional template version. #
# POST /templates/{template_id}/versions #

# data = {'sample': 'data'}
# template_id = "test_url_param"
# response = self.sg.client.templates._(template_id).versions.post(data=data)
# print response.status_code
# print response.text

##################################################
# Edit a transactional template version. #
# PATCH /templates/{template_id}/versions/{version_id} #

# data = {'sample': 'data'}
# template_id = "test_url_param"
        version_id = "test_url_param"
# response = self.sg.client.templates._(template_id).versions._(version_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve a specific transactional template version. #
# GET /templates/{template_id}/versions/{version_id} #

# template_id = "test_url_param"
        version_id = "test_url_param"
# response = self.sg.client.templates._(template_id).versions._(version_id).get()
# print response.status_code
# print response.text

##################################################
# Delete a transactional template version. #
# DELETE /templates/{template_id}/versions/{version_id} #

# template_id = "test_url_param"
        version_id = "test_url_param"
# response = self.sg.client.templates._(template_id).versions._(version_id).delete()
# print response.status_code
# print response.text

##################################################
# Activate a transactional template version. #
# POST /templates/{template_id}/versions/{version_id}/activate #

# data = {'sample': 'data'}
# template_id = "test_url_param"
        version_id = "test_url_param"
# response = self.sg.client.templates._(template_id).versions._(version_id).activate.post(data=data)
# print response.status_code
# print response.text

##################################################
# Get Tracking Settings #
# GET /tracking_settings #

# params = {'limit': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.tracking_settings.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Update Click Tracking Settings #
# PATCH /tracking_settings/click #

# data = {'sample': 'data'}
# response = self.sg.client.tracking_settings.click.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get Click Track Settings #
# GET /tracking_settings/click #

# response = self.sg.client.tracking_settings.click.get()
# print response.status_code
# print response.text

##################################################
# Update Google Analytics Settings #
# PATCH /tracking_settings/google_analytics #

# data = {'sample': 'data'}
# response = self.sg.client.tracking_settings.google_analytics.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get Google Analytics Settings #
# GET /tracking_settings/google_analytics #

# response = self.sg.client.tracking_settings.google_analytics.get()
# print response.status_code
# print response.text

##################################################
# Update Open Tracking Settings #
# PATCH /tracking_settings/open #

# data = {'sample': 'data'}
# response = self.sg.client.tracking_settings.open.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get Open Tracking Settings #
# GET /tracking_settings/open #

# response = self.sg.client.tracking_settings.open.get()
# print response.status_code
# print response.text

##################################################
# Update Subscription Tracking Settings #
# PATCH /tracking_settings/subscription #

# data = {'sample': 'data'}
# response = self.sg.client.tracking_settings.subscription.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get Subscription Tracking Settings #
# GET /tracking_settings/subscription #

# response = self.sg.client.tracking_settings.subscription.get()
# print response.status_code
# print response.text

##################################################
# Get a user's account information. #
# GET /user/account #

# response = self.sg.client.user.account.get()
# print response.status_code
# print response.text

##################################################
# Update a user's profile #
# PATCH /user/profile #

# data = {'sample': 'data'}
# response = self.sg.client.user.profile.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get a user's profile #
# GET /user/profile #

# response = self.sg.client.user.profile.get()
# print response.status_code
# print response.text

##################################################
# Cancel or pause a scheduled send #
# POST /user/scheduled_sends #

# data = {'sample': 'data'}
# response = self.sg.client.user.scheduled_sends.post(data=data)
# print response.status_code
# print response.text

##################################################
# Get all scheduled sends #
# GET /user/scheduled_sends #

# response = self.sg.client.user.scheduled_sends.get()
# print response.status_code
# print response.text

##################################################
# Update user scheduled send information #
# PATCH /user/scheduled_sends/{batch_id} #

# data = {'sample': 'data'}
# batch_id = "test_url_param"
# response = self.sg.client.user.scheduled_sends._(batch_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve scheduled send #
# GET /user/scheduled_sends/{batch_id} #

# params = {'batch_id': 'test_string'}
# batch_id = "test_url_param"
# response = self.sg.client.user.scheduled_sends._(batch_id).get(, params=params)
# print response.status_code
# print response.text

##################################################
# Delete a cancellation or pause of a scheduled send #
# DELETE /user/scheduled_sends/{batch_id} #

# params = {'batch_id': 'test_string'}
# batch_id = "test_url_param"
# response = self.sg.client.user.scheduled_sends._(batch_id).delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Change the Enforced TLS settings #
# PATCH /user/settings/enforced_tls #

# data = {'sample': 'data'}
# response = self.sg.client.user.settings.enforced_tls.patch(data=data)
# print response.status_code
# print response.text

##################################################
# Get the current Enforced TLS settings. #
# GET /user/settings/enforced_tls #

# response = self.sg.client.user.settings.enforced_tls.get()
# print response.status_code
# print response.text

##################################################
# Gets statistics for Parse Webhook usage. #
# GET /user/webhooks/parse/stats #

# params = {'aggregated_by': 'test_string', 'limit': 'test_string', 'start_date': 'test_string', 'end_date': 'test_string', 'offset': 'test_string'}
# response = self.sg.client.user.webhooks.parse.stats.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Create a domain whitelabel. #
# POST /whitelabel/domains #

# data = {'sample': 'data'}
# response = self.sg.client.whitelabel.domains.post(data=data)
# print response.status_code
# print response.text

##################################################
# List all domain whitelabels. #
# GET /whitelabel/domains #

# params = {'username': 'test_string', 'domain': 'test_string', 'exclude_subusers': 0, 'limit': 0, 'offset': 0}
# response = self.sg.client.whitelabel.domains.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Get the default domain whitelabel. #
# GET /whitelabel/domains/default #

# response = self.sg.client.whitelabel.domains.default.get()
# print response.status_code
# print response.text

##################################################
# List the domain whitelabel associated with the given user. #
# GET /whitelabel/domains/subuser #

# response = self.sg.client.whitelabel.domains.subuser.get()
# print response.status_code
# print response.text

##################################################
# Disassociate a domain whitelabel from a given user. #
# DELETE /whitelabel/domains/subuser #

# response = self.sg.client.whitelabel.domains.subuser.delete()
# print response.status_code
# print response.text

##################################################
# Update a domain whitelabel. #
# PATCH /whitelabel/domains/{domain_id} #

# data = {'sample': 'data'}
# domain_id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(domain_id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve a domain whitelabel. #
# GET /whitelabel/domains/{domain_id} #

# domain_id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(domain_id).get()
# print response.status_code
# print response.text

##################################################
# Delete a domain whitelabel. #
# DELETE /whitelabel/domains/{domain_id} #

# domain_id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(domain_id).delete()
# print response.status_code
# print response.text

##################################################
# Associate a domain whitelabel with a given user. #
# POST /whitelabel/domains/{domain_id}/subuser #

# data = {'sample': 'data'}
# domain_id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(domain_id).subuser.post(data=data)
# print response.status_code
# print response.text

##################################################
# Add an IP to a domain whitelabel. #
# POST /whitelabel/domains/{id}/ips #

# data = {'sample': 'data'}
# id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(id).ips.post(data=data)
# print response.status_code
# print response.text

##################################################
# Remove an IP from a domain whitelabel. #
# DELETE /whitelabel/domains/{id}/ips/{ip} #

# id = "test_url_param"
        ip = "test_url_param"
# response = self.sg.client.whitelabel.domains._(id).ips._(ip).delete()
# print response.status_code
# print response.text

##################################################
# Validate a domain whitelabel. #
# POST /whitelabel/domains/{id}/validate #

# data = {'sample': 'data'}
# id = "test_url_param"
# response = self.sg.client.whitelabel.domains._(id).validate.post(data=data)
# print response.status_code
# print response.text

##################################################
# Create an IP #
# POST /whitelabel/ips #

# data = {'sample': 'data'}
# response = self.sg.client.whitelabel.ips.post(data=data)
# print response.status_code
# print response.text

##################################################
# List all IPs #
# GET /whitelabel/ips #

# params = {'limit': 'test_string'}
# response = self.sg.client.whitelabel.ips.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Retrieve an IP #
# GET /whitelabel/ips/{id} #

# id = "test_url_param"
# response = self.sg.client.whitelabel.ips._(id).get()
# print response.status_code
# print response.text

##################################################
# Delete an IP #
# DELETE /whitelabel/ips/{id} #

# id = "test_url_param"
# response = self.sg.client.whitelabel.ips._(id).delete()
# print response.status_code
# print response.text

##################################################
# Validate an IP #
# POST /whitelabel/ips/{id}/validate #

# data = {'sample': 'data'}
# id = "test_url_param"
# response = self.sg.client.whitelabel.ips._(id).validate.post(data=data)
# print response.status_code
# print response.text

##################################################
# Create a Link #
# POST /whitelabel/links #

# data = {'sample': 'data'}
# params = {'limit': 0, 'offset': 0}
# response = self.sg.client.whitelabel.links.post(data=data, params=params)
# print response.status_code
# print response.text

##################################################
# List all Links #
# GET /whitelabel/links #

# params = {'limit': 'test_string'}
# response = self.sg.client.whitelabel.links.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Default Link #
# GET /whitelabel/links/default #

# params = {'domain': 'test_string'}
# response = self.sg.client.whitelabel.links.default.get(, params=params)
# print response.status_code
# print response.text

##################################################
# List Associated Link #
# GET /whitelabel/links/subuser #

# params = {'username': 'test_string'}
# response = self.sg.client.whitelabel.links.subuser.get(, params=params)
# print response.status_code
# print response.text

##################################################
# Disassociate Link #
# DELETE /whitelabel/links/subuser #

# params = {'username': 'test_string'}
# response = self.sg.client.whitelabel.links.subuser.delete(, params=params)
# print response.status_code
# print response.text

##################################################
# Update a Link #
# PATCH /whitelabel/links/{id} #

# data = {'sample': 'data'}
# id = "test_url_param"
# response = self.sg.client.whitelabel.links._(id).patch(data=data)
# print response.status_code
# print response.text

##################################################
# Retrieve a Link #
# GET /whitelabel/links/{id} #

# id = "test_url_param"
# response = self.sg.client.whitelabel.links._(id).get()
# print response.status_code
# print response.text

##################################################
# Delete a Link #
# DELETE /whitelabel/links/{id} #

# id = "test_url_param"
# response = self.sg.client.whitelabel.links._(id).delete()
# print response.status_code
# print response.text

##################################################
# Validate a Link #
# POST /whitelabel/links/{id}/validate #

# data = {'sample': 'data'}
# id = "test_url_param"
# response = self.sg.client.whitelabel.links._(id).validate.post(data=data)
# print response.status_code
# print response.text

##################################################
# Associate Link #
# POST /whitelabel/links/{link_id}/subuser #

# data = {'sample': 'data'}
# link_id = "test_url_param"
# response = self.sg.client.whitelabel.links._(link_id).subuser.post(data=data)
# print response.status_code
# print response.text


