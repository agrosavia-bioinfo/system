#!/usr/bin/python

import sys

filename = sys.argv[1]
linesLst = open (filename).readlines()

i = 0
while i < len(linesLst):
	lines = linesLst
	number = lines[i].split ()[0]
	comment= lines[i+2]

	print number,":"
	print comment

	i = i+3

