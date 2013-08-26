#!/usr/bin/python

# Imports
import re
from subprocess import check_output
from subprocess import call

# Turn raw numbers to user friendly strings
def sizeof_fmt(num):
	for x in ['bytes','KB','MB','GB','TB']:
		if num < 1024.0:
			return "%3.1f %s" % (num, x)
		num /= 1024.0


# Make some variables
inBytes = 0
outBytes = 0
interface = "en1"

# Get the response from netstat and break it up by row
ns =  check_output(["netstat", "-ib"])
ns = ns.split('\n')

# Look through each row
for row in ns:
	# Clean up and break up each row further
	row = re.sub('\s+', ' ', row).strip()
	row = row.split(' ')

	# Check for the matching interface, and save the data
	if row[0] == interface:
		inBytes += int(row[6])
		outBytes += int(row[9])
		break

# Build string and pass to cowsay
say = "Received " + sizeof_fmt(inBytes) + "   /   Sent " + sizeof_fmt(outBytes)
call(["cowsay", say])