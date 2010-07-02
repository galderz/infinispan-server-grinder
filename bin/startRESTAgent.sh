#!/bin/sh

. "bin/setGrinderEnv.sh"
java -cp $GRINDER_CP -Dgrinder.script=rest.py net.grinder.Grinder $GRINDER_PROPERTIES

