#!/usr/bin/python

import sys, os

cpid = os.getpid()

cmm2 = "lgps " + sys.argv [1] + " > /tmp/b"
os.system (cmm2)

for process in open("/tmp/b"):
	pid = int (process.split()[1])
	if pid < cpid:
		print ">>>",  process.strip()

response = raw_input ("kill all of them ?")
if response != "y":
	sys.exit (0)

for process in open("/tmp/b"):
	pid = int (process.split()[1])
	if pid < cpid:
		cmd = "kill -9 " + str(pid)
		print cmd
		os.system (cmd)

