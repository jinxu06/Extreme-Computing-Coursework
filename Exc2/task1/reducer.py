#!/usr/bin/python

import sys

# Reducer

prev_term = ""
prev_filename = ""
prev_count = 0
file_list = []

for line in sys.stdin:
    line = line.strip()
    term, filename, count = line.split(" ", 2)
    count = int(count)
    if term == prev_term:
        if filename == prev_filename:
            prev_count += count
        else:
            file_list.append((prev_filename, prev_count))
            prev_filename = filename
            prev_count = count
    else:
        if prev_term != "":
            file_list.append((prev_filename, prev_count))
            output = ["({0}, {1})".format(item[0], item[1]) for item in file_list]
            output = ", ".join(output)
            output = "{0}: {1}: {2}".format(prev_term, len(file_list), "{"+output+"}")
            print output
        prev_term = term
        prev_filename = filename
        prev_count = count
        file_list = []

file_list.append((prev_filename, prev_count))
output = ["({0}, {1})".format(item[0], item[1]) for item in file_list]
output = ", ".join(output)
output = "{0}: {1}: {2}".format(prev_term, len(file_list), "{"+output+"}")
print output



