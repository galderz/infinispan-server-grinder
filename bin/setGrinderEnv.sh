#!/bin/sh

SPYMEMCACHED_HOME=/opt/spymemcached-2.7
INFINISPAN_HOME=/opt/infinispan

GRINDER_HOME=/opt/grinder

GRINDER_CP=/Users/g/.m2/repository/log4j/log4j/1.2.16/log4j-1.2.16.jar
GRINDER_CP=$GRINDER_CP:$GRINDER_HOME/lib/grinder.jar
GRINDER_CP=$GRINDER_CP:$SPYMEMCACHED_HOME/spymemcached.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/infinispan-core.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/infinispan-client-hotrod.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/lib/commons-pool-1.5.6.jar

GRINDER_PROPERTIES=/Users/g/Go/demos/grinder-infinispan.git/grinder.properties

export SERVER_ADDRESS=localhost
