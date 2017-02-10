#!/usr/bin/python

import sys

# Squeeze question ids into an array. Reducer will assume it receivers (user_id, q_id array)

prev_user_id = ""
prev_q_id_arr = []

for line in sys.stdin:
    user_id, q_id_str = line.strip().split("\t",1)
    q_id_arr = q_id_str.split()
    if prev_user_id == user_id:
        prev_q_id_arr = prev_q_id_arr+q_id_arr
    else:
        if prev_user_id != "":
            prev_q_id_arr = list(set(prev_q_id_arr)) # duplicate question id does exist
            print "{0}\t{1}".format(prev_user_id, " ".join(prev_q_id_arr))
        prev_user_id = user_id
        prev_q_id_arr = q_id_arr

if prev_user_id != "":
    prev_q_id_arr = list(set(prev_q_id_arr)) # duplicate question id does exist
    print "{0}\t{1}".format(prev_user_id, " ".join(prev_q_id_arr))
