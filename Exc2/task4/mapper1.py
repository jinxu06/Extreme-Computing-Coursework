#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

def parser(row):
    root = ET.fromstring(row)
    return root.attrib

for line in sys.stdin:
    row = line.strip()
    record = parser(row)
    if record['PostTypeId']=='1':
        if  'AcceptedAnswerId' in record:
            print "{0}\t{1}".format(record['AcceptedAnswerId'], '*')
    elif record['PostTypeId']=='2':
        print "{0}\t{1}".format(record['Id'], record['OwnerUserId'])









