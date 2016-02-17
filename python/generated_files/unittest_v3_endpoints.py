import sendgrid
import json
from sendgrid.client import SendGridAPIClient
from sendgrid.version import __version__
from sendgrid.config import Config
try:
    import unittest2 as unittest
except ImportError:
    import unittest
import os
config = Config()

#TODO: Allow option for local mocking, with and without stoplight local test server
class UnitTests(unittest.TestCase):
    def setUp(self):
        #TODO: Location of API Key should come from config
        self.sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')
        #TODO: Host should come from config
        self.host = "https://e9sk3d3bfaikbpdq7.stoplight-proxy.io/v3"
        self.sg = sendgrid.SendGridAPIClient(self.sendgrid_api_key, host=self.host)
        self.api_keys = self.sg.client.api_keys

    def test_apikey_init(self):
        self.assertEqual(self.sg.apikey, self.sendgrid_api_key)

    def test_useragent(self):
        useragent = 'sendgrid/' + __version__ + ';python_v3'
        self.assertEqual(self.sg.useragent, useragent)

    def test_host(self):
        host = 'https://api.sendgrid.com/v3'
        self.assertEqual(self.sg.host, self.host)

    def test_api_keys_post(self):
        data = {"result": [{"name": "API Key Name", "api_key_id": "some-apikey-id"}, {"name": "API Key Name 2", "api_key_id": "another-apikey-id"}]}
        params = {'mock': 201}
        response = self.api_keys.post(data=data, params=params)
        self.assertEqual(response.status_code, 201)

    def test_api_keys_get(self):
        params = {'mock': 200}
        response = self.api_keys.get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__put(self):
        data = {"scopes": ["user.profile.read", "user.profile.update"], "name": "A New Hope", "api_key_id": "qfTQ6KG0QBiwWdJ0-pCLCA"}
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.api_keys._(api_key_id).put(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__patch(self):
        data = {"name": "A New Hope", "api_key_id": "qfTQ6KG0QBiwWdJ0-pCLCA"}
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.api_keys._(api_key_id).patch(data=data, params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__get(self):
        params = {'mock': 200}
        api_key_id = "test_url_param"
        response = self.api_keys._(api_key_id).get(params=params)
        self.assertEqual(response.status_code, 200)

    def test_api_keys__api_key_id__delete(self):
        params = {'mock': 204}
        api_key_id = "test_url_param"
        response = self.api_keys._(api_key_id).delete(params=params)
        self.assertEqual(response.status_code, 204)

