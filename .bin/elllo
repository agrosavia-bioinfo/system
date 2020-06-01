#!/usr/bin/python
### Download mp3 files from the english ello site"
### USAGE: ello.py <source of SAVED ello page> <title for sufix files>
### EXAMPLE: elllo.py 1024-Monica-Books.htm edu

import os, sys
import urlparse

inputFile = sys.argv [1]
title = sys.argv [2]

#cmm1 = '/bin/grep -o \'\\"[^"]*"\' %s |grep mp3|grep "[.][.]"|sed "s/[.][.]\\/[.][.]/http:\\/\\/www.elllo.org/g"|sed "s/\\"//g" > b ' % inputFile
cmm1 = '/bin/grep -o \'\\"[^"]*"\' %s |grep [.]mp3|sed "s/[.][.]\\/[.][.]/http:\\/\\/www.elllo.org/g"|sed "s/\\"//g" > b ' % inputFile
print cmm1
os.system (cmm1)

lines = open("b").readlines()

listOfFiles = filter (lambda x: "mp3" in x, lines)
listOfNames = map (lambda x: os.path.basename (x).strip(), lines)

savedList, n = [], 0
for urlMp3 in listOfFiles:
	basename = os.path.basename (urlMp3).strip() 
	if basename in savedList:
		continue

	if "http" not in urlMp3:
		url = urlparse.urlparse (listOfFiles[0])[1]
		urlMp3 = "http://" + url + urlMp3
	elif "=" in urlMp3:
		urlMp3 = "http" + urlMp3.split ("http")[1]
	
	newName = title + str(n).zfill (2) + "-" + basename.split ("-",1)[1]

	cmm2 = "axel -q %s -o %s" % (urlMp3.strip(), newName) 
	print ">>>> cmm2: " + cmm2

	os.system (cmm2)

	savedList.append (basename)
	n += 1

os.remove ("b")





