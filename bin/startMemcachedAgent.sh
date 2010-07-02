#!/bin/sh

. "bin/setGrinderEnv.sh"
java -cp $GRINDER_CP -Dgrinder.script=memcached.py net.grinder.Grinder $GRINDER_PROPERTIES