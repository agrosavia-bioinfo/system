#!/usr/bin/python
"""
Change a filename by removing the spaces and uppercase
initial words
"""

import os, sys
filename = sys.argv [1]

filenameLst = list (filename)
newFilenameLst = []

i=0
while i < len (filenameLst):
	c = filenameLst [i]
	if c.isspace ():
		filenameLst [i+1] = filenameLst[i+1].upper()
	else:
		newFilenameLst.append (c)
	
	i += 1

newFilename = "".join (newFilenameLst)

cmm = 'mv "%s" %s' % (filename, newFilename)
print (cmm)
if raw_input ("Rename (y/N)?") == "y":
	os.system (cmm)
		
