#!/usr/bin/python

import sys

file = open (sys.argv [1])

for line in file:
	line = line.strip()
	if "ATOM" in line[:5]:
		type = line [13]
		line = line + " " + type 
	print line



