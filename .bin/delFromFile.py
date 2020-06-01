#!/usr/bin/python 

import os, sys

listOfFiles = sys.argv [1]

for f in listOfFiles:
	cmm = "rm %s" % f
	print cmm

option = raw_input ("Remove Yes/Not")

if option == "Yes":
	for f in listOfFiles:
		cmm = "rm %s" % f
		print cmm
		os.system (cmm)


