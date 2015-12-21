import httplib
import json
from urlparse import urlparse

class ApiClient:

  def __init__(self, access_token, resource, base_url):
    self.access_token = access_token

    self.resource = resource

    self.base_url = base_url

    self.parsed_base_url = urlparse(base_url)

    self.connection = httplib.HTTPConnection(self.parsed_base_url.hostname, self.parsed_base_url.port)

  def assemble_url(self, resource_id = None):
    path = self.parsed_base_url.path

    url_id = ''

    if resource_id:
      url_id = '/' + str(resource_id)

    url = self.parsed_base_url.path + self.resource + url_id + '?access_token=' + self.access_token

    return url

  def make_request(self, *args):
    self.connection.request(*args)

    response = self.connection.getresponse()

    data = response.read()

    return [response.status, response.reason, data]

  def index(self):
    return self.make_request('GET', self.assemble_url())

  def show(self, id):
    return self.make_request('GET', self.assemble_url(id))

  def create(self, params):
    headers = {
      'Content-Type': 'application/json'
    }

    return self.make_request('POST', self.assemble_url(), json.dumps(params), headers)

  def update(self, id, params):
    headers = {
      'Content-Type': 'application/json'
    }

    return self.make_request('PATCH', self.assemble_url(id), json.dumps(params), headers)

  def destroy(self, id):
    return self.make_request('DELETE', self.assemble_url(id))
