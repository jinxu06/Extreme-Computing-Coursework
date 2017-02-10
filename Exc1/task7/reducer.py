#!/usr/bin/python

import sys

prev_student_id = ""
for line in sys.stdin:
    line = line.strip()
    items = line.split()
    student_id = items[0]
    if student_id!=prev_student_id:
        if prev_student_id!="":
            sys.stdout.write("\n")
        sys.stdout.write("{0} -->".format(items[2]))
        prev_student_id = student_id
    else:
        sys.stdout.write(" ({0},{1}) ".format(items[2],items[3]))

