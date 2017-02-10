#!/usr/bin/python

import sys


accepted_id = ""
accepted = False
for line in sys.stdin:
    line = line.strip()
    a_id, user_id = line.split()
    if user_id == '*':
        accepted = True
        accepted_id = a_id
        continue
    else:
        if accepted:
            if a_id == accepted_id:
                print "{0}\t{1}".format(user_id, a_id)
            accepted = False


