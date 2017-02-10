#!/usr/bin/python

import sys
import math


prev_context = ("","")
prev_sum = 0
entropy = 0

for line in sys.stdin:
    line = line.strip()
    items = line.split('\t')
    context = (items[0], items[1])
    if prev_context!=context:
        if prev_sum!=0:
            print prev_context[0], prev_context[1], entropy
            entropy = 0
        prev_context = context
        prev_sum = int(items[3])
    else:
        if items[2]=='*':
            prev_sum += int(items[3])
        else:
            div = float(int(items[3]))/prev_sum
            entropy -= div*math.log(div,2)
print prev_context[0], prev_context[1], entropy

