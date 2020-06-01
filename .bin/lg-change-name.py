#!/usr/bin/python

USAGE="\
Generate commands to change a substring from files within a directory\n\
USAGE: APP <old-substring> <new-substring> <file pattern> \n"

import os, sys

if len (sys.argv) < 2:
	print USAGE
	sys.exit (0)

oldname = sys.argv [1]
newname = sys.argv [2]
pattern = sys.argv [3]

flag = ""
if len (sys.argv) > 4:
	flag = sys.argv [4]

filelist = filter (lambda x: pattern in x, os.listdir ("."))
 
lst = []
for filename in filelist:
	if flag == "-pre":
		newFilename = "%s-%s" % (oldname, filename)
	else:
		newFilename = filename.replace (oldname, newname)

	cmm = "mv %s %s" % (filename, newFilename)
	lst.append (cmm)

response = raw_input ("Execute commands? " ) 
for cmm in lst:
	print cmm
	if response == "y":
		os.system (cmm)

