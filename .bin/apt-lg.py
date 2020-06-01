#!/usr/bin/python

import sys, os

myfile = open (sys.argv[1])

for line in myfile:
	if "http" not in line:
		continue

	start = line.find ("http")
	end = len (line)

	url = line [start:end]

	cmm = "xdown " + url.strip()

	print (cmm)
	os.system (cmm)

