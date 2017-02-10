#!/usr/bin/python

import sys

# compare results from different mappers
max_token_length = 0
max_line_length = 0
for line in sys.stdin:
    _,token_length,line_length = line.split('\t',2)
    if line_length>max_line_length:
        max_line_length = line_length
    if token_length>max_token_length:
        max_token_length = token_length
# output the overall maximum
sys.stdout.write("{0}\t{1}".format(max_token_length, max_line_length))
