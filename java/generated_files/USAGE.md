This documentation is based on our [OAI specification](https://github.com/sendgrid/sendgrid-oai).

# INITIALIZATION

```ruby
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import com.sendgrid.*;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;


public class Example {
  public static void main(String[] args) throws IOException {
    // Add the example code here
  }
}
```

# Table of Contents

* [ACCESS SETTINGS](#access_settings)
* [ALERTS](#alerts)
* [API KEYS](#api_keys)
* [ASM](#asm)
* [BROWSERS](#browsers)
* [CAMPAIGNS](#campaigns)
* [CATEGORIES](#categories)
* [CLIENTS](#clients)
* [CONTACTDB](#contactdb)
* [DEVICES](#devices)
* [GEO](#geo)
* [IPS](#ips)
* [MAIL](#mail)
* [MAIL SETTINGS](#mail_settings)
* [MAILBOX PROVIDERS](#mailbox_providers)
* [PARTNER SETTINGS](#partner_settings)
* [SCOPES](#scopes)
* [SENDERS](#senders)
* [STATS](#stats)
* [SUBUSERS](#subusers)
* [SUPPRESSION](#suppression)
* [TEMPLATES](#templates)
* [TRACKING SETTINGS](#tracking_settings)
* [USER](#user)
* [WHITELABEL](#whitelabel)


<a name="access_settings"></a>
# ACCESS SETTINGS

## Retrieve all recent access attempts

**This endpoint allows you to retrieve a list of all of the IP addresses that recently attempted to access your account either through the User Interface or the API.**

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### GET /access_settings/activity


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "access_settings/activity";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add one or more IPs to the whitelist

**This endpoint allows you to add one or more IP addresses to your IP whitelist.**

When adding an IP to your whitelist, include the IP address in an array. You can whitelist one IP at a time, or you can whitelist multiple IPs at once.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### POST /access_settings/whitelist


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "access_settings/whitelist";
    request.body = "{\"ips\":[{\"ip\":\"192.168.1.1\"},{\"ip\":\"192.*.*.*\"},{\"ip\":\"192.168.1.3/32\"}]}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a list of currently whitelisted IPs

**This endpoint allows you to retrieve a list of IP addresses that are currently whitelisted.**

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### GET /access_settings/whitelist


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "access_settings/whitelist";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Remove one or more IPs from the whitelist

**This endpoint allows you to remove one or more IPs from your IP whitelist.**

You can remove one IP at a time, or you can remove multiple IP addresses.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### DELETE /access_settings/whitelist


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "access_settings/whitelist";
    request.body = "{\"ids\":[1,2,3]}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific whitelisted IP

**This endpoint allows you to retreive a specific IP address that has been whitelisted.**

You must include the ID for the specific IP address you want to retrieve in your call.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### GET /access_settings/whitelist/{rule_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "access_settings/whitelist/{rule_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Remove a specific IP from the whitelist

**This endpoint allows you to remove a specific IP address from your IP whitelist.**

When removing a specific IP address from your whitelist, you must include the ID in your call.

IP Access Management allows you to control which IP addresses can be used to access your account, either through the User Interface or the API. There is no limit to the number of IP addresses that you can add to your whitelist. It is possible to remove your own IP address from the whitelist, thus preventing yourself from accessing your account.

For more information, please see our [User Guide](http://sendgrid.com/docs/User_Guide/Settings/ip_access_management.html).

### DELETE /access_settings/whitelist/{rule_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "access_settings/whitelist/{rule_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="alerts"></a>
# ALERTS

## Create a new Alert

**This endpoint allows you to create a new alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

### POST /alerts


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "alerts";
    request.body = "{\"type\":\"stats_notification\",\"frequency\":\"daily\",\"email_to\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all alerts

**This endpoint allows you to retieve all of your alerts.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

### GET /alerts


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "alerts";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update an alert

**This endpoint allows you to update an alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

### PATCH /alerts/{alert_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "alerts/{alert_id}";
    request.body = "{\"email_to\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific alert

**This endpoint allows you to retrieve a specific alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

### GET /alerts/{alert_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "alerts/{alert_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete an alert

**This endpoint allows you to delete an alert.**

Alerts allow you to specify an email address to receive notifications regarding your email usage or statistics. 
* Usage alerts allow you to set the threshold at which an alert will be sent.
* Stats notifications allow you to set how frequently you would like to receive email statistics reports. For example, "daily", "weekly", or "monthly".

For more information about alerts, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/alerts.html).

### DELETE /alerts/{alert_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "alerts/{alert_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="api_keys"></a>
# API KEYS

## Create API keys

**This enpoint allows you to create a new random API Key for the user.**

A JSON request body containing a "name" property is required. If number of maximum keys is reached, HTTP 403 will be returned.

There is a limit of 100 API Keys on your account.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

See the [API Key Permissions List](https://sendgrid.com/docs/API_Reference/Web_API_v3/API_Keys/api_key_permissions_list.html) for a list of all available scopes.

### POST /api_keys


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "api_keys";
    request.body = "{\"sample\":\"data\",\"scopes\":[\"mail.send\",\"alerts.create\",\"alerts.read\"],\"name\":\"My API Key\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all API Keys belonging to the authenticated user

**This endpoint allows you to retrieve all API Keys that belong to the authenticated user.**

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

### GET /api_keys


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "api_keys";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update the name & scopes of an API Key

**This endpoint allows you to update the name and scopes of a given API key.**

A JSON request body with a "name" property is required.
Most provide the list of all the scopes an api key should have.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).


### PUT /api_keys/{api_key_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "api_keys/{api_key_id}";
    request.body = "{\"scopes\":[\"user.profile.read\",\"user.profile.update\"],\"name\":\"A New Hope\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update API keys

**This endpoint allows you to update the name of an existing API Key.**

A JSON request body with a "name" property is required.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

## URI Parameters

| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
|api_key_id |string | required | The ID of the API Key you are updating.|

### PATCH /api_keys/{api_key_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "api_keys/{api_key_id}";
    request.body = "{\"name\":\"A New Hope\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve an existing API Key

**This endpoint allows you to retrieve a single api key.**

If the API Key ID does not exist an HTTP 404 will be returned.

### GET /api_keys/{api_key_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "api_keys/{api_key_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete API keys

**This endpoint allows you to revoke an existing API Key**

Authentications using this API Key will fail after this request is made, with some small propogation delay.If the API Key ID does not exist an HTTP 404 will be returned.

The API Keys feature allows customers to be able to generate an API Key credential which can be used for authentication with the SendGrid v3 Web API or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

## URI Parameters

| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
|api_key_id |string | required | The ID of the API Key you are deleting.|

### DELETE /api_keys/{api_key_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "api_keys/{api_key_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="asm"></a>
# ASM

## Create a new suppression group

**This endpoint allows you to create a new suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

### POST /asm/groups


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "asm/groups";
    request.body = "{\"is_default\":true,\"description\":\"Suggestions for products our users might like.\",\"name\":\"Product Suggestions\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve information about multiple suppression groups

**This endpoint allows you to retrieve information about multiple suppression groups.**

This endpoint will return information for each group ID that you include in your request. To add a group ID to your request, simply append `&id=` followed by the group ID.

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

Suppression groups, or [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html), allow you to label a category of content that you regularly send. This gives your recipients the ability to opt out of a specific set of your email. For example, you might define a group for your transactional email, and one for your marketing email so that your users can continue recieving your transactional email witout having to receive your marketing content.

### GET /asm/groups


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/groups";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a suppression group.

**This endpoint allows you to update or change a suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

### PATCH /asm/groups/{group_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "asm/groups/{group_id}";
    request.body = "{\"description\":\"Suggestions for items our users might like.\",\"name\":\"Item Suggestions\",\"id\":103}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Get information on a single suppression group.

**This endpoint allows you to retrieve a single suppression group.**

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

### GET /asm/groups/{group_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/groups/{group_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a suppression group.

**This endpoint allows you to delete a suppression group.**

You can only delete groups that have not been attached to sent mail in the last 60 days. If a recipient uses the "one-click unsubscribe" option on an email associated with a deleted group, that recipient will be added to the global suppression list.

Suppression groups, or unsubscribe groups, are specific types or categories of email that you would like your recipients to be able to unsubscribe from. For example: Daily Newsletters, Invoices, System Alerts.

The **name** and **description** of the unsubscribe group will be visible by recipients when they are managing their subscriptions.

Each user can create up to 25 different suppression groups.

### DELETE /asm/groups/{group_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "asm/groups/{group_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add suppressions to a suppression group

**This endpoint allows you to add email addresses to an unsubscribe group.**

If you attempt to add suppressions to a group that has been deleted or does not exist, the suppressions will be added to the global suppressions list.

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

### POST /asm/groups/{group_id}/suppressions


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "asm/groups/{group_id}/suppressions";
    request.body = "{\"recipient_emails\":[\"test1@example.com\",\"test2@example.com\"]}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all suppressions for a suppression group

**This endpoint allows you to retrieve all suppressed email addresses belonging to the given group.**

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

### GET /asm/groups/{group_id}/suppressions


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/groups/{group_id}/suppressions";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Search for suppressions within a group

**This endpoint allows you to search a suppression group for multiple suppressions.**

When given a list of email addresses and a group ID, this endpoint will return only the email addresses that have been unsubscribed from the given group.

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

### POST /asm/groups/{group_id}/suppressions/search


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "asm/groups/{group_id}/suppressions/search";
    request.body = "{\"recipient_emails\":[\"exists1@example.com\",\"exists2@example.com\",\"doesnotexists@example.com\"]}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a suppression from a suppression group

**This endpoint allows you to remove a suppressed email address from the given suppression group.**

Suppressions are recipient email addresses that are added to [unsubscribe groups](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html). Once a recipient's address is on the suppressions list for an unsubscribe group, they will not receive any emails that are tagged with that unsubscribe group.

### DELETE /asm/groups/{group_id}/suppressions/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "asm/groups/{group_id}/suppressions/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all suppressions

**This endpoint allows you to retrieve a list of all suppressions.**

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

### GET /asm/suppressions


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/suppressions";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add recipient addresses to the global suppression group.

**This endpoint allows you to add one or more email addresses to the global suppressions group.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

### POST /asm/suppressions/global


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "asm/suppressions/global";
    request.body = "{\"recipient_emails\":[\"test1@example.com\",\"test2@example.com\"]}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Global Suppression

**This endpoint allows you to retrieve a global suppression. You can also use this endpoint to confirm if an email address is already globally suppresed.**

If the email address you include in the URL path parameter `{email}` is alreayd globally suppressed, the response will include that email address. If the address you enter for `{email}` is not globally suppressed, an empty JSON object `{}` will be returned.

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

### GET /asm/suppressions/global/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/suppressions/global/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Global Suppression

**This endpoint allows you to remove an email address from the global suppressions group.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

### DELETE /asm/suppressions/global/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "asm/suppressions/global/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all suppression groups for an email address

**This endpoint returns the list of all groups that the given email address has been unsubscribed from.**

Suppressions are a list of email addresses that will not receive content sent under a given [group](https://sendgrid.com/docs/API_Reference/Web_API_v3/Suppression_Management/groups.html).

### GET /asm/suppressions/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "asm/suppressions/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="browsers"></a>
# BROWSERS

## Retrieve email statistics by browser. 

**This endpoint allows you to retrieve your email statistics segmented by browser type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /browsers/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "browsers/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("aggregated_by", "day");
      queryParams.put("browsers", "test_string");
      queryParams.put("limit", "test_string");
      queryParams.put("offset", "test_string");
      queryParams.put("start_date", "2016-01-01");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="campaigns"></a>
# CAMPAIGNS

## Create a Campaign

**This endpoint allows you to create a campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

Note: In order to send or schedule the campaign, you will be required to provide a subject, sender ID, content (we suggest both html and plain text), and at least one list or segment ID. This information is not required when you create a campaign.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### POST /campaigns


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "campaigns";
    request.body = "{\"custom_unsubscribe_url\":\"\",\"html_content\":\"<html><head><title></title></head><body><p>Check out our spring line!</p></body></html>\",\"list_ids\":[110,124],\"sender_id\":124451,\"subject\":\"New Products for Spring!\",\"plain_content\":\"Check out our spring line!\",\"suppression_group_id\":42,\"title\":\"March Newsletter\",\"segment_ids\":[110],\"categories\":[\"spring line\"],\"ip_pool\":\"marketing\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all Campaigns

**This endpoint allows you to retrieve a list of all of your campaigns.**

Returns campaigns in reverse order they were created (newest first).

Returns an empty array if no campaigns exist.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### GET /campaigns


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "campaigns";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a Campaign

Update a campaign. This is especially useful if you only set up the campaign using POST /campaigns, but didn't set many of the parameters.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### PATCH /campaigns/{campaign_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "campaigns/{campaign_id}";
    request.body = "{\"html_content\":\"<html><head><title></title></head><body><p>Check out our summer line!</p></body></html>\",\"subject\":\"New Products for Summer!\",\"title\":\"May Newsletter\",\"categories\":[\"summer line\"],\"plain_content\":\"Check out our summer line!\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a single campaign

**This endpoint allows you to retrieve a specific campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### GET /campaigns/{campaign_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "campaigns/{campaign_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Campaign

**This endpoint allows you to delete a specific campaign.**

Our Marketing Campaigns API lets you create, manage, send, and schedule campaigns.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### DELETE /campaigns/{campaign_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "campaigns/{campaign_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a Scheduled Campaign

**This endpoint allows to you change the scheduled time and date for a campaign to be sent.**

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### PATCH /campaigns/{campaign_id}/schedules


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "campaigns/{campaign_id}/schedules";
    request.body = "{\"send_at\":1489451436}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Schedule a Campaign

**This endpoint allows you to schedule a specific date and time for your campaign to be sent.**

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### POST /campaigns/{campaign_id}/schedules


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "campaigns/{campaign_id}/schedules";
    request.body = "{\"send_at\":1489771528}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## View Scheduled Time of a Campaign

**This endpoint allows you to retrieve the date and time that the given campaign has been scheduled to be sent.**

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### GET /campaigns/{campaign_id}/schedules


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "campaigns/{campaign_id}/schedules";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Unschedule a Scheduled Campaign

**This endpoint allows you to unschedule a campaign that has already been scheduled to be sent.**

A successful unschedule will return a 204.
If the specified campaign is in the process of being sent, the only option is to cancel (a different method).

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### DELETE /campaigns/{campaign_id}/schedules


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "campaigns/{campaign_id}/schedules";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Send a Campaign

**This endpoint allows you to immediately send a campaign at the time you make the API call.**

Normally a POST would have a request body, but since this endpoint is telling us to send a resource that is already created, a request body is not needed.

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### POST /campaigns/{campaign_id}/schedules/now


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "campaigns/{campaign_id}/schedules/now";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Send a Test Campaign

**This endpoint allows you to send a test campaign.**

To send to multiple addresses, use an array for the JSON "to" value ["one@address","two@address"]

For more information:

* [User Guide > Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html)

### POST /campaigns/{campaign_id}/schedules/test


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "campaigns/{campaign_id}/schedules/test";
    request.body = "{\"to\":\"your.email@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="categories"></a>
# CATEGORIES

## Retrieve all categories

**This endpoint allows you to retrieve a list of all of your categories.**

Categories can help organize your email analytics by enabling you to tag emails by type or broad topic. You can define your own custom categories. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html).

### GET /categories


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "categories";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("category", "test_string");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Email Statistics for Categories

**This endpoint allows you to retrieve all of your email statistics for each of your categories.**

If you do not define any query parameters, this endpoint will return a sum for each category in groups of 10.

Categories allow you to group your emails together according to broad topics that you define. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html). 

### GET /categories/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "categories/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("categories", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve sums of email stats for each category [Needs: Stats object defined, has category ID?]

**This endpoint allows you to retrieve the total sum of each email statistic for every category over the given date range.**

If you do not define any query parameters, this endpoint will return a sum for each category in groups of 10.

Categories allow you to group your emails together according to broad topics that you define. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/categories.html). 

### GET /categories/stats/sums


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "categories/stats/sums";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("sort_by_metric", "test_string");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("sort_by_direction", "asc");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="clients"></a>
# CLIENTS

## Retrieve email statistics by client type.

**This endpoint allows you to retrieve your email statistics segmented by client type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /clients/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "clients/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("aggregated_by", "day");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("end_date", "2016-04-01");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve stats by a specific client type.

**This endpoint allows you to retrieve your email statistics segmented by a specific client type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

## Available Client Types
- phone
- tablet
- webmail
- desktop

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /clients/{client_type}/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "clients/{client_type}/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("aggregated_by", "day");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("end_date", "2016-04-01");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="contactdb"></a>
# CONTACTDB

## Create a Custom Field

**This endpoint allows you to create a custom field.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### POST /contactdb/custom_fields


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/custom_fields";
    request.body = "{\"type\":\"text\",\"name\":\"pet\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all custom fields

**This endpoint allows you to retrieve all custom fields.** 

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### GET /contactdb/custom_fields


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/custom_fields";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Custom Field

**This endpoint allows you to retrieve a custom field by ID.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### GET /contactdb/custom_fields/{custom_field_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/custom_fields/{custom_field_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Custom Field

**This endpoint allows you to delete a custom field by ID.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### DELETE /contactdb/custom_fields/{custom_field_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/custom_fields/{custom_field_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create a List

**This endpoint allows you to create a list for your recipients.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### POST /contactdb/lists


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/lists";
    request.body = "{\"name\":\"your list name\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all lists

**This endpoint allows you to retrieve all of your recipient lists. If you don't have any lists, an empty array will be returned.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/lists


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/lists";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete Multiple lists

**This endpoint allows you to delete multiple recipient lists.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### DELETE /contactdb/lists


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/lists";
    request.body = "[1,2,3,4]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a List

**This endpoint allows you to update the name of one of your recipient lists.**


The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### PATCH /contactdb/lists/{list_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "contactdb/lists/{list_id}";
    request.body = "{\"name\":\"newlistname\"}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("list_id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a single list

This endpoint allows you to retrieve a single recipient list.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/lists/{list_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/lists/{list_id}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("list_id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a List

**This endpoint allows you to delete a specific recipient list with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### DELETE /contactdb/lists/{list_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/lists/{list_id}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("delete_contacts", "true");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add Multiple Recipients to a List

**This endpoint allows you to add multiple recipients to a list.**

Adds existing recipients to a list, passing in the recipient IDs to add. Recipient IDs should be passed exactly as they are returned from recipient endpoints.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### POST /contactdb/lists/{list_id}/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/lists/{list_id}/recipients";
    request.body = "[\"recipient_id1\",\"recipient_id2\"]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all recipients on a List

**This endpoint allows you to retrieve all recipients on the list with the given ID.** 

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/lists/{list_id}/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/lists/{list_id}/recipients";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("page", "1");
      queryParams.put("page_size", "1");
      queryParams.put("list_id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add a Single Recipient to a List

**This endpoint allows you to add a single recipient to a list.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### POST /contactdb/lists/{list_id}/recipients/{recipient_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/lists/{list_id}/recipients/{recipient_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Single Recipient from a Single List

**This endpoint allows you to delete a single recipient from a list.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### DELETE /contactdb/lists/{list_id}/recipients/{recipient_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/lists/{list_id}/recipients/{recipient_id}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("recipient_id", "1");
      queryParams.put("list_id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Recipient

**This endpoint allows you to update one or more recipients.**

The body of an API call to this endpoint must include an array of one or more recipient objects.

It is of note that you can add custom field data as parameters on recipient objects. We have provided an example using some of the default custom fields SendGrid provides.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### PATCH /contactdb/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "contactdb/recipients";
    request.body = "[{\"first_name\":\"Guy\",\"last_name\":\"Jones\",\"email\":\"jones@example.com\"}]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add recipients

**This endpoint allows you to add a Marketing Campaigns recipient.**

It is of note that you can add custom field data as a parameter on this endpoint. We have provided an example using some of the default custom fields SendGrid provides.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### POST /contactdb/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/recipients";
    request.body = "[{\"age\":25,\"last_name\":\"User\",\"email\":\"example@example.com\",\"first_name\":\"\"},{\"age\":25,\"last_name\":\"User\",\"email\":\"example2@example.com\",\"first_name\":\"Example\"}]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve recipients

**This endpoint allows you to retrieve all of your Marketing Campaigns recipients.**

Batch deletion of a page makes it possible to receive an empty page of recipients before reaching the end of
the list of recipients. To avoid this issue; iterate over pages until a 404 is retrieved.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("page", "1");
      queryParams.put("page_size", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete Recipient

**This endpoint allows you to deletes one or more recipients.**

The body of an API call to this endpoint must include an array of recipient IDs of the recipients you want to delete.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### DELETE /contactdb/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/recipients";
    request.body = "[\"recipient_id1\",\"recipient_id2\"]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve the count of billable recipients

**This endpoint allows you to retrieve the number of Marketing Campaigns recipients that you will be billed for.**

You are billed for marketing campaigns based on the highest number of recipients you have had in your account at one time. This endpoint will allow you to know the current billable count value.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/recipients/billable_count


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients/billable_count";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Count of Recipients

**This endpoint allows you to retrieve the total number of Marketing Campaigns recipients.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### GET /contactdb/recipients/count


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients/count";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve recipients matching search criteria

**This endpoint allows you to perform a search on all of your Marketing Campaigns recipients.**

field_name:

* is a variable that is substituted for your actual custom field name from your recipient.
* Text fields must be url-encoded. Date fields are searchable only by unix timestamp (e.g. 2/2/2015 becomes 1422835200)
* If field_name is a 'reserved' date field, such as created_at or updated_at, the system will internally convert
your epoch time to a date range encompassing the entire day. For example, an epoch time of 1422835600 converts to
Mon, 02 Feb 2015 00:06:40 GMT, but internally the system will search from Mon, 02 Feb 2015 00:00:00 GMT through
Mon, 02 Feb 2015 23:59:59 GMT.

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### GET /contactdb/recipients/search


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients/search";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("{field_name}", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a single recipient

**This endpoint allows you to retrieve a single recipient by ID from your contact database.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/recipients/{recipient_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients/{recipient_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Recipient

**This endpoint allows you to delete a single recipient with the given ID from your contact database.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### DELETE /contactdb/recipients/{recipient_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/recipients/{recipient_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve the lists that a recipient is on

**This endpoint allows you to retrieve the lists that a given recipient belongs to.**

Each recipient can be on many lists. This endpoint gives you all of the lists that any one recipient has been added to.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

### GET /contactdb/recipients/{recipient_id}/lists


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/recipients/{recipient_id}/lists";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve reserved fields

**This endpoint allows you to list all fields that are reserved and can't be used for custom field names.**

The contactdb is a database of your contacts for [SendGrid Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html).

### GET /contactdb/reserved_fields


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/reserved_fields";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create a Segment

**This endpoint allows you to create a segment.**

All recipients in your contactdb will be added or removed automatically depending on whether they match the criteria for this segment.

List Id:

* Send this to segment from an existing list
* Don't send this in order to segment from your entire contactdb.

Valid operators for create and update depend on the type of the field you are segmenting: 

* **Dates:** "eq", "ne", "lt" (before), "gt" (after) 
* **Text:** "contains", "eq" (is - matches the full field), "ne" (is not - matches any field where the entire field is not the condition value) 
* **Numbers:** "eq", "lt", "gt" 
* **Email Clicks and Opens:** "eq" (opened), "ne" (not opened) 

Segment conditions using "eq" or "ne" for email clicks and opens should provide a "field" of either *clicks.campaign_identifier* or *opens.campaign_identifier*. The condition value should be a string containing the id of a completed campaign. 

Segments may contain multiple condtions, joined by an "and" or "or" in the "and_or" field. The first condition in the conditions list must have an empty "and_or", and subsequent conditions must all specify an "and_or".

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### POST /contactdb/segments


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "contactdb/segments";
    request.body = "{\"conditions\":[{\"operator\":\"eq\",\"field\":\"last_name\",\"and_or\":\"\",\"value\":\"Miller\"},{\"operator\":\"gt\",\"field\":\"last_clicked\",\"and_or\":\"and\",\"value\":\"01/02/2015\"},{\"operator\":\"eq\",\"field\":\"clicks.campaign_identifier\",\"and_or\":\"or\",\"value\":\"513\"}],\"name\":\"Last Name Miller\",\"list_id\":4}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all segments

**This endpoint allows you to retrieve all of your segments.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### GET /contactdb/segments


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/segments";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a segment

**This endpoint allows you to update a segment.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### PATCH /contactdb/segments/{segment_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "contactdb/segments/{segment_id}";
    request.body = "{\"conditions\":[{\"operator\":\"eq\",\"field\":\"last_name\",\"and_or\":\"\",\"value\":\"Miller\"}],\"name\":\"The Millers\",\"list_id\":5}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("segment_id", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a segment

**This endpoint allows you to retrieve a single segment with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### GET /contactdb/segments/{segment_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/segments/{segment_id}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("segment_id", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a segment

**This endpoint allows you to delete a segment from your recipients database.**

You also have the option to delete all the contacts from your Marketing Campaigns recipient database who were in this segment.

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### DELETE /contactdb/segments/{segment_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "contactdb/segments/{segment_id}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("delete_contacts", "true");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve recipients on a segment

**This endpoint allows you to retrieve all of the recipients in a segment with the given ID.**

The Contacts API helps you manage your [Marketing Campaigns](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/index.html) recipients.

For more information about segments in Marketing Campaigns, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/lists.html#-Create-a-Segment).

### GET /contactdb/segments/{segment_id}/recipients


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "contactdb/segments/{segment_id}/recipients";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("page", "1");
      queryParams.put("page_size", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="devices"></a>
# DEVICES

## Retrieve email statistics by device type.

**This endpoint allows you to retrieve your email statistics segmented by the device type.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

## Available Device Types
| **Device** | **Description** | **Example** |
|---|---|---|
| Desktop | Email software on desktop computer. | I.E., Outlook, Sparrow, or Apple Mail. |
| Webmail |	A web-based email client. | I.E., Yahoo, Google, AOL, or Outlook.com. |
| Phone | A smart phone. | iPhone, Android, Blackberry, etc.
| Tablet | A tablet computer. | iPad, android based tablet, etc. |
| Other | An unrecognized device. |

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /devices/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "devices/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("end_date", "2016-04-01");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="geo"></a>
# GEO

## Retrieve email statistics by country and state/province.

**This endpoint allows you to retrieve your email statistics segmented by country and state/province.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /geo/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "geo/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("country", "US");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="ips"></a>
# IPS

## Retrieve all IP addresses

**This endpoint allows you to retrieve a list of all assigned and unassigned IPs.**

Response includes warm up status, pools, assigned subusers, and whitelabel info. The start_date field corresponds to when warmup started for that IP.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

### GET /ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("subuser", "test_string");
      queryParams.put("ip", "test_string");
      queryParams.put("limit", "1");
      queryParams.put("exclude_whitelabels", "true");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all assigned IPs

**This endpoint allows you to retrieve only assigned IP addresses.**

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

### GET /ips/assigned


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/assigned";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create an IP pool.

**This endpoint allows you to create an IP pool.**

**Each user can create up to 10 different IP pools.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

### POST /ips/pools


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "ips/pools";
    request.body = "{\"name\":\"marketing\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all IP pools.

**This endpoint allows you to retreive all of your IP pools.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

### GET /ips/pools


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/pools";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update an IP pools name.

**This endpoint allows you to update the name of an IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

### PUT /ips/pools/{pool_name}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "ips/pools/{pool_name}";
    request.body = "{\"name\":\"new_pool_name\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all IPs in a specified pool.

**This endpoint allows you to list all of the IP addresses that are in a specific IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

### GET /ips/pools/{pool_name}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/pools/{pool_name}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete an IP pool.

**This endpoint allows you to delete an IP pool.**

IP Pools allow you to group your dedicated SendGrid IP addresses together. For example, you could create separate pools for your transactional and marketing email. When sending marketing emails, specify that you want to use the marketing IP pool. This allows you to maintain separate reputations for your different email traffic.

IP pools can only be used with whitelabeled IP addresses.

If an IP pool is NOT specified for an email, it will use any IP available, including ones in pools.

### DELETE /ips/pools/{pool_name}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "ips/pools/{pool_name}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add an IP address to a pool

**This endpoint allows you to add an IP address to an IP pool.**

You can add the same IP address to multiple pools. It may take up to 60 seconds for your IP address to be added to a pool after your request is made.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

### POST /ips/pools/{pool_name}/ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "ips/pools/{pool_name}/ips";
    request.body = "{\"ip\":\"0.0.0.0\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Remove an IP address from a pool.

**This endpoint allows you to remove an IP address from an IP pool.**

The same IP address can be added to multiple IP pools.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

### DELETE /ips/pools/{pool_name}/ips/{ip}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "ips/pools/{pool_name}/ips/{ip}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add an IP to warmup

**This endpoint allows you to enter an IP address into warmup mode.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

### POST /ips/warmup


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "ips/warmup";
    request.body = "{\"ip\":\"0.0.0.0\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all IPs currently in warmup

**This endpoint allows you to retrieve all of your IP addresses that are currently warming up.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

### GET /ips/warmup


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/warmup";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve warmup status for a specific IP address

**This endpoint allows you to retrieve the warmup status for a specific IP address.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

### GET /ips/warmup/{ip_address}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/warmup/{ip_address}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Remove an IP from warmup

**This endpoint allows you to remove an IP address from warmup mode.**

SendGrid can automatically warm up dedicated IP addresses by limiting the amount of mail that can be sent through them per hour, with the limit determined by how long the IP address has been in warmup. See the [warmup schedule](https://sendgrid.com/docs/API_Reference/Web_API_v3/IP_Management/ip_warmup_schedule.html) for more details on how SendGrid limits your email traffic for IPs in warmup.

For more general information about warming up IPs, please see our [Classroom](https://sendgrid.com/docs/Classroom/Deliver/Delivery_Introduction/warming_up_ips.html).

### DELETE /ips/warmup/{ip_address}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "ips/warmup/{ip_address}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all IP pools an IP address belongs to

**This endpoint allows you to see which IP pools a particular IP address has been added to.**

The same IP address can be added to multiple IP pools.

A single IP address or a range of IP addresses may be dedicated to an account in order to send email for multiple domains. The reputation of this IP is based on the aggregate performance of all the senders who use it.

### GET /ips/{ip_address}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "ips/{ip_address}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="mail"></a>
# MAIL

## Create a batch ID

**This endpoint allows you to generate a new batch ID. This batch ID can be associated with scheduled sends via the mail/send endpoint.**

If you set the SMTPAPI header `batch_id`, it allows you to then associate multiple scheduled mail/send requests together with the same ID. Then at anytime up to 10 minutes before the schedule date, you can cancel all of the mail/send requests that have this batch ID by calling the Cancel Scheduled Send endpoint. 

More Information:

* [Scheduling Parameters > Batch ID](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html)

### POST /mail/batch


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "mail/batch";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Validate batch ID

**This endpoint allows you to validate a batch ID.**

If you set the SMTPAPI header `batch_id`, it allows you to then associate multiple scheduled mail/send requests together with the same ID. Then at anytime up to 10 minutes before the schedule date, you can cancel all of the mail/send requests that have this batch ID by calling the Cancel Scheduled Send endpoint. 

More Information:

* [Scheduling Parameters > Batch ID](https://sendgrid.com/docs/API_Reference/SMTP_API/scheduling_parameters.html)

### GET /mail/batch/{batch_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail/batch/{batch_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## v3 Mail Send

This endpoint allows you to send email over SendGrids v3 Web API, the most recent version of our API. If you are looking for documentation about the v2 Mail Send endpoint, please see our [v2 API Reference](https://sendgrid.com/docs/API_Reference/Web_API/mail.html).

* Top level parameters are referred to as "global".
* Individual fields within the personalizations array will override any other global, or message level, parameters that are defined outside of personalizations.

For an overview of the v3 Mail Send endpoint, please visit our [v3 API Reference](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/index.html)

For more detailed information about how to use the v3 Mail Send endpoint, please visit our [Classroom](https://sendgrid.com/docs/Classroom/Send/v3_Mail_Send/index.html).

### POST /mail/send

This endpoint has a helper, check it out [here](https://github.com/sendgrid/sendgrid-java/blob/master/src/main/java/com/sendgrid/helpers/README.md).

```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "mail/send";
    request.body = "{\"custom_args\":{\"New Argument 1\":\"New Value 1\",\"activationAttempt\":\"1\",\"customerAccountNumber\":\"[CUSTOMER ACCOUNT NUMBER GOES HERE]\"},\"from\":{\"email\":\"sam.smith@example.com\",\"name\":\"Sam Smith\"},\"attachments\":[{\"name\":\"file1\",\"filename\":\"file1.jpg\",\"content\":\"[BASE64 encoded content block here]\",\"disposition\":\"inline\",\"content_id\":\"ii_139db99fdb5c3704\",\"type\":\"jpg\"}],\"personalizations\":[{\"to\":[{\"email\":\"john.doe@example.com\",\"name\":\"John Doe\"}],\"cc\":[{\"email\":\"jane.doe@example.com\",\"name\":\"Jane Doe\"}],\"bcc\":[{\"email\":\"sam.doe@example.com\",\"name\":\"Sam Doe\"}],\"custom_args\":{\"New Argument 1\":\"New Value 1\",\"activationAttempt\":\"1\",\"customerAccountNumber\":\"[CUSTOMER ACCOUNT NUMBER GOES HERE]\"},\"headers\":{\"X-Accept-Language\":\"en\",\"X-Mailer\":\"MyApp\"},\"send_at\":1409348513,\"substitutions\":{\"type\":\"object\",\"id\":\"substitutions\"},\"subject\":\"Hello, World!\"}],\"subject\":\"Hello, World!\",\"ip_pool_name\":\"[YOUR POOL NAME GOES HERE]\",\"content\":[{\"type\":\"text/html\",\"value\":\"<html><p>Hello, world!</p><img src=[CID GOES HERE]></img></html>\"}],\"headers\":{},\"asm\":{\"groups_to_display\":[1,2,3],\"group_id\":1},\"batch_id\":\"[YOUR BATCH ID GOES HERE]\",\"tracking_settings\":{\"subscription_tracking\":{\"text\":\"If you would like to unsubscribe and stop receiveing these emails <% click here %>.\",\"enable\":true,\"html\":\"If you would like to unsubscribe and stop receiving these emails <% clickhere %>.\",\"substitution_tag\":\"<%click here%>\"},\"open_tracking\":{\"enable\":true,\"substitution_tag\":\"%opentrack\"},\"click_tracking\":{\"enable\":true,\"enable_text\":true},\"ganalytics\":{\"utm_campaign\":\"[NAME OF YOUR REFERRER SOURCE]\",\"enable\":true,\"utm_name\":\"[NAME OF YOUR CAMPAIGN]\",\"utm_term\":\"[IDENTIFY PAID KEYWORDS HERE]\",\"utm_content\":\"[USE THIS SPACE TO DIFFERENTIATE YOUR EMAIL FROM ADS]\",\"utm_medium\":\"[NAME OF YOUR MARKETING MEDIUM e.g. email]\"}},\"mail_settings\":{\"footer\":{\"text\":\"Thanks,/n The SendGrid Team\",\"enable\":true,\"html\":\"<p>Thanks</br>The SendGrid Team</p>\"},\"spam_check\":{\"threshold\":3,\"post_to_url\":\"http://example.com/compliance\",\"enable\":true},\"bypass_list_management\":{\"enable\":true},\"sandbox_mode\":{\"enable\":false},\"bcc\":{\"enable\":true,\"email\":\"ben.doe@example.com\"}},\"reply_to\":{\"email\":\"sam.smith@example.com\",\"name\":\"Sam Smith\"},\"sections\":{\"section\":{\":sectionName2\":\"section 2 text\",\":sectionName1\":\"section 1 text\"}},\"template_id\":\"[YOUR TEMPLATE ID GOES HERE]\",\"categories\":[\"category1\",\"category2\"],\"send_at\":1409348513}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="mail_settings"></a>
# MAIL SETTINGS

## Retrieve all mail settings

**This endpoint allows you to retrieve a list of all mail settings.**

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update address whitelist mail settings

**This endpoint allows you to update your current email address whitelist settings.**

The address whitelist setting whitelists a specified email address or domain for which mail should never be suppressed. For example, you own the domain example.com, and one or more of your recipients use email@example.com addresses, by placing example.com in the address whitelist setting, all bounces, blocks, and unsubscribes logged for that domain will be ignored and sent as if under normal sending conditions.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/address_whitelist


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/address_whitelist";
    request.body = "{\"list\":[\"email1@example.com\",\"example.com\"],\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve address whitelist mail settings

**This endpoint allows you to retrieve your current email address whitelist settings.**

The address whitelist setting whitelists a specified email address or domain for which mail should never be suppressed. For example, you own the domain example.com, and one or more of your recipients use email@example.com addresses, by placing example.com in the address whitelist setting, all bounces, blocks, and unsubscribes logged for that domain will be ignored and sent as if under normal sending conditions.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/address_whitelist


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/address_whitelist";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update BCC mail settings

**This endpoint allows you to update your current BCC mail settings.**

When the BCC mail setting is enabled, SendGrid will automatically send a blind carbon copy (BCC) to an address for every email sent without adding that address to the header. Please note that only one email address may be entered in this field, if you wish to distribute BCCs to multiple addresses you will need to create a distribution group or use forwarding rules.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/bcc


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/bcc";
    request.body = "{\"enabled\":false,\"email\":\"email@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all BCC mail settings

**This endpoint allows you to retrieve your current BCC mail settings.**

When the BCC mail setting is enabled, SendGrid will automatically send a blind carbon copy (BCC) to an address for every email sent without adding that address to the header. Please note that only one email address may be entered in this field, if you wish to distribute BCCs to multiple addresses you will need to create a distribution group or use forwarding rules.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/bcc


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/bcc";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update bounce purge mail settings

**This endpoint allows you to update your current bounce purge settings.**

This setting allows you to set a schedule for SendGrid to automatically delete contacts from your soft and hard bounce suppression lists.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/bounce_purge


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/bounce_purge";
    request.body = "{\"hard_bounces\":5,\"soft_bounces\":5,\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve bounce purge mail settings

**This endpoint allows you to retrieve your current bounce purge settings.**

This setting allows you to set a schedule for SendGrid to automatically delete contacts from your soft and hard bounce suppression lists.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/bounce_purge


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/bounce_purge";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update footer mail settings

**This endpoint allows you to update your current Footer mail settings.**

The footer setting will insert a custom footer at the bottom of the text and HTML bodies. Use the embedded HTML editor and plain text entry fields to create the content of the footers to be inserted into your emails.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/footer


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/footer";
    request.body = "{\"html_content\":\"...\",\"enabled\":true,\"plain_content\":\"...\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve footer mail settings

**This endpoint allows you to retrieve your current Footer mail settings.**

The footer setting will insert a custom footer at the bottom of the text and HTML bodies. Use the embedded HTML editor and plain text entry fields to create the content of the footers to be inserted into your emails.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/footer


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/footer";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update forward bounce mail settings

**This endpoint allows you to update your current bounce forwarding mail settings.**

Activating this setting allows you to specify an email address to which bounce reports are forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/forward_bounce


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/forward_bounce";
    request.body = "{\"enabled\":true,\"email\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve forward bounce mail settings

**This endpoint allows you to retrieve your current bounce forwarding mail settings.**

Activating this setting allows you to specify an email address to which bounce reports are forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/forward_bounce


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/forward_bounce";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update forward spam mail settings

**This endpoint allows you to update your current Forward Spam mail settings.**

Enabling the forward spam setting allows you to specify an email address to which spam reports will be forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/forward_spam


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/forward_spam";
    request.body = "{\"enabled\":false,\"email\":\"\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve forward spam mail settings

**This endpoint allows you to retrieve your current Forward Spam mail settings.**

Enabling the forward spam setting allows you to specify an email address to which spam reports will be forwarded.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/forward_spam


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/forward_spam";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update plain content mail settings

**This endpoint allows you to update your current Plain Content mail settings.**

The plain content setting will automatically convert any plain text emails that you send to HTML before sending.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/plain_content


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/plain_content";
    request.body = "{\"enabled\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve plain content mail settings

**This endpoint allows you to retrieve your current Plain Content mail settings.**

The plain content setting will automatically convert any plain text emails that you send to HTML before sending.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/plain_content


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/plain_content";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update spam check mail settings

**This endpoint allows you to update your current spam checker mail settings.**

The spam checker filter notifies you when emails are detected that exceed a predefined spam threshold.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/spam_check


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/spam_check";
    request.body = "{\"url\":\"url\",\"max_score\":5,\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve spam check mail settings

**This endpoint allows you to retrieve your current Spam Checker mail settings.**

The spam checker filter notifies you when emails are detected that exceed a predefined spam threshold.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/spam_check


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/spam_check";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update template mail settings

**This endpoint allows you to update your current legacy email template settings.**

This setting refers to our original email templates. We currently support more fully featured [transactional templates](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). 

The legacy email template setting wraps an HTML template around your email content. This can be useful for sending out marketing email and/or other HTML formatted messages.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### PATCH /mail_settings/template


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "mail_settings/template";
    request.body = "{\"html_content\":\"<% body %>\",\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve legacy template mail settings

**This endpoint allows you to retrieve your current legacy email template settings.**

This setting refers to our original email templates. We currently support more fully featured [transactional templates](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). 

The legacy email template setting wraps an HTML template around your email content. This can be useful for sending out marketing email and/or other HTML formatted messages.

Mail settings allow you to tell SendGrid specific things to do to every email that you send to your recipients over SendGrids [Web API](https://sendgrid.com/docs/API_Reference/Web_API/mail.html) or [SMTP Relay](https://sendgrid.com/docs/API_Reference/SMTP_API/index.html).

### GET /mail_settings/template


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mail_settings/template";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="mailbox_providers"></a>
# MAILBOX PROVIDERS

## Retrieve email statistics by mailbox provider.

**This endpoint allows you to retrieve your email statistics segmented by recipient mailbox provider.**

**We only store up to 7 days of email activity in our database.** By default, 500 items will be returned per request via the Advanced Stats API endpoints.

Advanced Stats provide a more in-depth view of your email statistics and the actions taken by your recipients. You can segment these statistics by geographic location, device type, client type, browser, and mailbox provider. For more information about statistics, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/index.html).

### GET /mailbox_providers/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "mailbox_providers/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("mailbox_providers", "test_string");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="partner_settings"></a>
# PARTNER SETTINGS

## Returns a list of all partner settings.

**This endpoint allows you to retrieve a list of all partner settings that you can enable.**

Our partner settings allow you to integrate your SendGrid account with our partners to increase your SendGrid experience and functionality. For more information about our partners, and how you can begin integrating with them, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/partners.html).

### GET /partner_settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "partner_settings";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Updates New Relic partner settings.

**This endpoint allows you to update or change your New Relic partner settings.**

Our partner settings allow you to integrate your SendGrid account with our partners to increase your SendGrid experience and functionality. For more information about our partners, and how you can begin integrating with them, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/partners.html).

By integrating with New Relic, you can send your SendGrid email statistics to your New Relic Dashboard. If you enable this setting, your stats will be sent to New Relic every 5 minutes. You will need your New Relic License Key to enable this setting. For more information, please see our [Classroom](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/new_relic.html).

### PATCH /partner_settings/new_relic


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "partner_settings/new_relic";
    request.body = "{\"enable_subuser_statistics\":true,\"enabled\":true,\"license_key\":\"\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Returns all New Relic partner settings.

**This endpoint allows you to retrieve your current New Relic partner settings.**

Our partner settings allow you to integrate your SendGrid account with our partners to increase your SendGrid experience and functionality. For more information about our partners, and how you can begin integrating with them, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/partners.html).

By integrating with New Relic, you can send your SendGrid email statistics to your New Relic Dashboard. If you enable this setting, your stats will be sent to New Relic every 5 minutes. You will need your New Relic License Key to enable this setting. For more information, please see our [Classroom](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/new_relic.html).

### GET /partner_settings/new_relic


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "partner_settings/new_relic";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="scopes"></a>
# SCOPES

## Retrieve a list of scopes for which this user has access.

**This endpoint returns a list of all scopes that this user has access to.**

API Keys can be used to authenticate the use of [SendGrids v3 Web API](https://sendgrid.com/docs/API_Reference/Web_API_v3/index.html), or the [Mail API Endpoint](https://sendgrid.com/docs/API_Reference/Web_API/mail.html). API Keys may be assigned certain permissions, or scopes, that limit which API endpoints they are able to access. For a more detailed explanation of how you can use API Key permissios, please visit our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/api_keys.html#-API-Key-Permissions) or [Classroom](https://sendgrid.com/docs/Classroom/Basics/API/api_key_permissions.html). 

### GET /scopes


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "scopes";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="senders"></a>
# SENDERS

## Create a Sender Identity

**This endpoint allows you to create a new sender identity.**

*You may create up to 100 unique sender identities.*

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

### POST /senders


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "senders";
    request.body = "{\"city\":\"Denver\",\"from\":{\"email\":\"from@example.com\",\"name\":\"Example INC\"},\"zip\":\"80202\",\"country\":\"United States\",\"state\":\"Colorado\",\"address_2\":\"Apt. 456\",\"address\":\"123 Elm St.\",\"reply_to\":{\"email\":\"replyto@example.com\",\"name\":\"Example INC\"},\"nickname\":\"My Sender ID\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Get all Sender Identities

**This endpoint allows you to retrieve a list of all sender identities that have been created for your account.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

### GET /senders


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "senders";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a Sender Identity

**This endpoint allows you to update a sender identity.**

Updates to `from.email` require re-verification. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

Partial updates are allowed, but fields that are marked as "required" in the POST (create) endpoint must not be nil if that field is included in the PATCH request.

### PATCH /senders/{sender_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "senders/{sender_id}";
    request.body = "{\"city\":\"Denver\",\"from\":{\"email\":\"from@example.com\",\"name\":\"Example INC\"},\"zip\":\"80202\",\"country\":\"United States\",\"state\":\"Colorado\",\"address_2\":\"Apt. 456\",\"address\":\"123 Elm St.\",\"reply_to\":{\"email\":\"replyto@example.com\",\"name\":\"Example INC\"},\"nickname\":\"My Sender ID\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## View a Sender Identity

**This endpoint allows you to retrieve a specific sender identity.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

### GET /senders/{sender_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "senders/{sender_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Sender Identity

**This endoint allows you to delete one of your sender identities.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

### DELETE /senders/{sender_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "senders/{sender_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Resend Sender Identity Verification

**This enpdoint allows you to resend a sender identity verification email.**

Sender Identities are required to be verified before use. If your domain has been whitelabeled it will auto verify on creation. Otherwise an email will be sent to the `from.email`.

### POST /senders/{sender_id}/resend_verification


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "senders/{sender_id}/resend_verification";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="stats"></a>
# STATS

## Retrieve global email statistics

**This endpoint allows you to retrieve all of your global email statistics between a given date range.**

Parent accounts will see aggregated stats for their account and all subuser accounts. Subuser accounts will only see their own stats.

### GET /stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("end_date", "2016-04-01");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="subusers"></a>
# SUBUSERS

## Create Subuser

This endpoint allows you to retrieve a list of all of your subusers. You can choose to retrieve specific subusers as well as limit the results that come back from the API.

For more information about Subusers:

* [User Guide > Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom > How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

### POST /subusers


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "subusers";
    request.body = "{\"username\":\"John@example.com\",\"ips\":[\"1.1.1.1\",\"2.2.2.2\"],\"password\":\"johns_password\",\"email\":\"John@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## List all Subusers

This endpoint allows you to retrieve a list of all of your subusers. You can choose to retrieve specific subusers as well as limit the results that come back from the API.

For more information about Subusers:

* [User Guide > Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom > How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

### GET /subusers


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("username", "test_string");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Subuser Reputations

Subuser sender reputations give a good idea how well a sender is doing with regards to how recipients and recipient servers react to the mail that is being received. When a bounce, spam report, or other negative action happens on a sent email, it will effect your sender rating.

This endpoint allows you to request the reputations for your subusers.

### GET /subusers/reputations


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/reputations";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("usernames", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve email statistics for your subusers.

**This endpoint allows you to retrieve the email statistics for the given subusers.**

You may retrieve statistics for up to 10 different subusers by including an additional _subusers_ parameter for each additional subuser.

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

### GET /subusers/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("subusers", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve monthly stats for all subusers

**This endpoint allows you to retrieve the monthly email statistics for all subusers over the given date range.**

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats for your subusers. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

When using the `sort_by_metric` to sort your stats by a specific metric, you can not sort by the following metrics:
`bounce_drops`, `deferred`, `invalid_emails`, `processed`, `spam_report_drops`, `spam_reports`, or `unsubscribe_drops`.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

### GET /subusers/stats/monthly


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/stats/monthly";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("subuser", "test_string");
      queryParams.put("limit", "1");
      queryParams.put("sort_by_metric", "test_string");
      queryParams.put("offset", "1");
      queryParams.put("date", "test_string");
      queryParams.put("sort_by_direction", "asc");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
##  Retrieve the totals for each email statistic metric for all subusers.

**This endpoint allows you to retrieve the total sums of each email statistic metric for all subusers over the given date range.**


While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

### GET /subusers/stats/sums


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/stats/sums";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("end_date", "2016-04-01");
      queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "1");
      queryParams.put("sort_by_metric", "test_string");
      queryParams.put("offset", "1");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("sort_by_direction", "asc");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Enable/disable a subuser

This endpoint allows you to enable or disable a subuser.

For more information about Subusers:

* [User Guide > Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom > How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

### PATCH /subusers/{subuser_name}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "subusers/{subuser_name}";
    request.body = "{\"disabled\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a subuser

This endpoint allows you to delete a subuser. This is a permanent action, once deleted a subuser cannot be retrieved.

For more information about Subusers:

* [User Guide > Subusers](https://sendgrid.com/docs/User_Guide/Settings/Subusers/index.html)
* [Classroom > How do I add more subusers to my account?](https://sendgrid.com/docs/Classroom/Basics/Account/how_do_i_add_more_subusers_to_my_account.html)

### DELETE /subusers/{subuser_name}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "subusers/{subuser_name}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update IPs assigned to a subuser

Each subuser should be assigned to an IP address, from which all of this subuser's mail will be sent. Often, this is the same IP as the parent account, but each subuser can have their own, or multiple, IP addresses as well. 

More information:

* [How to request more IPs](https://sendgrid.com/docs/Classroom/Basics/Account/adding_an_additional_dedicated_ip_to_your_account.html)
* [IPs can be whitelabeled](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/ips.html)

### PUT /subusers/{subuser_name}/ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "subusers/{subuser_name}/ips";
    request.body = "[\"127.0.0.1\"]";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Monitor Settings for a subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

### PUT /subusers/{subuser_name}/monitor


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "subusers/{subuser_name}/monitor";
    request.body = "{\"frequency\":500,\"email\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create monitor settings

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

### POST /subusers/{subuser_name}/monitor


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "subusers/{subuser_name}/monitor";
    request.body = "{\"frequency\":50000,\"email\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve monitor settings for a subuser

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

### GET /subusers/{subuser_name}/monitor


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/{subuser_name}/monitor";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete monitor settings

Subuser monitor settings allow you to receive a sample of an outgoing message by a specific customer at a specific frequency of emails.

### DELETE /subusers/{subuser_name}/monitor


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "subusers/{subuser_name}/monitor";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve the monthly email statistics for a single subuser

**This endpoint allows you to retrive the monthly email statistics for a specific subuser.**

While you can always view the statistics for all email activity on your account, subuser statistics enable you to view specific segments of your stats for your subusers. Emails sent, bounces, and spam reports are always tracked for subusers. Unsubscribes, clicks, and opens are tracked if you have enabled the required settings.

When using the `sort_by_metric` to sort your stats by a specific metric, you can not sort by the following metrics:
`bounce_drops`, `deferred`, `invalid_emails`, `processed`, `spam_report_drops`, `spam_reports`, or `unsubscribe_drops`.

For more information, see our [User Guide](https://sendgrid.com/docs/User_Guide/Statistics/subuser.html).

### GET /subusers/{subuser_name}/stats/monthly


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "subusers/{subuser_name}/stats/monthly";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("date", "test_string");
      queryParams.put("sort_by_direction", "asc");
      queryParams.put("limit", "1");
      queryParams.put("sort_by_metric", "test_string");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="suppression"></a>
# SUPPRESSION

## Retrieve all blocks

**This endpoint allows you to retrieve a list of all email addresses that are currently on your blocks list.**

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

### GET /suppression/blocks


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/blocks";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("start_time", "1");
      queryParams.put("limit", "1");
      queryParams.put("end_time", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete blocks

**This endpoint allows you to delete all email addresses on your blocks list.**

There are two options for deleting blocked emails: 

1. You can delete all blocked emails by setting `delete_all` to true in the request body. 
2. You can delete some blocked emails by specifying the email addresses in an array in the request body.

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

### DELETE /suppression/blocks


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/blocks";
    request.body = "{\"emails\":[\"example1@example.com\",\"example2@example.com\"],\"delete_all\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific block

**This endpoint allows you to retrieve a specific email address from your blocks list.**

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

### GET /suppression/blocks/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/blocks/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a specific block

**This endpoint allows you to delete a specific email address from your blocks list.**

[Blocks](https://sendgrid.com/docs/Glossary/blocks.html) happen when your message was rejected for a reason related to the message, not the recipient address. This can happen when your mail server IP address has been added to a blacklist or blocked by an ISP, or if the message content is flagged by a filter on the receiving server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/blocks.html).

### DELETE /suppression/blocks/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/blocks/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all bounces

**This endpoint allows you to retrieve all of your bounces.**

Bounces are messages that are returned to the server that sent it. 

For more information see: 

* [User Guide > Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary > Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)

### GET /suppression/bounces


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/bounces";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("start_time", "1");
      queryParams.put("end_time", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete bounces

**This endpoint allows you to delete all of your bounces. You can also use this endpoint to remove a specific email address from your bounce list.**

Bounces are messages that are returned to the server that sent it.

For more information see: 

* [User Guide > Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary > Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom > List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

Note: the `delete_all` and `emails` parameters should be used independently of each other as they have different purposes.

### DELETE /suppression/bounces


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/bounces";
    request.body = "{\"emails\":[\"example@example.com\",\"example2@example.com\"],\"delete_all\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Bounce

**This endpoint allows you to retrieve a specific bounce for a given email address.**

Bounces are messages that are returned to the server that sent it.

For more information see: 

* [User Guide > Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary > Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom > List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

### GET /suppression/bounces/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/bounces/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a bounce

**This endpoint allows you to remove an email address from your bounce list.**

Bounces are messages that are returned to the server that sent it. This endpoint allows you to delete a single email addresses from your bounce list. 

For more information see: 

* [User Guide > Bounces](https://sendgrid.com/docs/User_Guide/Suppressions/bounces.html) for more information
* [Glossary > Bounces](https://sendgrid.com/docs/Glossary/Bounces.html)
* [Classroom > List Scrubbing Guide](https://sendgrid.com/docs/Classroom/Deliver/list_scrubbing.html)

### DELETE /suppression/bounces/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/bounces/{email}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("email_address", "example@example.com");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all invalid emails

**This endpoint allows you to retrieve a list of all invalid email addresses.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipients mail server.

Examples include addresses without the @ sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

### GET /suppression/invalid_emails


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/invalid_emails";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("start_time", "1");
      queryParams.put("limit", "1");
      queryParams.put("end_time", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete invalid emails

**This endpoint allows you to remove email addresses from your invalid email address list.**

There are two options for deleting invalid email addresses: 

1) You can delete all invalid email addresses by setting `delete_all` to true in the request body.
2) You can delete some invalid email addresses by specifying certain addresses in an array in the request body.

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipients mail server.

Examples include addresses without the @ sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

### DELETE /suppression/invalid_emails


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/invalid_emails";
    request.body = "{\"emails\":[\"example1@example.com\",\"example2@example.com\"],\"delete_all\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific invalid email

**This endpoint allows you to retrieve a specific invalid email addresses.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipients mail server.

Examples include addresses without the @ sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

### GET /suppression/invalid_emails/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/invalid_emails/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a specific invalid email

**This endpoint allows you to remove a specific email address from the invalid email address list.**

An invalid email occurs when you attempt to send email to an address that is formatted in a manner that does not meet internet email format standards or the email does not exist at the recipients mail server.

Examples include addresses without the @ sign or addresses that include certain special characters and/or spaces. This response can come from our own server or the recipient mail server.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/invalid_emails.html).

### DELETE /suppression/invalid_emails/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/invalid_emails/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific spam report

**This endpoint allows you to retrieve a specific spam report.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

### GET /suppression/spam_report/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/spam_report/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a specific spam report

**This endpoint allows you to delete a specific spam report.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

### DELETE /suppression/spam_report/{email}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/spam_report/{email}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all spam reports

**This endpoint allows you to retrieve all spam reports.**

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

### GET /suppression/spam_reports


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/spam_reports";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("start_time", "1");
      queryParams.put("limit", "1");
      queryParams.put("end_time", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete spam reports

**This endpoint allows you to delete your spam reports.**

There are two options for deleting spam reports: 

1) You can delete all spam reports by setting "delete_all" to true in the request body. 
2) You can delete some spam reports by specifying the email addresses in an array in the request body.

[Spam reports](https://sendgrid.com/docs/Glossary/spam_reports.html) happen when a recipient indicates that they think your email is [spam](https://sendgrid.com/docs/Glossary/spam.html) and then their email provider reports this to SendGrid.

For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/spam_reports.html).

### DELETE /suppression/spam_reports


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "suppression/spam_reports";
    request.body = "{\"emails\":[\"example1@example.com\",\"example2@example.com\"],\"delete_all\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all global suppressions

**This endpoint allows you to retrieve a list of all email address that are globally suppressed.**

A global suppression (or global unsubscribe) is an email address of a recipient who does not want to receive any of your messages. A globally suppressed recipient will be removed from any email you send. For more information, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Suppressions/global_unsubscribes.html).

### GET /suppression/unsubscribes


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "suppression/unsubscribes";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("start_time", "1");
      queryParams.put("limit", "1");
      queryParams.put("end_time", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="templates"></a>
# TEMPLATES

## Create a transactional template.

**This endpoint allows you to create a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

### POST /templates


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "templates";
    request.body = "{\"name\":\"example_name\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all transactional templates.

**This endpoint allows you to retrieve all transactional templates.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

### GET /templates


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "templates";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Edit a transactional template.

**This endpoint allows you to edit a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).


### PATCH /templates/{template_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "templates/{template_id}";
    request.body = "{\"name\":\"new_example_name\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a single transactional template.

**This endpoint allows you to retrieve a single transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).


### GET /templates/{template_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "templates/{template_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a template.

**This endpoint allows you to delete a transactional template.**

Each user can create up to 300 different transactional templates. Transactional templates are specific to accounts and subusers. Templates created on a parent account will not be accessible from the subuser accounts.

Transactional templates are templates created specifically for transactional email and are not to be confused with [Marketing Campaigns templates](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/templates.html). For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).


### DELETE /templates/{template_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "templates/{template_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create a new transactional template version.

**This endpoint allows you to create a new version of a template.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).


### POST /templates/{template_id}/versions


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "templates/{template_id}/versions";
    request.body = "{\"name\":\"example_version_name\",\"html_content\":\"<%body%>\",\"plain_content\":\"<%body%>\",\"active\":1,\"template_id\":\"ddb96bbc-9b92-425e-8979-99464621b543\",\"subject\":\"<%subject%>\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Edit a transactional template version.

**This endpoint allows you to edit a version of one of your transactional templates.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string | The ID of the template version |

### PATCH /templates/{template_id}/versions/{version_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "templates/{template_id}/versions/{version_id}";
    request.body = "{\"active\":1,\"html_content\":\"<%body%>\",\"subject\":\"<%subject%>\",\"name\":\"updated_example_name\",\"plain_content\":\"<%body%>\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific transactional template version.

**This endpoint allows you to retrieve a specific version of a template.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string |  The ID of the template version |

### GET /templates/{template_id}/versions/{version_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "templates/{template_id}/versions/{version_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a transactional template version.

**This endpoint allows you to delete one of your transactional template versions.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.

For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string | The ID of the template version |

### DELETE /templates/{template_id}/versions/{version_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "templates/{template_id}/versions/{version_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Activate a transactional template version.

**This endpoint allows you to activate a version of one of your templates.**

Each transactional template can have multiple versions, each version with its own subject and content. Each user can have up to 300 versions across across all templates.


For more information about transactional templates, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html).

## URI Parameters
| URI Parameter | Type | Description |
|---|---|---|
| template_id | string | The ID of the original template |
| version_id | string |  The ID of the template version |

### POST /templates/{template_id}/versions/{version_id}/activate


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "templates/{template_id}/versions/{version_id}/activate";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="tracking_settings"></a>
# TRACKING SETTINGS

## Retrieve Tracking Settings

**This endpoint allows you to retrieve a list of all tracking settings that you can enable on your account.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### GET /tracking_settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "tracking_settings";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Click Tracking Settings

**This endpoint allows you to change your current click tracking setting. You can enable, or disable, click tracking using this endpoint.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### PATCH /tracking_settings/click


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "tracking_settings/click";
    request.body = "{\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Click Track Settings

**This endpoint allows you to retrieve your current click tracking setting.**

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### GET /tracking_settings/click


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "tracking_settings/click";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Google Analytics Settings

**This endpoint allows you to update your current setting for Google Analytics.**

For more information about using Google Analytics, please refer to [Googles URL Builder](https://support.google.com/analytics/answer/1033867?hl=en) and their article on ["Best Practices for Campaign Building"](https://support.google.com/analytics/answer/1037445).

We default the settings to Googles recommendations. For more information, see [Google Analytics Demystified](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/google_analytics_demystified_ga_statistics_vs_sg_statistics.html).

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### PATCH /tracking_settings/google_analytics


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "tracking_settings/google_analytics";
    request.body = "{\"utm_campaign\":\"website\",\"utm_term\":\"\",\"utm_content\":\"\",\"enabled\":true,\"utm_source\":\"sendgrid.com\",\"utm_medium\":\"email\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Google Analytics Settings

**This endpoint allows you to retrieve your current setting for Google Analytics.**

For more information about using Google Analytics, please refer to [Googles URL Builder](https://support.google.com/analytics/answer/1033867?hl=en) and their article on ["Best Practices for Campaign Building"](https://support.google.com/analytics/answer/1037445).

We default the settings to Googles recommendations. For more information, see [Google Analytics Demystified](https://sendgrid.com/docs/Classroom/Track/Collecting_Data/google_analytics_demystified_ga_statistics_vs_sg_statistics.html).

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### GET /tracking_settings/google_analytics


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "tracking_settings/google_analytics";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Open Tracking Settings

**This endpoint allows you to update your current settings for open tracking.**

Open Tracking adds an invisible image at the end of the email which can track email opens. If the email recipient has images enabled on their email client, a request to SendGrids server for the invisible image is executed and an open event is logged. These events are logged in the Statistics portal, Email Activity interface, and are reported by the Event Webhook.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### PATCH /tracking_settings/open


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "tracking_settings/open";
    request.body = "{\"enabled\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Get Open Tracking Settings

**This endpoint allows you to retrieve your current settings for open tracking.**

Open Tracking adds an invisible image at the end of the email which can track email opens. If the email recipient has images enabled on their email client, a request to SendGrids server for the invisible image is executed and an open event is logged. These events are logged in the Statistics portal, Email Activity interface, and are reported by the Event Webhook.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### GET /tracking_settings/open


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "tracking_settings/open";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Subscription Tracking Settings

**This endpoint allows you to update your current settings for subscription tracking.**

Subscription tracking adds links to the bottom of your emails that allows your recipients to subscribe to, or unsubscribe from, your emails.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### PATCH /tracking_settings/subscription


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "tracking_settings/subscription";
    request.body = "{\"url\":\"url\",\"html_content\":\"html content\",\"enabled\":true,\"landing\":\"landing page html\",\"replace\":\"replacement tag\",\"plain_content\":\"text content\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Subscription Tracking Settings

**This endpoint allows you to retrieve your current settings for subscription tracking.**

Subscription tracking adds links to the bottom of your emails that allows your recipients to subscribe to, or unsubscribe from, your emails.

You can track a variety of the actions your recipients may take when interacting with your emails including opening your emails, clicking on links in your emails, and subscribing to (or unsubscribing from) your emails.

For more information about tracking, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/tracking.html).

### GET /tracking_settings/subscription


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "tracking_settings/subscription";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="user"></a>
# USER

## Get a user's account information.

**This endpoint allows you to retrieve your user account details.**

Your user's account information includes the user's account type and reputation.

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### GET /user/account


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/account";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve your credit balance

**This endpoint allows you to retrieve the current credit balance for your account.**

Your monthly credit allotment limits the number of emails you may send before incurring overage charges. For more information about credits and billing, please visit our [Clssroom](https://sendgrid.com/docs/Classroom/Basics/Billing/billing_info_and_faqs.html).

### GET /user/credits


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/credits";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update your account email address

**This endpoint allows you to update the email address currently on file for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### PUT /user/email


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "user/email";
    request.body = "{\"email\":\"example@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve your account email address

**This endpoint allows you to retrieve the email address currently on file for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### GET /user/email


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/email";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update your password

**This endpoint allows you to update your password.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### PUT /user/password


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "user/password";
    request.body = "{\"new_password\":\"new_password\",\"old_password\":\"old_password\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a user's profile

**This endpoint allows you to update your current profile details.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

It should be noted that any one or more of the parameters can be updated via the PATCH /user/profile endpoint. The only requirement is that you include at least one when you PATCH.

### PATCH /user/profile


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "user/profile";
    request.body = "{\"city\":\"Orange\",\"first_name\":\"Example\",\"last_name\":\"User\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Get a user's profile

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### GET /user/profile


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/profile";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Cancel or pause a scheduled send

**This endpoint allows you to cancel or pause an email that has been scheduled to be sent.**

If the maximum number of cancellations/pauses are added, HTTP 400 will
be returned.

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header.Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

### POST /user/scheduled_sends


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "user/scheduled_sends";
    request.body = "{\"batch_id\":\"YOUR_BATCH_ID\",\"status\":\"pause\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all scheduled sends

**This endpoint allows you to retrieve all cancel/paused scheduled send information.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header.Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

### GET /user/scheduled_sends


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/scheduled_sends";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update user scheduled send information

**This endpoint allows you to update the status of a scheduled send for the given `batch_id`.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header.Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

### PATCH /user/scheduled_sends/{batch_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "user/scheduled_sends/{batch_id}";
    request.body = "{\"status\":\"pause\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve scheduled send

**This endpoint allows you to retrieve the cancel/paused scheduled send information for a specific `batch_id`.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header.Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

### GET /user/scheduled_sends/{batch_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/scheduled_sends/{batch_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a cancellation or pause of a scheduled send

**This endpoint allows you to delete the cancellation/pause of a scheduled send.**

The Cancel Scheduled Sends feature allows the customer to cancel a scheduled send based on a Batch ID included in the SMTPAPI header.Scheduled sends cancelled less than 10 minutes before the scheduled time are not guaranteed to be cancelled.

### DELETE /user/scheduled_sends/{batch_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "user/scheduled_sends/{batch_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Enforced TLS settings

**This endpoint allows you to update your current Enforced TLS settings.**

The Enforced TLS settings specify whether or not the recipient is required to support TLS or have a valid certificate. See the [SMTP Ports User Guide](https://sendgrid.com/docs/Classroom/Basics/Email_Infrastructure/smtp_ports.html) for more information on opportunistic TLS.

**Note:** If either setting is enabled and the recipient does not support TLS or have a valid certificate, we drop the message and send a block event with TLS required but not supported as the description.

### PATCH /user/settings/enforced_tls


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "user/settings/enforced_tls";
    request.body = "{\"require_tls\":true,\"require_valid_cert\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve current Enforced TLS settings.

**This endpoint allows you to retrieve your current Enforced TLS settings.**

The Enforced TLS settings specify whether or not the recipient is required to support TLS or have a valid certificate. See the [SMTP Ports User Guide](https://sendgrid.com/docs/Classroom/Basics/Email_Infrastructure/smtp_ports.html) for more information on opportunistic TLS.

**Note:** If either setting is enabled and the recipient does not support TLS or have a valid certificate, we drop the message and send a block event with TLS required but not supported as the description.

### GET /user/settings/enforced_tls


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/settings/enforced_tls";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update your username

**This endpoint allows you to update the username for your account.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### PUT /user/username


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PUT;
    request.endpoint = "user/username";
    request.body = "{\"username\":\"test_username\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve your username

**This endpoint allows you to retrieve your current account username.**

Keeping your user profile up to date is important. This will help SendGrid to verify who you are as well as contact you should we need to.

For more information about your user profile:

* [SendGrid Account Settings](https://sendgrid.com/docs/User_Guide/Settings/account.html)

### GET /user/username


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/username";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update Event Notification Settings

**This endpoint allows you to update your current event webhook settings.**

If an event type is marked as `true`, then the event webhook will include information about that event.

SendGrids Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

### PATCH /user/webhooks/event/settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "user/webhooks/event/settings";
    request.body = "{\"group_resubscribe\":true,\"delivered\":true,\"group_unsubscribe\":true,\"spam_report\":true,\"url\":\"url\",\"enabled\":true,\"bounce\":true,\"deferred\":true,\"unsubscribe\":true,\"dropped\":true,\"open\":true,\"click\":true,\"processed\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Event Webhook settings

**This endpoint allows you to retrieve your current event webhook settings.**

If an event type is marked as `true`, then the event webhook will include information about that event.

SendGrids Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

### GET /user/webhooks/event/settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/webhooks/event/settings";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Test Event Notification Settings 

**This endpoint allows you to test your event webhook by sending a fake event notification post to the provided URL.**

SendGrids Event Webhook will notify a URL of your choice via HTTP POST with information about events that occur as SendGrid processes your email.

Common uses of this data are to remove unsubscribes, react to spam reports, determine unengaged recipients, identify bounced email addresses, or create advanced analytics of your email program.

### POST /user/webhooks/event/test


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "user/webhooks/event/test";
    request.body = "{\"url\":\"url\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create a parse setting

**This endpoint allows you to create a new inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the content, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

### POST /user/webhooks/parse/settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "user/webhooks/parse/settings";
    request.body = "{\"url\":\"http://email.myhosthame.com\",\"send_raw\":false,\"hostname\":\"myhostname.com\",\"spam_check\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all parse settings

**This endpoint allows you to retrieve all of your current inbound parse settings.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

### GET /user/webhooks/parse/settings


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/webhooks/parse/settings";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a parse setting

**This endpoint allows you to update a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

### PATCH /user/webhooks/parse/settings/{hostname}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "user/webhooks/parse/settings/{hostname}";
    request.body = "{\"url\":\"http://newdomain.com/parse\",\"send_raw\":true,\"spam_check\":false}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a specific parse setting

**This endpoint allows you to retrieve a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

### GET /user/webhooks/parse/settings/{hostname}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/webhooks/parse/settings/{hostname}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a parse setting

**This endpoint allows you to delete a specific inbound parse setting.**

The inbound parse webhook allows you to have incoming emails parsed, extracting some or all of the contnet, and then have that content POSTed by SendGrid to a URL of your choosing. For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html).

### DELETE /user/webhooks/parse/settings/{hostname}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "user/webhooks/parse/settings/{hostname}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieves Inbound Parse Webhook statistics.

**This endpoint allows you to retrieve the statistics for your Parse Webhook useage.**

SendGrid's Inbound Parse Webhook allows you to parse the contents and attachments of incomming emails. The Parse API can then POST the parsed emails to a URL that you specify. The Inbound Parse Webhook cannot parse messages greater than 20MB in size, including all attachments.

There are a number of pre-made integrations for the SendGrid Parse Webhook which make processing events easy. You can find these integrations in the [Library Index](https://sendgrid.com/docs/Integrate/libraries.html#-Webhook-Libraries).

### GET /user/webhooks/parse/stats


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "user/webhooks/parse/stats";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("aggregated_by", "day");
      queryParams.put("limit", "test_string");
      queryParams.put("start_date", "2016-01-01");
      queryParams.put("end_date", "2016-04-01");
      queryParams.put("offset", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
<a name="whitelabel"></a>
# WHITELABEL

## Create a domain whitelabel.

**This endpoint allows you to create a whitelabel for one of your domains.**

If you are creating a domain whitelabel that you would like a subuser to use, you have two options:
1. Use the "username" parameter. This allows you to create a whitelabel on behalf of your subuser. This means the subuser is able to see and modify the created whitelabel.
2. Use the Association workflow (see Associate Domain section). This allows you to assign a whitelabel created by the parent to a subuser. This means the subuser will default to the assigned whitelabel, but will not be able to see or modify that whitelabel. However, if the subuser creates their own whitelabel it will overwrite the assigned whitelabel.

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

### POST /whitelabel/domains


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/domains";
    request.body = "{\"automatic_security\":false,\"username\":\"john@example.com\",\"domain\":\"example.com\",\"default\":true,\"custom_spf\":true,\"ips\":[\"192.168.1.1\",\"192.168.1.2\"],\"subdomain\":\"news\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## List all domain whitelabels.

**This endpoint allows you to retrieve a list of all domain whitelabels you have created.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)


### GET /whitelabel/domains


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/domains";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("username", "test_string");
      queryParams.put("domain", "test_string");
      queryParams.put("exclude_subusers", "true");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Get the default domain whitelabel.

**This endpoint allows you to retrieve the default whitelabel for a domain.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| domain | string  |The domain to find a default domain whitelabel for. |

### GET /whitelabel/domains/default


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/domains/default";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## List the domain whitelabel associated with the given user.

**This endpoint allows you to retrieve all of the whitelabels that have been assigned to a specific subuser.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Description  |
|---|---|---|
| username | string  | Username of the subuser to find associated whitelabels for. |

### GET /whitelabel/domains/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/domains/subuser";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Disassociate a domain whitelabel from a given user.

**This endpoint allows you to disassociate a specific whitelabel from a subuser.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Required?  | Description  |
|---|---|---|---|
| username | string  | required  | Username for the subuser to find associated whitelabels for. |

### DELETE /whitelabel/domains/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/domains/subuser";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a domain whitelabel.

**This endpoint allows you to update the settings for a domain whitelabel.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

### PATCH /whitelabel/domains/{domain_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "whitelabel/domains/{domain_id}";
    request.body = "{\"default\":false,\"custom_spf\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a domain whitelabel.

**This endpoint allows you to retrieve a specific domain whitelabel.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)


### GET /whitelabel/domains/{domain_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/domains/{domain_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a domain whitelabel.

**This endpoint allows you to delete a domain whitelabel.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

### DELETE /whitelabel/domains/{domain_id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/domains/{domain_id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Associate a domain whitelabel with a given user.

**This endpoint allows you to associate a specific domain whitelabel with a subuser.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

Domain whitelabels can be associated with (i.e. assigned to) subusers from a parent account. This functionality allows subusers to send mail using their parent's whitelabels. To associate a whitelabel with a subuser, the parent account must first create the whitelabel and validate it. The the parent may then associate the whitelabel via the subuser management tools.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| domain_id | integer   | ID of the domain whitelabel to associate with the subuser. |

### POST /whitelabel/domains/{domain_id}/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/domains/{domain_id}/subuser";
    request.body = "{\"username\":\"jane@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Add an IP to a domain whitelabel.

**This endpoint allows you to add an IP address to a domain whitelabel.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  |  Description  |
|---|---|---|
| id | integer  | ID of the domain to which you are adding an IP |

### POST /whitelabel/domains/{id}/ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/domains/{id}/ips";
    request.body = "{\"ip\":\"192.168.0.1\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Remove an IP from a domain whitelabel.

**This endpoint allows you to remove a domain's IP address from that domain's whitelabel.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type  | Description  |
|---|---|---|
| id | integer  | ID of the domain whitelabel to delete the IP from. |
| ip | string | IP to remove from the domain whitelabel. |

### DELETE /whitelabel/domains/{id}/ips/{ip}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/domains/{id}/ips/{ip}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Validate a domain whitelabel.

**This endpoint allows you to validate a domain whitelabel. If it fails, it will return an error message describing why the whitelabel could not be validated.**

A domain whitelabel allows you to remove the via or sent on behalf of message that your recipients see when they read your emails. Whitelabeling a domain allows you to replace sendgrid.net with your personal sending domain. You will be required to create a subdomain so that SendGrid can generate the DNS records which you must give to your host provider. If you choose to use Automated Security, SendGrid will provide you with 3 CNAME records. If you turn Automated Security off, you will be given 2 TXT records and 1 MX record.

For more information on whitelabeling, please see our [User Guide](https://sendgrid.com/docs/User_Guide/Settings/Whitelabel/index.html)

## URI Parameters
| URI Parameter   | Type   | Description  |
|---|---|---|
| id | integer  |ID of the domain whitelabel to validate. |

### POST /whitelabel/domains/{id}/validate


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/domains/{id}/validate";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create an IP whitelabel

**This endpoint allows you to create an IP whitelabel.**

When creating an IP whitelable, you should use the same subdomain that you used when you created a domain whitelabel.

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

### POST /whitelabel/ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/ips";
    request.body = "{\"ip\":\"192.168.1.1\",\"domain\":\"example.com\",\"subdomain\":\"email\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all IP whitelabels

**This endpoint allows you to retrieve all of the IP whitelabels that have been createdy by this account.**

You may include a search key by using the "ip" parameter. This enables you to perform a prefix search for a given IP segment (e.g. "192.").

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

### GET /whitelabel/ips


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/ips";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("ip", "test_string");
      queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve an IP whitelabel

**This endpoint allows you to retrieve an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

### GET /whitelabel/ips/{id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/ips/{id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete an IP whitelabel

**This endpoint allows you to delete an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

### DELETE /whitelabel/ips/{id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/ips/{id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Validate an IP whitelabel

**This endpoint allows you to validate an IP whitelabel.**

A IP whitelabel consists of a subdomain and domain that will be used to generate a reverse DNS record for a given IP. Once SendGrid has verified that the appropriate A record for the IP has been created, the appropriate reverse DNS record for the IP is generated.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/ips.html).

### POST /whitelabel/ips/{id}/validate


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/ips/{id}/validate";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Create a Link Whitelabel

**This endpoint allows you to create a new link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### POST /whitelabel/links


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/links";
    request.body = "{\"default\":true,\"domain\":\"example.com\",\"subdomain\":\"mail\"}";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
      queryParams.put("offset", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve all link whitelabels

**This endpoint allows you to retrieve all link whitelabels.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### GET /whitelabel/links


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/links";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("limit", "1");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Default Link Whitelabel

**This endpoint allows you to retrieve the default link whitelabel.**

Default link whitelabel is the actual link whitelabel to be used when sending messages. If there are multiple link whitelabels, the default is determined by the following order:
<ul>
  <li>Validated link whitelabels marked as "default"</li>
  <li>Legacy link whitelabels (migrated from the whitelabel wizard)</li>
  <li>Default SendGrid link whitelabel (i.e. 100.ct.sendgrid.net)</li>
</ul>

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### GET /whitelabel/links/default


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/links/default";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("domain", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve Associated Link Whitelabel

**This endpoint allows you to retrieve the associated link whitelabel for a subuser.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### GET /whitelabel/links/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/links/subuser";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("username", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Disassociate a Link Whitelabel

**This endpoint allows you to disassociate a link whitelabel from a subuser.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### DELETE /whitelabel/links/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/links/subuser";
    Map<String,String> queryParams = new HashMap<String, String>();
    queryParams.put("username", "test_string");
    request.queryParams = queryParams;
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Update a Link Whitelabel

**This endpoint allows you to update a specific link whitelabel. You can use this endpoint to change a link whitelabel's default status.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### PATCH /whitelabel/links/{id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.PATCH;
    request.endpoint = "whitelabel/links/{id}";
    request.body = "{\"default\":true}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Retrieve a Link Whitelabel

**This endpoint allows you to retrieve a specific link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### GET /whitelabel/links/{id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.GET;
    request.endpoint = "whitelabel/links/{id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Delete a Link Whitelabel

**This endpoint allows you to delete a link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### DELETE /whitelabel/links/{id}


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.DELETE;
    request.endpoint = "whitelabel/links/{id}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Validate a Link Whitelabel

**This endpoint allows you to validate a link whitelabel.**

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### POST /whitelabel/links/{id}/validate


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/links/{id}/validate";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```
## Associate a Link Whitelabel

**This endpoint allows you to associate a link whitelabel with a subuser account.**

Link whitelables can be associated with subusers from the parent account. This functionality allows
subusers to send mail using their parent's linke whitelabels. To associate a link whitelabel, the parent account
must first create a whitelabel and validate it. The parent may then associate that whitelabel with a subuser via the API or the Subuser Management page in the user interface.

Email link whitelabels allow all of the click-tracked links you send in your emails to include the URL of your domain instead of sendgrid.net.

For more information, please see our [User Guide](https://sendgrid.com/docs/API_Reference/Web_API_v3/Whitelabel/links.html).

### POST /whitelabel/links/{link_id}/subuser


```java
  try {
    SendGrid sg = new SendGrid(System.getenv("SENDGRID_API_KEY"));
    Request request = new Request();
    request.method = Method.POST;
    request.endpoint = "whitelabel/links/{link_id}/subuser";
    request.body = "{\"username\":\"jane@example.com\"}";
    Response response = sg.api(request);
    System.out.println(response.statusCode);
    System.out.println(response.body);
    System.out.println(response.headers);
  } catch (IOException ex) {
    throw ex;
  }
  ```

