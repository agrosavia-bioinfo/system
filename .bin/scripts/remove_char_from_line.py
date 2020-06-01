#!/usr/bin/python

"""
Remove a column from a multicolumn file
"""
import sys

delFile = open (sys.argv[1])
col = int (sys.argv[2])

for line in delFile:
	line = line.strip()
	if "ATOM" in line [:5]:
		line = line[:col-1] + line [col:]

	print line



