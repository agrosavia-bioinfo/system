#!/usr/bin/python

"""
Move files from an input file archive to a directory
USAGE: move_files <list of filenames file> 
"""

import os, sys

listOfFiles = open (sys.argv [1])

for f  in listOfFiles:
	cmm = "mv %s random_pdbs" % (f.strip().split(":")[1])
	print cmm
	os.system (cmm)

