#!/usr/bin/python

# Call from vim when editing latex document (childs with input)
# Create the latex structure and adds the lines, and call pdflatex, y pdfview

import sys, os
import commands
#-----------------------------------------------------------------------
def getCurrentPdfReaderStr():
	lines = open ("/home/lg/.bin/pdf").readlines()

	for i in lines:
		if "#" in i:
			continue
		else:
			return i.split ('"')[0]
#-----------------------------------------------------------------------

args = sys.argv
inFile = args[1]

outFile = "tmp-" + inFile
outName = outFile.split(".")[0]
source = open (outFile, "w")

# Create tmp tex document
#source.write ("\documentclass[12pt,spanish]{article}\n")
source.write ("\documentclass[12pt,spanish]{letter}\n")
source.write ("\usepackage[T1]{fontenc}\n")
source.write ("\usepackage[latin1]{inputenc}\n")
source.write ("\usepackage{babel}\n")
source.write ("\\addto\shorthandsspanish{\spanishdeactivate{~<>}}\n")
#source.write ("\\renewcommand{\\familydefault}{\sfdefault}\n")
#source.write ("\usepackage[T1]{fontenc}\n")
#source.write ("\usepackage{ae,aecompl}\n")
#source.write ("\usepackage{epstopdf}\n")
source.write ("\\begin{document}\n")

lines = open (args [1])
for l in lines:
	source.write (l)

source.write ("\end{document}\n")
source.close()

status = os.system ("pdflatex " +  outFile)

# Check if error
if status != 0:
	sys.exit (0) 

output = commands.getoutput ('ps -af')

strPdf = getCurrentPdfReaderStr ()
str = strPdf + outName
if not str in output:
	cmm = "pdf " +  outName + ".pdf 2> /dev/null & "
	os.system (cmm)

import time
time.sleep (0.05)
os.system ("cleanltx > /dev/null")
os.system ("ltx > /dev/null &")
