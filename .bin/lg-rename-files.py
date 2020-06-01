#!/usr/bin/python

"""
Change the names of files within a directory
USAGE: oldName newName pattern
"""
import os, sys

USAGE="xrename <oldaName> <newName> <pattern>"

if (len (sys.argv) < 4):
    print USAGE
    sys.exit (0)

oldname = sys.argv [1]
newname = sys.argv [2]
pattern = sys.argv [3]


filelist = filter (lambda x: pattern in x, os.listdir ("."))

newFilelist = []
for filename in filelist:
	if oldname in filename:
		newFilelist.append (filename)
		newFilename = filename.replace (oldname, newname)

for filename in filelist:
	newFilename = filename.replace (oldname, newname)
	print "mv %s %s" % (filename, newFilename)

