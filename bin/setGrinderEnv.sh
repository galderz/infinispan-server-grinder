#!/bin/sh

SPYMEMCACHED_HOME=/Users/z/Unshared/JBoss/thirdparty/spymemcached-2.4.2
INFINISPAN_HOME=/Users/z/Infinispan/code/trunk/target/distribution/infinispan-4.1.0-SNAPSHOT

GRINDER_HOME=/Users/z/Unshared/JBoss/thirdparty/grinder-3.4
#GRINDER_HOME=/Users/z/Unshared/JBoss/thirdparty/mod-grinder-3.4

GRINDER_CP=$GRINDER_HOME/lib/grinder.jar
GRINDER_CP=$GRINDER_CP:$SPYMEMCACHED_HOME/spymemcached.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/infinispan-core.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/infinispan-client-hotrod.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/lib/commons-pool-1.5.4.jar

GRINDER_PROPERTIES=/Users/z/Infinispan/grinder/grinder.properties

export SERVER_ADDRESS=localhost
