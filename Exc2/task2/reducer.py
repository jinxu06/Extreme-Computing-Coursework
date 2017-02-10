#!/usr/bin/python

import sys

for line_number, line in enumerate(sys.stdin):
    if line_number >= 10:
        break
    line = line.strip()
    items = line.split()
    count = int(items[0])
    q_id = items[1]
    print "{0} {1}".format(count, q_id)

