#!/usr/bin/python
"""
Join the lines or fields of two related files (same ids)
"""

import sys

fileA = open (sys.argv[1])
fileB = open (sys.argv [2])

for lineA, lineB in zip (fileA, fileB):
	tailLineA = lineB.split () [-2:]

	line = lineA.strip() + "\t" + tailLineA[0] + "\t" + tailLineA[1]
	print line


