# Hot Rod server test runner

import abstractServer
from org.infinispan.client.hotrod import RemoteCacheManager
from java.util import Properties

p = Properties()
p.put("hotrod-servers", "127.0.0.1:11311")
p.put("maxActive", -1)
p.put("maxIdle", -1)

remoteCacheManager = RemoteCacheManager(p)

class TestRunner(abstractServer.TestRunner):

   def doInit(self):
      self.remoteCache = remoteCacheManager.getCache()

   def doPut(self, key, value):
      self.remoteCache.put(key, value)

   def doGet(self, key):
      return self.remoteCache.get(key)

   def stop(self):
      self.remoteCache.stop()

