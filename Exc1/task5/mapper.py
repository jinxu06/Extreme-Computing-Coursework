#!/usr/bin/python

import sys
import heapq

# max heap is used here

max_20 = []
for line in sys.stdin:
    line = line.strip()
    items = line.split()
    triple_seq = " ".join(items[:-1])
    count = int(items[-1])
    if len(max_20)<20:
        heapq.heappush(max_20, (count, triple_seq))
    else:
        heapq.heappushpop(max_20, (count, triple_seq))
max_20 = sorted(max_20, reverse=True)
for item in max_20:
    print "common-key\t{0} {1}".format(item[0], item[1])







