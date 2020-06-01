#!/usr/bin/python

# Display a terminal to receive words and translate them using  "i2e-cli" .
# Aditionally uses "espeak" to pronounce the work
# Two options -e (defautl) for english, -s for spanish
# Another option: digit a number and the words in this line number will be
# writen to the file "words.txt" used by the puzzle of words "JDic"

##########################################################################
# Get the line at line number and add to the file of words using "jadd"
##########################################################################

import sys
##########################################################################
def runApplication (arguments):
	if arguments == "":
		sys.exit(0)

	listOfArguments = arguments.split()

	fileOfResults = open ("b")
	listOfFiles = fileOfResults.readlines()

	
	application = listOfArguments[0]
	lineNumber = int (listOfArguments[1])
	filename = listOfFiles [lineNumber -1].strip()

	if application == "cp":
		command = application + " " + filename + " ."
	elif application == "ln":
		command = application + " -s " + filename
	elif application == "cd":
		oldDir = filename.split("/")[:-1]
		newDir = ""
		for dir in oldDir:
			newDir += dir + "/"

		os.chdir (newDir)
		command = "x"
	else:
		command = application + " " + filename

	print command
	os.system (command)
##########################################################################

import sys, os

word = sys.argv[1]
command = "locate " + word
for filter in sys.argv[1:]:
	command += "|grep " + filter

os.system (command + "> b")

os.system ("cat b")
print ">>",
arguments = raw_input()
runApplication (arguments)

