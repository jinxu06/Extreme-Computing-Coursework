#!/usr/bin/python

import sys

for line in sys.stdin:
    sys.stdout.write(line.upper()) # avoid string strip to save memory and no newline added


