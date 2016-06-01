using System;
using SendGrid.Helpers.Mail;
using System.Collections.Generic;
using System.Net;

string _apiKey = Environment.GetEnvironmentVariable("SENDGRID_APIKEY", EnvironmentVariableTarget.User);
dynamic sg = new SendGrid.SendGridAPIClient(_apiKey);

##################################################
# Retrieve email statistics by browser.  #
# GET /browsers/stats #

string queryParams = @"{
  'aggregated_by': 'day', 
  'browsers': 'test_string', 
  'end_date': '2016-04-01', 
  'limit': 'test_string', 
  'offset': 'test_string', 
  'start_date': '2016-01-01'
}";
dynamic response = sg.client.browsers.stats.get(queryParams: queryParams);
Console.WriteLine(response.StatusCode);
Console.WriteLine(response.ResponseBody.ReadAsStringAsync().Result);
Console.WriteLine(response.ResponseHeaders.ToString());

