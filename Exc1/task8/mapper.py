#!/usr/bin/python

import sys
import re

# in-mapper combiner

highest = 0
names = []

for line in sys.stdin:
    line = line.strip()
    idx = line.find('-->')
    name = line[:idx-1]
    regex = ur",\d+\)"
    matches = re.findall(regex, line)
    if len(matches)>3:
        scores = [float(int(x[1:-1])) for x in matches]
        mean_score = sum(scores)/len(scores)
        if mean_score>highest:
            highest = mean_score
            names = [name]
        elif mean_score==highest:
            names.append(name)

for name in names:
    print "common-key\t{0}\t{1}".format(name, highest)
# I do this common-key because I want to force mapreduce to send them to one reducer. options in shell seems to be not compulsory...










