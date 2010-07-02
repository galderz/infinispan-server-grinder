# REST server test runner

import abstractServer
from net.grinder.plugin.http import HTTPRequest

## Your Infinispan WAR server host
host = "http://127.0.0.1:8080"
path = "/infinispan/rest/___defaultcache/%s"

class TestRunner(abstractServer.TestRunner):

   def doInit(self):
      self.request = HTTPRequest(url = host)

   def doPut(self, key, value):
      # Cache and reuse the http request? Test and see performance
      fullPath = path % key
      response = self.request.PUT(fullPath, value)
      status = response.getStatusCode()
      if status != 200:
         raise Exception("PUT request on %s did not succeed, status returned is %i" % (fullPath, status))

   def doGet(self, key):
      fullPath = path % key
      response = self.request.GET(fullPath)
      status = response.getStatusCode()
      if status != 200 and status != 404:
         raise Exception("GET request on %s did not succeed, status returned is %i" % (fullPath, status))
      return response.getData()

   def stop(self):
      pass # No-op
