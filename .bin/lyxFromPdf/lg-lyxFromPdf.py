#!/usr/bin/python

# Create a lyx file from a graphics file (.pdf, .png, ..)
# To text margins and boundaries and presentation

import os, sys

args = sys.argv

graphicsFilename = args[1]
lyxFilename = graphicsFilename.split (".")[0] + ".lyx"

lyxFile = open (lyxFilename, "w")

lyxSource = "/home/lg/.bin/lyxFromPdf/a.lyx"
for line in open (lyxSource):
	if "filename" in line:
		lyxFile.write ("filename " + graphicsFilename + "\n")
		continue

	lyxFile.write (line)
	
		
