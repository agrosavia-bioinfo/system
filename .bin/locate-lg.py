#!/usr/bin/python

# Display a terminal to receive words and translate them using  "i2e-cli" .
# Aditionally uses "espeak" to pronounce the work
# Two options -e (defautl) for english, -s for spanish
# Another option: digit a number and the words in this line number will be
# writen to the file "words.txt" used by the puzzle of words "JDic"

# Version 2.0
# You can exclude words appending "-" before the pattern

##########################################################################
# Get the line at line number and add to the file of words using "jadd"
##########################################################################

import sys
#######################################################################
def getPath (filenamePath):
	oldDir = filenamePath.split("/")[:-1]
	newDir = "/".join (oldDir)

	return newDir
#######################################################################
def runApplication (listOfArguments, listOfFilenames):
	if len (listOfArguments) == 0:
		sys.exit(0)
	elif len (listOfArguments) == 1:
		listOfArguments.append (1)

	application = listOfArguments[0]
	lineNumber = int (listOfArguments[1])
	filename = listOfFilenames [lineNumber -1]

	if application == "cp":
		command = application + " '" + filename + "' ."
	elif application == "ln":
		command = application + " -s " + filename
	elif application == "cd":
		newDir = getPath (filename)
		os.chdir (newDir)
		command = "/bin/bash"
	elif application == "mc":
		newDir = getPath (filename)
		command = "mc " + newDir
	elif application == "hot":
		newDir = getPath (filename)
		command = "hot " + newDir
	elif application == "px":
		newDir = getPath (filename)
		command = "/home/lg/.bin/px " + newDir + " "
	else:
		command = application + " " + '"' + filename + '"'

	print ">>>", command, "<<<<"
	os.system (command)

#---------------------------------------------------------------------
# Print lines from linesOfFindings excluding them with the words in
# excludeWords
#---------------------------------------------------------------------
def printLines (linesOfFindings, excludeWords):
	listOfLines = []
	for line in linesOfFindings:
		line = line.strip()
		if excludeWords == []:
			listOfLines.append (line)
			print len (listOfLines), line
		else:
			notIsIn = False
			for word in excludeWords:
				notIsIn = notIsIn or (word in line)

			if notIsIn == False:
				listOfLines.append (line)
				print len (listOfLines), line

	return listOfLines
	
#---------------------------------------------------------------------

import sys, os

word = sys.argv[1]
excludeWords = ["vim/view/"]
command = "locate -i " + word
for filter in sys.argv[2:]:
	if filter[0] == "-":
		excludeWords.append (filter[1:])
	elif filter [0] == ".":
		command += "|grep -i [.]" + filter[1:]
	elif filter.isdigit() :
		print "isDig"
		command += '|grep -i "%s" ' % filter
	else:
		command += "|grep -i " + filter

os.system (command + "> /tmp/b")
fileOfFindings = open ("/tmp/b")
linesOfFindings = fileOfFindings.readlines()
os.system ("rm /tmp/b")

while True:
	listOfLines = printLines (linesOfFindings, excludeWords)
		
	print ">>",
	listOfArguments = raw_input().split()
	if listOfArguments == []:
		continue

	if (listOfArguments[0] == "q"):
		sys.exit (0)
	if (listOfArguments[0][0] == "-"):
		excludeWords = excludeWords + map (lambda x: x[1:], listOfArguments)
		excludeWords.append (listOfArguments[0][1:])
	elif (listOfArguments[0][0] == "."):
		None
	else:
		runApplication (listOfArguments, listOfLines)

