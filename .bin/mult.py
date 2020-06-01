#!/usr/bin/python

GOAL="Apply a command to multiple files \n\n\
USAGE: mult.py <command> <files>\n"

import os, sys

args = sys.argv
dir = "./"

if len (args) < 2:
	print GOAL
	sys.exit (0)

cmm = sys.argv [1]
pattern = sys.argv [2]
if (len (args) > 3): 
	dir = args [3]

files = filter (lambda x:pattern in x, os.listdir (dir))
files = sorted (files)

for i in files:
	fullCommand = cmm + " " + dir + i + " &"
	#fullCommand =  "feh -g 500x600 "+ i + " &"
	#fullCommand =  "convert -quality 20 "+ i + "  " + i +" &"
	#fullCommand =  "vlow " + i

	print (fullCommand)
	os.system (fullCommand)


