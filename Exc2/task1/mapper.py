#!/usr/bin/python

import sys
import os

# Mapper
# <key=(term, filename), value=frequency>, partition on term, sort on (term, filename)
# In-mapper Combiner


for line in sys.stdin:
    url = os.environ["mapreduce_map_input_file"]
    filename = url[url.rfind(r"/")+1:]
    line = line.strip()
    terms = line.split()
    for term in terms:
        print "{0} {1} {2}".format(term, filename, 1)

