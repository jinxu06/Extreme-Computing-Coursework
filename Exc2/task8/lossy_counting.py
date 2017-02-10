#!/usr/bin/python

import sys

# wrap the std line-by-line stream to a generator
stream = (line.strip() for line in sys.stdin)


def lossy_counting(stream, support, error=None):

    stats = {} # (key=item, value=(frequency, delta))
    if error is None:
        error = suport*0.1 # rule of thumb
    bucket_width = int(1.0/error)
    cur_bucket_label = 0
    total_count = 0

    for index, item in enumerate(stream):
        total_count = index+1
        # update bucket label
        cur_bucket_label = int(float(index)/bucket_width)+1
        # bucket boundary update, release items
        if index % bucket_width == 0:
            stats_new = {}
            for item in stats:
                if stats[item][0]+stats[item][1] > cur_bucket_label:
                    stats_new[item] = stats[item]
            stats = stats_new
        # already exists, increase frequency
        if item in stats:
            stats[item][0] += 1
        # add new item
        else:
            delta = cur_bucket_label-1
            stats[item] = [1, delta]

    for item in stats:
        if stats[item][0] >= (support-error)*total_count:
            print item, stats[item][0]



# support 1%, error 0.1%
lossy_counting(stream, 0.01, 0.001)







