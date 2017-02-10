#!/usr/bin/python

import sys

# stripes algorithm, flush the memory when threshold is reached
# use three level dict to store the three-word sequence count
# to get better in-mapper combining chances
# to compress data size and to cut down network workload

def add_three_word_sequence(ori_dict, seq):
    """
    add a single three word sequence to the dict
    use in-place modifcation to save memory
    Args:
        ori_dict: three level dict, use first word as first level key, second word as second level key, etc.
        seq: three word sequence
    """
    assert len(seq)==3, 'length of the seq should be exactly 3'
    if seq[0] in ori_dict:
        if seq[1] in ori_dict[seq[0]]:
            if seq[2] in ori_dict[seq[0]][seq[1]]:
                ori_dict[seq[0]][seq[1]][seq[2]] += 1
            else:
                ori_dict[seq[0]][seq[1]][seq[2]] = 1
        else:
            ori_dict[seq[0]][seq[1]] = { seq[2]:1 }
    else:
        ori_dict[seq[0]] = { seq[1]:{seq[2]:1} }

threshold = 1000000 # threshold set to the bytes of all dict
triple_dict = {}
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    # list all the three word sequence and add them to our dict
    if len(words)>=3:
        for i in range(len(words)-2):
            add_three_word_sequence(triple_dict,(words[i],words[i+1],words[i+2]))
    # if the memory size of our dict reach the threshold, print them out and empty our storage
    if sys.getsizeof(triple_dict)>threshold:
        for word in triple_dict:
            print "{0}\t{1}".format(word, str(triple_dict[word])) # key is the first word, value is a 2-level dict (do serialization)
        triple_dict = {}

# print out the rest at the end
for word in triple_dict:
    print "{0}\t{1}".format(word, str(triple_dict[word]))
