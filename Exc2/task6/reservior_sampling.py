#!/usr/bin/python

import sys
import random


num_sample = int(sys.argv[1])
reservoir = []

for line_number, line in enumerate(sys.stdin):
    if len(reservoir) < num_sample:
        reservoir.append(line.strip())
    else:
        if random.randint(0, line_number) < num_sample:
            idx = random.randint(0, num_sample-1)
            reservoir[idx] = line.strip()

for sample in reservoir:
    print sample


