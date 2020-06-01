#!/usr/bin/python

"""
Move files from an input file archive to a directory
USAGE: move_files <list of filenames file> 
"""

import os, sys

listOfDirs = os.listdir (".")

for dir in listOfDirs:
	cmm = "cd %s;rmdir rigidity" % (dir)
	print cmm
	os.system (cmm)

