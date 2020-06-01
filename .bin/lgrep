#!/usr/bin/python

# lgrep <lineNumber> <application>
# Uses as a pipe to run aplication with standard output from other pipe programs
#
# example:
# locate pdf|grep proteins|lgrep 3 acroread

import sys, os

#################################################3
def runApplication (line, application):
	if application == "": 
		extension = line.strip().split (".") [-1]
		print line, extension
		if extension == "pdf": 		application =  "evince"
		elif extension == "html": 	application =  "opera"
		elif extension == "lyx": 	application =  "lyx"
		elif extension == "txt": 	application =  "gedit"
		else: application = "xed"

	command = application + " " + line
	print command
	os.system (command)

#################################################3
numberLine = 1
application = ""

if len (sys.argv) == 2:
	if type (sys.argv [1]) is int: 
		numberLine = int (sys.argv [1])
	else: 
		application = sys.argv [1]

elif len (sys.argv) == 3:
	numberLine = int (sys.argv [1])
	application = sys.argv [2]

f = sys.stdin

i=1
for line in f:
	if i == numberLine :
		runApplication (line, application)
		exit (0)
	i += 1


