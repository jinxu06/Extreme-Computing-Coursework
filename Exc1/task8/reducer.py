#!/usr/bin/python

import sys

highest_score = 0
names = []
for line in sys.stdin:
    line = line.strip()
    _, name, mean_score = line.split('\t')
    mean_score = float(mean_score)
    if mean_score>highest_score:
        names = []
        names.append(name)
        highest_score = mean_score
    elif mean_score==highest_score:
        names.append(name)
for name in names:
    print name
