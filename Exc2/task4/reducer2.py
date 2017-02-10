#!/usr/bin/python

import sys

prev_user_id = ""
prev_a_id_list = []

max_user_id = ""
max_a_id_list = []
max_count = 0


for line in sys.stdin:
    user_id, a_id_str = line.strip().split("\t", 1)
    a_id_arr = a_id_str.split()
    if user_id == prev_user_id:
        prev_a_id_list += a_id_arr
    else:
        if prev_user_id != "":
            if len(prev_a_id_list) > max_count:
                max_user_id = prev_user_id
                max_a_id_list = prev_a_id_list
                max_count = len(prev_a_id_list)
        prev_user_id = user_id
        prev_a_id_list = a_id_arr

if prev_user_id != "":
    if len(prev_a_id_list) > max_count:
        max_user_id = prev_user_id
        max_a_id_list = prev_a_id_list
        max_count = len(prev_a_id_list)

if max_count>0:
    output = ", ".join(max_a_id_list)
    output = "{0}\t{1} -> {2}, {3}".format(max_count, max_user_id, max_count, output)
    print output





