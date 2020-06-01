#!/usr/bin/python

import sys, os

configFilename = "/home/lg/tmp/dic.cfg"

word = ""
oldWord = ""
if len (sys.argv) > 1:
	word = sys.argv[1]
else:
	word = raw_input()

flag = ""
while word != "":
	if word == "-":
		word = oldWord
	elif word == "-snd":
		configFile = open (configFilename, "w").write("sound")
		word = raw_input()
		continue
	elif word == "-nsnd":
		configFile = open (configFilename, "w").write("nosound")
		word = raw_input()
		continue
	elif word == "-s":
		flag = " -r "
		word = raw_input()
		continue
	elif word == "-e":
		flag = ""
		word = raw_input()
		continue
		
	os.system ("i2e-cli "+ flag + word)
	try:
		configFile = open (configFilename)
		if (configFile.read() == "sound"):
			os.system ("espeak " + word)
			configFile.close()
	except IOError:
		None

	oldWord = word
	word = raw_input()
