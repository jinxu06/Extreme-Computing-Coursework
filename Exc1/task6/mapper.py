#!/usr/bin/python

import sys

# I use a special third word * to count the overall number of a specific context
# Original three word sequences are also printed out, but * will be the first after shuffle and sort

context_sum = {}
threshold = 10000000

for line in sys.stdin:
    line = line.strip()
    items = line.split()
    if (items[0],items[1]) in context_sum:
        context_sum[(items[0],items[1])] += int(items[3])
    else:
        context_sum[(items[0],items[1])] = int(items[3])
    print "\t".join(items)

    if sys.getsizeof(context_sum)>threshold:
        for context in context_sum:
            print "{0}\t{1}\t{2}\t{3}".format(context[0], context[1], '*', context_sum[context])
            # * is used here as a special word to count the total sum of a specific context"
            # We can make sure this special word is ordered before any others with the same context
        context_sum = {}

# output all the remaining in the end
for context in context_sum:
    print "{0}\t{1}\t{2}\t{3}".format(context[0], context[1], '*', context_sum[context])








