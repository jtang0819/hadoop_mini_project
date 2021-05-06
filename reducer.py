#!/usr/bin/env python
import sys
# [Define group level master information]
vin = ''

def reset(line):
	# [Logic to reset master info for every new group]
	vin = ''
	make_and_year = ''
	# Run for end of every group


def flush():
	print(vin, make_and_year)
	# basically a print statement


# input comes from STDIN
for line in sys.stdin:
	# [parse the input we got from mapper and update the master info]
	# [detect key changes]
	line = line.split()
	current_vin = line[2]
	make_and_year = line[3, 5]
	if current_vin != vin:
		if current_vin is not None:
			# write result to STDOUT
			flush()	
		reset()
# [update more master info after the key change handling]

