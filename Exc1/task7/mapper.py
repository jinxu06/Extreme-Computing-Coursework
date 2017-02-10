#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    items = line.split()
    if items[0]=='student':
        print "{0}\t{1}\t{2}".format(items[1],items[0],items[2])
    elif items[0]=='mark':
        print "{0}\t{1}\t{2}\t{3}".format(items[1],items[0],items[2],items[3])








