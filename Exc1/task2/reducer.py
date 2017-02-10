#!/usr/bin/python

import sys

prev_line = ""
prev_count = 0
for pair in sys.stdin:
    pair = pair.rstrip('\r\n')
    line, count = pair.split("\t",1)
    count = int(count)
    if line==prev_line:
        prev_count += count
    elif prev_count!=1:
        # discard when count>1 or initial state count=0
        prev_line = line
        prev_count = count
    elif prev_count==1:
        # unique line, print out
        print prev_line
        prev_line = line
        prev_count = count

# end check, if unique, print out
if prev_count==1:
    print prev_line
