#!/usr/bin/python

"""
Download all the files from a range of podcasts of a elllo site
USAGE ell-all.py <Full Url + pagename>
"""
import os, sys

html = sys.argv[1]

#cmm1 = 'grep english %s |grep -o \'\"[^"]*"\'|grep 0951|grep htm|sed \'s/"//g\' > b' % html
cmm1 = 'grep english %s |grep -o \'\"[^"]*"\'|grep htm|sed \'s/"//g\' > b' % html

print cmm1
os.system (cmm1)

listOfHtms = open ("b").readlines()

lastHtm = ""
for htm in listOfHtms:
	if (htm == lastHtm):
		continue

	print ">>>", htm
	name = htm.split ("/") [-1].split (".")[0]
	dir = name.split ("-",1)[1]

	fullHtml = htm

	print ">>> NAME, DIR, HTML: ", name, ">>>", dir, ">>>", fullHtml

	os.mkdir (dir)
	os.chdir (dir)

	cmm2="wget -nd %s" % fullHtml
	os.system (cmm2)

	print ">>>>>>>>>>>>>>", dir
	cmm3 = "elllo %s %s " % (os.path.basename (fullHtml).strip(), dir) 
	print ">>>>> cmm3: ", cmm3
	os.system (cmm3)
	os.chdir ("..")

	lastHtm = htm
