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
	workingDir = os.getcwd ()
	os.chdir (subdir)
	listOfFiles = os.listdir (".")
	for file in listOfFiles:
		if  "min.pdbs.tar.gz" in file:
			continue
		else:
			cmm = "rm -rf %s" % file
			print cmm
			os.system (cmm)
	os.chdir (workingDir)

