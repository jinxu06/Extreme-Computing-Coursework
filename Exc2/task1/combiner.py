#!/usr/bin/python

import sys

# Combiner
# Sum up all the counts with the same (term, filename)

prev_term = ""
prev_filename = ""
prev_count = 0

for line in sys.stdin:
    line = line.strip()
    term, filename, count = line.split(" ", 2)
    count = int(count)
    if term == prev_term and prev_filename == filename:
        prev_count += count
    else:
        if prev_term != "":
            print "{0} {1} {2}".format(prev_term, prev_filename, prev_count)
        prev_count = count
        prev_term = term
        prev_filename = filename

if prev_term != "":
    print "{0} {1} {2}".format(prev_term, prev_filename, prev_count)


