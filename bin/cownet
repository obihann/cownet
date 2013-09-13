#!/usr/bin/python

# Imports
import os, re, threading, sys, getopt, time
from subprocess import check_output
from subprocess import call

# The brains
class Cownet:
	def __init__(self, interface, delay):
		self.interface = interface
		self.delay = delay

		while(True):
			self.loadNetData()
			self.cowSayWhat()
			time.sleep(self.delay)

	def loadNetData(self):
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
				self.inBytes = int(row[6])
				self.outBytes = int(row[9])
				break

		# Build string and pass to cowsay
		self.say = "Received " + self.sizeof_fmt(self.inBytes) + "   /   Sent " + self.sizeof_fmt(self.outBytes)

	def cowSayWhat(self):
		os.system('clear')
		call(["figlet", "cownet"])
		call(["cowsay", self.say])

	# Turn raw numbers to user friendly strings
	def sizeof_fmt(self, num):
		for x in ['bytes','KB','MB','GB','TB']:
			if num < 1024.0:
				return "%3.1f %s" % (num, x)
			num /= 1024.0

# The main class to handle threads, and inputs
class Main:
	# Setup some default varialbes
	interface = "en1"
	delay = 30.0

	def __init__(self, argv):
		# Check for command line arguments
		try:
			opts, args = getopt.getopt(argv,"hi:d:",["help", "interface=","delay="])
		except getopt.GetoptError:
			print 'cownet.py -i <interface> -d <delay>'
			sys.exit(2)

		for opt, arg in opts:
			if opt == '-h':
				print 'cownet.py -i <interface> -d <delay>'
				sys.exit()
			elif opt in ("-i", "--interface"):
				self.interface = arg
			elif opt in ("-d", "--delay"):
				self.delay = float(arg)

		cowThread = threading.Thread(target = self.startThreads)
		cowThread.daemon = True
		cowThread.start()

		try:
			time.sleep(1000)
		except KeyboardInterrupt:
			print '\nGoodbye!'

	def startThreads(self):
		Cownet(self.interface, self.delay)

if __name__ == "__main__":
	main = Main(sys.argv[1:])