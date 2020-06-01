#!/usr/bin/python

"""
Remove a column from a multicolumn file
"""
import sys

delFile = open (sys.argv[1])
col = int (sys.argv[2])

for line in delFile:
	listLine = line.split ()
	listLine.pop (col - 1)
	newLine = reduce (lambda x,y:str (x)+"\t"+str(y), listLine)

	print newLine



