#!/usr/bin/python

import sys

# receive (user_id, question id list)

max_user_id = ""
max_count = 0
max_q_id_list = []

prev_user_id = ""
prev_q_id_list = set() # use set instead of list, because user does answer to the same question twice

for line in sys.stdin:
    line = line.strip()
    user_id, q_id_str = line.split("\t", 1)
    q_id_arr = q_id_str.split()
    if user_id != prev_user_id:
        if prev_user_id != "":
            if len(prev_q_id_list) > max_count:
                max_user_id = prev_user_id
                max_count = len(prev_q_id_list)
                max_q_id_list = prev_q_id_list
        prev_user_id = user_id
        prev_q_id_list = set(q_id_arr)
    else:
        prev_q_id_list = prev_q_id_list | set(q_id_arr)

if prev_user_id != "":
    if len(prev_q_id_list) > max_count:
        max_user_id = prev_user_id
        max_count = len(prev_q_id_list)
        max_q_id_list = prev_q_id_list

if max_count > 0:
    output = ", ".join(list(max_q_id_list))
    output = "{0}\t{1} -> {2}".format(max_count, max_user_id, output)
    print output



