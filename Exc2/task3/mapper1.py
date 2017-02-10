#!/usr/bin/python

import sys
import xml.etree.ElementTree as ET

def parser(row):
    root = ET.fromstring(row)
    return root.attrib

for line in sys.stdin:
    row = line.strip()
    record = parser(row)
    if record['PostTypeId'] != '2':
        continue
    user_id = record['OwnerUserId']
    q_id = record['ParentId']
    print "{0}\t{1}".format(user_id, q_id)
