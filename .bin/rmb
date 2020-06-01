#!/usr/bin/python

import os

files = os.listdir(".")
bibFiles = filter (lambda x: ".bib" in x, files)

for bib in bibFiles:
	if bib in ["Proteins.bib", "Scripting.bib"] :
		continue
	print bib
	os.remove (bib)

