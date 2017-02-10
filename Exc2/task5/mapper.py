#!/usr/bin/python

import sys
import random

reservoir = None
line_count = 0

for line_number, line in enumerate(sys.stdin):
    line_count = line_number+1
    if random.randint(0, line_number) == 0:
        line = line.strip()
        reservior = line
print "{0}\t{1}".format(line_count, reservior)












