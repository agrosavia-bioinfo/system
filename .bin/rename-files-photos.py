#!/usr/bin/python

"Change the names of the current directory, filling it with zeros to the right"

import os

listOfFiles = filter (lambda x: "-" in x, os.listdir("."))

k=1
title = "Troy-Marzo02-"
for photo in listOfFiles:
	name = photo.split ("02-")[0]
	newname = name + "02-"+ str(k).zfill(2) + ".jpg"
	#number = tail.split (".")[0]
	#newname = tail

	
	command = "mv " + photo + " "  + newname

	print command 
	k = k + 1

	#fullname = file.split (".")[0]
	#name = "Troy-Marzo02-low-" + str(k).zfill(2) 
	#stemName = file.split ("JPG.")[1]
	#newName = name + ".jpg"

	#command = "mv " + file + " "  + newName
	#command = "convert -quality 20 " + file + " " + newName
	#print command
	#os.system (command)
