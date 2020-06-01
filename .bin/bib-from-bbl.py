#!/usr/bin/python
"""
Select the bibtex items from the .bbl file generated from 
latex from a full bibtex file.
"""
import sys

#############################################
def keyInLine (keys, line):
	for k in keys:
		if k in line:
			return True
	return False
#############################################

args = sys.argv
bibFilename = args [1]
bblFilename = args [2]
newBibFilename = bibFilename.split(".")[0]+"-new.bib"

keys = []
for line in open (bblFilename):
	if "bibitem" in line:
		k = line.split("{")[1].split("}")[0]
		keys.append (k)

bibOneLine = open (bibFilename).read ()
bibArticles = bibOneLine.split ("@")

newBibFile = open (newBibFilename, "w")
for line in bibArticles:
	if keyInLine (keys, line):
		newBibFile.write ("@"+line)

		
