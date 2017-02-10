#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    _, output = line.split("\t", 1)
    print output
    break
