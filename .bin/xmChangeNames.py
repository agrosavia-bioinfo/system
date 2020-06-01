#!/usr/bin/python

USAGE="\
Generate commands to change a substring from files within a directory\n\
USAGE: APP <old-substring> <new-substring> <file pattern> \n"

import os, sys
from multiprocessing import Pool 

if len (sys.argv) < 2:
	print USAGE
	sys.exit (0)

oldname = sys.argv [1]
newname = sys.argv [2]
pattern = sys.argv [3]

nCores = 1
if len (sys.argv) > 4:
	nCores = int (sys.argv [4])

filelist = filter (lambda x: pattern in x, os.listdir ("."))
filelist = filter (lambda x: oldname in x, filelist)

cmmList = []
for filename in filelist:
	newFilename = filename.replace (oldname, newname)

	cmm = 'mv "%s" "%s"' % (filename, newFilename)
	cmmList.append (cmm)

for i in cmmList[0:5]:
	print  (i)
print ("....")
for i in cmmList[-5:]:
	print  (i)

x=raw_input(">>> Continue (y/N)")	
if (x!="y"):
	sys.exit (0)
	
#print (cmmList)
#print len (cmmList)

pool = Pool (processes=nCores)   
pool.map (os.system, cmmList)
pool.close ()
pool.join ()

#input (">>>")	  

