#!/usr/bin/python

"""
Change the name of mp3 files in the current directory
"""

import os

files = os.listdir (".")

mp3Files = filter (lambda x: ".mp3" in x, files)

#mp3Files = [x.strip ("\n") for x in mp3Files]

print mp3Files

for i in mp3Files:
	print ">", i
	name = i.split (".") [0]
	parts = name.split (" - ")
	title = parts[0]
	author = parts[1]

	author = author.replace ("(", "")
	author = author.replace (")", "")
	author = author.replace (" ", "")

	newName = author + "-" +  title + ".mp3"

	print newName

	os.rename (i, newName)

