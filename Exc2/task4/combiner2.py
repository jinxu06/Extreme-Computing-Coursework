#!/usr/bin/python

import sys

# Squeeze answer ids into an array. Reducer will assume it receivers (user_id, a_id array)

prev_user_id = ""
prev_a_id_arr = []

for line in sys.stdin:
    user_id, a_id_str = line.strip().split("\t",1)
    a_id_arr = a_id_str.split()
    if prev_user_id == user_id:
        prev_a_id_arr = prev_a_id_arr+a_id_arr
    else:
        if prev_user_id != "":
            print "{0}\t{1}".format(prev_user_id, " ".join(prev_a_id_arr))
        prev_user_id = user_id
        prev_a_id_arr = a_id_arr

if prev_user_id != "":
    print "{0}\t{1}".format(prev_user_id, " ".join(prev_a_id_arr))
