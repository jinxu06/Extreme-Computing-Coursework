#!/usr/bin/python

import sys

max_token_length = 0 # record max token length in the current mapper
max_line_length = 0 # record max line length in the current reducer
for line in sys.stdin:
    line = line.strip()
    line_length = len(line) # obtain current line length
    if line_length>max_line_length:
        max_line_length = line_length
    tokens = line.split() # tokenize
    for token in tokens:
        token_length = len(token)
        if token_length>max_token_length:
            max_token_length = token_length
# each mapper will only output just one line, set the key to common key and produce only one reducer job is enough.
print "common-key\t{0}\t{1}".format(max_token_length, max_line_length)




