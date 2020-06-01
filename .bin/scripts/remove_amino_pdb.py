#!/usr/bin/python

"""
Remove an Amino acid type from a PDB file
"""
import sys

file = open (sys.argv[1])
amino = sys.argv[2]

for line in file:
	line = line.strip()
	if "ATOM" in line [:5]:
		if amino in line:
			continue

	print line

