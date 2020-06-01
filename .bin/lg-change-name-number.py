#!/usr/bin/python

USAGE="\
Change the filename by filling a number with 0's\n\
USAGE: APP <pattern> <token> <pos token> <fill number format> \n"

import os, sys

if len (sys.argv) < 2:
	print USAGE
	sys.exit (0)

pattern  = sys.argv [1]
token    = sys.argv [2]
posToken = int (sys.argv [3])
nFill    = int (sys.argv [4])

flag = ""
if len (sys.argv) > 4:
	flag = sys.argv [4]

filelist = filter (lambda x: pattern in x, os.listdir ("."))

for filename in filelist:
	strLst = filename.split (token)
	strNumber = strLst [posToken]
	strNumberFilled = strNumber.zfill (nFill)

	newFilename = filename.replace (strNumber, strNumberFilled)

	cmm = "mv %s %s" % (filename, newFilename)
	print cmm

