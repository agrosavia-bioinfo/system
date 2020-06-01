#!/usr/bin/python

"Change the names of the current directory, filling it with zeros to the right"

import os, sys
import glob   # For use wildcars to select files

args = sys.argv
quality = 20   # 20%
files    = "*"  # All files

i=0
while i < len (args[1:]):
	if args [i] == "-q":
		quality = int (args [i+1])	
		i += 1
	elif args [i] == "-f":
		files = args [i+1]
		i += 1
	
	i += 1

print "Quality:", quality, "Files:", files
		
listOfFiles = glob.glob (files)
listOfCommands = []
for file in listOfFiles:
	name = file.split (".")[0]
	ext = file.split (".")[1]

	newName = name + "-low." + ext 

	command = "convert -quality %s %s %s " % (quality, file, newName) 
	listOfCommands.append (command)
	print command

if (raw_input ("\nExecute?\n") != "Y"): sys.exit (0)

for cmm in listOfCommands:
	print cmm
	os.system (cmm)
