#!/usr/bin/python

# Imports
import os, re, threading, sys, getopt
from subprocess import check_output
from subprocess import call

class Cownet:
	# Make some variables
	inBytes = 0
	outBytes = 0

	def __init__(self, interface = "en1", pause = 30):
		self.interface = interface

		# Get the response from netstat and break it up by row
		ns =  check_output(["netstat", "-ib"])
		ns = ns.split('\n')

		# Look through each row
		for row in ns:
			# Clean up and break up each row further
			row = re.sub('\s+', ' ', row).strip()
			row = row.split(' ')

			# Check for the matching interface, and save the data
			if row[0] == self.interface:
				self.inBytes += int(row[6])
				self.outBytes += int(row[9])
				break

		# Build string and pass to cowsay
		self.say = "Received " + self.sizeof_fmt(self.inBytes) + "   /   Sent " + self.sizeof_fmt(self.outBytes)

		self.cowSayWhat()

	# Turn raw numbers to user friendly strings
	def sizeof_fmt(self, num):
		for x in ['bytes','KB','MB','GB','TB']:
			if num < 1024.0:
				return "%3.1f %s" % (num, x)
			num /= 1024.0

	def cowSayWhat(self):
		threading.Timer(5.0, self.cowSayWhat).start()
		os.system('clear')
		call(["cowsay", self.say])

cn = Cownet()