#!/usr/bin/python

USAGE =  "process-dir <subdir>\n"
USAGE += "Process the files or directories of a parent dir"

import os, sys

if len (sys.argv) < 2:
	print USAGE
	sys.exit (0)

parentDir = sys.argv [1]

listOfDirs = os.listdir (parentDir)

os.chdir (parentDir)
for subdir  in listOfDirs:
	if not os.path.isdir (subdir):
		continue

	workingDir = os.getcwd ()
	os.chdir (subdir)
	listOfFiles = os.listdir (".")
	for file in listOfFiles:
		cmm = "some_command %s" % file
		print cmm
		os.chdir (workingDir)

