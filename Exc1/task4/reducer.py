#!/usr/bin/python

import sys
import os

# 2-level dict associated with the same key will be combined, however, there is possibilty that they cannot be fitted into memory at the same time.
# I use external storage to deal with this bottleneck, and these external storage will be combined later use merge sort. So unlike basic stripes algorithm,
# This version has no memory bottleneck. All the storage will be cleaned up, so the program won't leave anything on the cluster.




def inner_dict_combine(dict_mod, dict_ref):
    """
    1-level dict combine
    in-place modification to dict_mod
    Args:
        dict_mod: first dict, will be directly modified to store the final result
        dict_ref: second dict, read only.
    """
    for w in dict_ref:
        if w in dict_mod:
            dict_mod[w] += dict_ref[w]
        else:
            dict_mod[w] = dict_ref[w]

def dict_combine(dict_mod, dict_ref):
    """
    2-level dict combine
    in-place modification to dict_mod
    Args:
        dict_mod: first dict, will be directly modified to store the final result
        dict_ref: second dict, read only.
    """
    for w in dict_ref:
        if w in dict_mod:
            inner_dict_combine(dict_mod[w], dict_ref[w])
        else:
            dict_mod[w] = dict_ref[w]

def external_store(dic, index):
    """
    store a 2-level dict on disk, will merge all the external store corresponding to a specific key later

    Args:
        dic: 2-level dic associated with a specific key
        index: current file index
    """
    # expand the 2-level dict into list of tuples, (second word, third word, count)
    expand_array = []
    for w2 in dic:
        for w3 in dic[w2]:
            expand_array.append((w2,w3,str(dic[w2][w3])))

    f = open("ext_"+str(index), 'w')
    sorted_array = sorted(expand_array, key=lambda x: (x[0],x[1])) # sort the tuples use second word as the first key, third word as the secondary key
    # externally store the sorted result
    for item in sorted_array:
        f.write("\t".join(item)+"\n")

def external_merge():
    """
    Combine all the external files to just one file. Since all the files are already sorted, we will just merge them here
    """
    global file_index
    assert file_index>0, 'file_index should >0 when call external_merge'
    # open all the external files and put handles in a list
    f_comb = open("ext_combine", 'w')
    files = []
    for i in range(file_index):
        if os.stat("ext_"+str(i+1)).st_size>0:
            files.append(open("ext_"+str(i+1)))
    # get the first line in every file
    current_lines = []
    for f in files:
        arr = f.next().strip().split('\t')
        current_lines.append(arr)
    while len(files):
        w2,w3 = min(current_lines, key=lambda x: (x[0],x[1]))[:2] # compare current lines from different files, get the smallest one, w2, w3 are the second, third word in three-word sequence
        count = 0
        end_of_file = [] # record all the files meeting EOF
        for i,line in enumerate(current_lines):
            if line[0]==w2 and line[1]==w3:
                count += int(line[2])
                # if it is going to output, get the next line
                try:
                    current_lines[i] = files[i].next().strip().split('\t')
                except StopIteration:
                    end_of_file.append(i)
        f_comb.write("{0}\t{1}\t{2}\n".format(w2,w3,count))
        for i in end_of_file:
            files[i].close()
        current_lines = [x for i, x in enumerate(current_lines) if i not in end_of_file]
        files = [x for i, x in enumerate(files) if i not in end_of_file]
    for i in range(file_index):
        os.remove("ext_"+str(i+1))
    f_comb.close()
    os.rename('ext_combine', 'ext_1')
    file_index = 1


def external_output(key):
    """
    merge all the external file, output the result and clean up
    """
    global file_index
    external_merge()
    f = open('ext_1','r')
    for line in f:
        items = line.strip().split('\t')
        print '{0} {1} {2}\t{3}'.format(key, items[0], items[1], items[2])
    f.close()
    os.remove('ext_1')
    file_index = 0


prev_word = "" # refer to the first word (key)
prev_dic = {} # 2-level dict (value)
threshold = 1000000
num_file_threshold = 100 # control the number of external files, if too many, merge them immediately
file_index = 0



for line in sys.stdin:
    line = line.strip()
    word, dic = line.split("\t",1)
    dic = eval(dic) # recover dict structure from string
    if word==prev_word:
        dict_combine(prev_dic,dic)
        # check if the prev_dic is too large after combine, if so, use external store and empty current prev_dic
        if sys.getsizeof(prev_dic)>threshold:
            file_index += 1
            external_store(prev_dic, file_index)
            prev_dic = {}
            # if too many files outstanding, merge them immediately
            if file_index>num_file_threshold:
                external_merge()
    else: # empty string won't be a problem, since the prev_dic is empty
        if file_index>0: # if there are external files
            file_index += 1
            external_store(prev_dic, file_index)
            prev_dic = {}
            external_output(prev_word)
        else:
            # do the normal output
            for w2 in prev_dic:
                for w3 in prev_dic[w2]:
                    print "{0} {1} {2}\t{3}".format(prev_word,w2,w3,prev_dic[w2][w3])
        prev_word = word
        prev_dic = dic

# print out all the remaining at the end
if file_index>0: # if there are external files
    file_index += 1
    external_store(prev_dic, file_index)
    external_output(prev_word)
else:
    # do the normal output
    for w2 in prev_dic:
        for w3 in prev_dic[w2]:
            print "{0} {1} {2}\t{3}".format(prev_word,w2,w3,prev_dic[w2][w3])

