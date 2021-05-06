#!/usr/bin/env python
import sys
# [Define group level master information]

make_and_year = ''
make_and_year_count = []

def reset(line):
    # [Logic to reset master info for every new group]
    make_and_year = ''
    make_and_year_count.clear()
    # Run for end of every group


def flush():
    print(current_make_and_year, sum(make_and_year_count))
    # print out key, value pair; value is sum of all of make_and_years that are the same... /
    # this is assuming data is sorted


# input comes from STDIN
for line in sys.stdin:
    # [parse the input we got from mapper and update the master info]
    # [detect key changes]
    line = line.split()
    current_make_and_year = line[0]
    make_and_year_count.append(line[1])
    if current_make_and_year != make_and_year:
        if current_make_and_year is not None:
            # write result to STDOUT
            flush()
        reset()
# [update more master info after the key change handling]

