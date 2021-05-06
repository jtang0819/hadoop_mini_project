#!/usr/bin/env python
import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.split()
    key = line[1]
    value = 1
    print('%s\t%s' % (key, value))

