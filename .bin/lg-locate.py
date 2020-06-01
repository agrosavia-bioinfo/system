#!/usr/bin/python

# Display a terminal to receive words and translate them using  "i2e-cli" .
# Aditionally uses "espeak" to pronounce the work
# Two options -e (defautl) for english, -s for spanish
# Another option: digit a number and the words in this line number will be
# writen to the file "words.txt" used by the puzzle of words "JDic"

# Version 2.1 (Mar-2015)
	# Added 'q' to quit
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

	if application == "ln":
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
	elif application == "cp":
		command = "cp %s ." % filename
	else:
		command = '%s "%s"' % (application, filename)

	print command
	os.system (command)

#---------------------------------------------------------------------
# Print lines from linesOfFindings excluding them with the words in
# excludeWords
#---------------------------------------------------------------------
def printLines (linesOfFindings, excludeWords, includeWords):
	listOfLines = []
	listOfLinesFiltered = []
	for line in linesOfFindings:
		line = line.strip()
		if excludeWords == []:
			listOfLines.append (line)
			print len (listOfLines), line
		else:
			notIsIn = False
			for word in excludeWords:
				notIsIn = notIsIn or (word in line)

			isIn = False
			for word in includeWords:
				isIn = isIn or (word in line)

			#print ">>>", isIn, notIsIn
			if notIsIn == False: 
				listOfLines.append (line)
				print len (listOfLines), line
			elif isIn == True:
				listOfLinesFiltered.append (line)
				print len (listOfLinesFiltered), line

	return listOfLines
	
#---------------------------------------------------------------------

import sys, os

word = sys.argv[1]
excludeWords = ["vim/view/~"]
includeWords = []
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

print command
os.system (command + "> /tmp/b")
fileOfFindings = open ("/tmp/b")
linesOfFindings = fileOfFindings.readlines()
os.system ("rm /tmp/b")

while True:
	listOfLines = printLines (linesOfFindings, excludeWords, includeWords)
		
	print ">>",
	listOfArguments = raw_input().split()
	if listOfArguments == []:
		None
	elif (listOfArguments[0][0] == "."):
		sys.exit (0)
	elif (listOfArguments[0][0] == "q"):
		sys.exit (0)
	elif (listOfArguments[0][0] == "-"):
		excludeWords = excludeWords + map (lambda x: x[1:], listOfArguments)
		excludeWords.append (listOfArguments[0][1:])
	elif (listOfArguments[0][0] == "+"):
		includeWords = includeWords + map (lambda x: x[1:], listOfArguments)
		includeWords.append (listOfArguments[0][1:])
	else:
		runApplication (listOfArguments, listOfLines)

