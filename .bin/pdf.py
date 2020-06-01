#!/usr/bin/python
import os, sys

args = sys.argv
option = args [1]
pdfOptionFile = "/home/lg/tmp/config/pdfoption"

if "-" in option[0]:
	pdfFile = open (pdfOptionFile, "w")
	pdfFile.write (args[1][1:])
	sys.exit ()
	
fileName = option

option = ""
if len (args) > 2:
	option = args [2]	
	pdfFile = open (pdfOptionFile, "w")
	pdfFile.write (option)
elif os.path.exists (pdfOptionFile):
	option = open (pdfOptionFile).readline()
else:
	option = "m"

cmm = ""
if 'V' in option:
	cmm = 'ViewPDF "%s" 2> /dev/null &' % fileName
elif '1' in option:
	cmm = 'qpdfview "%s" 2> /dev/null &' % fileName
elif 'z' in option:
	cmm = 'zathura "%s" 2> /dev/null &' % fileName
elif 'm' in option:
	#cmm = 'mupdf -G -r 100 "%s" 2> /dev/null &' % fileName
	#cmm = 'mupdf -G -r 50 "%s" 2> /dev/null &' % fileName
	cmm = 'mupdf -A 0 -G -r 50 "%s" 2> /dev/null &' % fileName
elif 'r' in option:
	cmm = 'mupdf -G -r 100 "%s" 2> /dev/null &' % fileName
elif 'M' in option:
	cmm = 'mupdf -G -r 50 "%s" 2> /dev/null &' % fileName
elif "g" in option:
	cmm = 'gpicview "%s" 2> /dev/null &' % fileName
elif "e" in option:
	cmm = 'epdfview "%s" 2> /dev/null &' % fileName
elif "v" in option:
	cmm = 'evince "%s" 2> /dev/null &' % fileName
elif 'o' in option:
	#cmm = 'okular "%s" 2> /dev/null &' % fileName
	#cmm = '/usr/bin/okular "%s"' % fileName
	cmm  = "xokular.sh '%s'" % fileName
	open ("/tmp/a", "w").write (cmm)
elif 'a' in option:
	cmm = 'acroread -openInNewInstance "%s" 2> /dev/null &' % fileName
	#cmm = 'acroread  "%s" 2> /dev/null &' % fileName
elif 'k' in option:
	cmm = 'konqueror "%s" 2> /dev/null &' % fileName
elif 'q' in option:
	cmm = 'qpdfview "%s" 2> /dev/null &' % fileName
elif 'i' in option:
	cmm = 'inkscape "%s" 2> /dev/null &' % fileName
elif 'x' in option:
	winFilename = "Z:%s" % fileName.replace ("/", "\\")
	#cmm = 'PDFXCview.exe "%s" 2> /dev/null &' % winFilename
        cmm= 'wine "/home/lg/.wine/drive_c/Program Files/Tracker Software/PDF Viewer/PDFXCview.exe %s" 2> /dev/null &' % filename
else:
	cmm = 'mupdf -A 0 "%s" 2> /dev/null &' % fileName

print cmm
os.system (cmm)
