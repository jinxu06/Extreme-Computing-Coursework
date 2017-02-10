#!/usr/bin/python

import sys

# Yes, I intended to use "org.apache.hadoop.mapred.lib.IdentityMapper"
# But it seems that there is an unsolved bug in it
# http://stackoverflow.com/questions/7576985/hadoop-streaming-example-failed-to-run-type-mismatch-in-key-from-map

for line in sys.stdin:
    sys.stdout.write(line)
