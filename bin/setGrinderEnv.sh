#!/bin/sh

if [ -z "$SPYMEMCACHED_HOME" ]; then 
    SPYMEMCACHED_HOME=/opt/spymemcached-2.7
fi	

if [ -z "$INFINISPAN_HOME" ]; then 
    INFINISPAN_HOME=/opt/infinispan
fi
	

if [ -z "$GRINDER_HOME" ]; then 
    GRINDER_HOME=/opt/grinder
fi

echo $GRINDER_HOME
GRINDER_CP=~/.m2/repository/log4j/log4j/1.2.16/log4j-1.2.16.jar
GRINDER_CP=$GRINDER_CP:$GRINDER_HOME/lib/grinder.jar
GRINDER_CP=$GRINDER_CP:$SPYMEMCACHED_HOME/spymemcached.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/infinispan-core.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/infinispan-client-hotrod.jar
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/modules/hotrod-client/lib/commons-pool-1.6.jar

# This is needed for logger etc
GRINDER_CP=$GRINDER_CP:$INFINISPAN_HOME/lib/*
	
if [ -z "$GRINDER_PROPERTIES" ]; then 
    GRINDER_PROPERTIES=/Users/g/Go/demos/grinder-infinispan.git/grinder.properties
fi

export SERVER_ADDRESS=localhost
