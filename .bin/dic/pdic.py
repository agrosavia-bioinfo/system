#!/usr/bin/python

import sys, os

word = ""
if len (sys.argv) > 1:
	word = sys.argv[1]
else:
	word = raw_input()

flag = ""
while word != "":
	if word == "-s":
		flag = " -r "
		word = raw_input()
		continue
	elif word == "-e":
		flag = ""
		word = raw_input()
		continue
		
	os.system ("i2e-cli "+ flag + word)
	word = raw_input()


