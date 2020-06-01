#!/usr/bin/python

USAGE="\
Upper the first letter of composed filenamed from a dir"


import os, sys

if len (sys.argv) < 2:
    print USAGE
    sys.exit (0)

pattern = sys.argv [1]

flag = ""
if len (sys.argv) > 4:
	flag = sys.argv [4]



filelist = filter (lambda x: pattern in x, os.listdir ("."))

for filename in filelist:
    wordList = filename.split (" ")
    wordListNew = []
    for w in wordList:
        nw = w[0].upper()+w[1:]
        wordListNew.append (nw)

    newFilename = " ".join (wordListNew)
    cmm = 'mv "%s" "%s"'  % (filename, newFilename)
    print cmm

