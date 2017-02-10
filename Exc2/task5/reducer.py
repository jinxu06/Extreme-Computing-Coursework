#!/usr/bin/python

import sys
import random

total_count = 0
reservior = None

for line in sys.stdin:
    line = line.strip()
    count, sample = line.split('\t', 1)
    count = int(count)
    total_count += count
    if random.randint(0, total_count-1) < count:
        reservior = sample
print reservior



