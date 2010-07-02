
from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from java.util import Properties, Random
from jarray import zeros
from java.net import InetSocketAddress
from java.lang import String
from java.util.concurrent import TimeUnit, Future
from java.util import ArrayList
from java.lang import System, Integer

log = grinder.logger.output

random = Random()

# Warm up parameters
warmUpOpCount = 1000
warmUpSizeValue = 1

# Test parameters
opCount = Integer.parseInt(System.getProperty("grinder.numOpsPerThread", "10000"))
writePercentage = 20
numberOfKeys = 100
pooledKeys = ArrayList()
sizeOfValue = 1000

test1 = Test(1, "Warmup (%i ops)" % warmUpOpCount)
test2 = Test(2, "Read (%i ops per thread)" % opCount)
test3 = Test(3, "Put (%i ops per thread)" % opCount)

class TestRunner:

   def __init__(self):
      self.doInit()
      log("Warm up operation count is %i" % warmUpOpCount)
      log("Test operation count is %i" % opCount)

   def warmup(self):
      writes = 0
      reads = 0

      log("Start warming up")
      while (writes < warmUpOpCount and reads < warmUpOpCount):
         isGet = random.nextInt(2) == 1
         if isGet:
            reads = reads + 1
            operationId = reads
            if operationId < warmUpOpCount:
               key = "Warmup-%i-%i" % (operationId, grinder.getThreadNumber())
               self.doGet(key)
         else:
            writes = writes + 1
            operationId = writes
            if operationId < warmUpOpCount:
               key = "Warmup-%i-%i" % (operationId, grinder.getThreadNumber())
               value = self.createValue(warmUpSizeValue)
               self.doPut(key, value)
      log("Warm up finished")

   def initialiseKeys(self):
      log("Initialise test keys")
      for i in range(0, numberOfKeys):
         key = "%i-%i" % (i, grinder.getThreadNumber())
         pooledKeys.add(key)
         value = self.createValue(sizeOfValue)
         self.doPut(key, value)
      log("Initialisation finished")

   def putGetStressor(self):
      readPercentage = 100 - writePercentage
      log("Start put/get stressor test")
      for i in range(0, opCount):
         # Log progress ??
         randomAction = random.nextInt(100)
         randomKeyInt = random.nextInt(numberOfKeys - 1)
         key = pooledKeys.get(randomKeyInt)
         if randomAction < readPercentage:
            readTest = test2.wrap(self.timedRead)
            result = readTest(key)
            self.makeSureCallIsNotSkipped(result)
         else:
            value = self.createValue(sizeOfValue)
            putTest = test3.wrap(self.timedPut)
            putTest(key, value)
      log("End put/get stressor test")

   def makeSureCallIsNotSkipped(self, result):
      if result != None and result[0] > System.currentTimeMillis():
         log("")

   def timedRead(self, key):
      return self.doGet(key)

   def timedPut(self, key, value):
      self.doPut(key, value)   

   def doInit(self):
      raise NotImplementedError, "doInit implementation undefined"

   def doPut(self, key, value):
      raise NotImplementedError, "doPut implementation undefined"

   def doGet(self, key):
      raise NotImplementedError, "doGet implementation undefined"

   def stop(self):
      raise NotImplementedError, "stop implementation undefined"

   def createValue(self, valueSize):
      bytes = zeros(valueSize, 'b')
      random.nextBytes(bytes)
      return bytes

   # This method is called for every run.
   def __call__(self):
      try:
         warmupTest = test1.wrap(self.warmup)
         warmupTest()
         self.initialiseKeys()
         self.putGetStressor()

      finally:
         self.stop()
