#!/usr/bin/python

"Change the names of the current directory, filling it with zeros to the right"

import os

listOfFiles = filter (lambda x: ".pl" in x, os.listdir("."))

for file in listOfFiles:
	name = file.split (".")[0]
	newName = name + ".html"

	command = "mv " + file + " "  + newName
	print command
	os.system (command)
