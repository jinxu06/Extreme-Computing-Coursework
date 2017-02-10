#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET
import heapq

def parser(row):
    root = ET.fromstring(row)
    return root.attrib


max_10 = []
for line in sys.stdin:
    row = line.strip()
    record = parser(row)
    if record['PostTypeId'] != '1':
        continue
    count = int(record['ViewCount'])
    q_id = record['Id']
    if len(max_10)<10:
        heapq.heappush(max_10, (count, q_id))
    else:
        heapq.heappushpop(max_10, (count, q_id))

for item in max_10:
    print "{0}\t{1}".format(item[0], item[1])









