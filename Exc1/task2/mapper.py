#!/usr/bin/python

import sys

threshold = 10000000 # set threshold to the bytes of key-value table in memory
line_dict = {} # hash table to store key-value pairs, key is the line content, value is a counter.
for line in sys.stdin:
    line = line.rstrip('\r\n') # remove EOL
    # in-mapping combiner, flush to the stdout when threshold is reached
    if line in line_dict:
        line_dict[line] += 1
    else:
        line_dict[line] = 1
    if sys.getsizeof(line_dict)>threshold:
        # flush to the stdout
        for l in line_dict:
            print "{0}\t{1}".format(l,line_dict[l])
        line_dict = {} # empty dictionary
# flush out all the data at the end
for l in line_dict:
    print "{0}\t{1}".format(l,line_dict[l])



