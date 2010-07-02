# Memcached server test runner

import abstractServer
from net.spy.memcached import MemcachedClient
from net.spy.memcached import DefaultConnectionFactory
from java.net import InetSocketAddress
from java.util.concurrent import TimeUnit, Future
from net.grinder.script.Grinder import grinder
from java.util import Arrays

log = grinder.logger.output

class ConnectionFactoryBiggerTimeout(DefaultConnectionFactory):
   
   def getOperationTimeout(self):
      timeout = 5000 # Return 5 seconds
      log("getOperationTimeout returns %ims" % timeout)
      return timeout

class TestRunner(abstractServer.TestRunner):

   def doInit(self):
      self.client = MemcachedClient(ConnectionFactoryBiggerTimeout(), Arrays.asList([InetSocketAddress("127.0.0.1", 11211)]))

   def doPut(self, key, value):
      f = self.client.set(key, 0, value)
      status = f.get(120, TimeUnit.SECONDS)
      if status != 1:
         raise RuntimeException("Set operation did not complete successfully, instead returned %i" % status)

   def doGet(self, key):
      return self.client.get(key)

   def stop(self):
      self.client.shutdown()
