# Memcached server test runner

import sys
print(sys.path)

import abstractServer
import memcache
from net.grinder.script.Grinder import grinder

log = grinder.logger.info

class TestRunner(abstractServer.TestRunner):

   def doInit(self):
      self.client = memcache.Client(['127.0.0.1:11211'], debug=0)

   def doPut(self, key, value):
      self.client.set(key, value)

   def doRemove(self, key):
     self.client.delete(key)

   def doGet(self, key):
      return self.client.get(key)

   def stop(self):
      self.client.disconnect_all
