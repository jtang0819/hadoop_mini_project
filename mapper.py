#!/usr/bin/env python
import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    key = line[1]
    value = line[0, 3, 5]
    print('%s\t%s' % (key, value))

