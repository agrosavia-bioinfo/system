#!/usr/bin/python

import sys, os

#processNumber = sys.argv [1]
processNumber = "6075"

processFile = "/home/lg/tmp/status-process.txt"
if not os.path.exists (processFile):
	open (processFile, "w").write ("stopped")
	
	
status = open (processFile).read()

if status == "stopped":
	os.system ("kill -CONT %s" % processNumber)
	status = "running"
else:
	os.system ("kill -STOP %s" % processNumber)
	status = "stopped"

open (processFile, "w").write (status)
