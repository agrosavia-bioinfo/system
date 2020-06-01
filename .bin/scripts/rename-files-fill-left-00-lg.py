#!/usr/bin/python

"Change the names of the current directory, filling it with zeros to the right"

import os

listOfFiles = os.listdir (".")
listOfPdbs = filter (lambda x: ".pdb" in x, listOfFiles)

for pdb in listOfPdbs:
	print pdb, 
	name = pdb.split (".")[0].split ("-")[1]
	newName = "c-" + name.zfill (5) + ".pdb"

	command = "mv " + pdb + " "  + newName
	print command
	os.system (command)
