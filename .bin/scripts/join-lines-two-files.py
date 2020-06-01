#!/usr/bin/python
"""
Join the lines or fields of two related files (same ids)
"""

import sys

fileA = open (sys.argv[1])
fileB = open (sys.argv [2])

for lineA, lineB in zip (fileA, fileB):
	line = lineA.strip() + "\t" + lineB.split ()[1]
	print line


