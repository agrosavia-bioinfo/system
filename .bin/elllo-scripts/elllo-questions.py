#!/usr/bin/python

"""
Download all the files from a range of podcasts of a elllo site
USAGE ell-all.py <Full Url + pagename>
"""
import os, sys

htmls = sys.argv[1]

listOfHtms = open (htmls).readlines()

for htm in listOfHtms:
	print "------------------------------------"
	fullHtml = htm.strip()

	name = htm.split ("/") [-1]
	name = name.split (".")[0]
	dir = name.split ("-",1)[1]

	print htm.strip(), "----", dir, fullHtml

	os.mkdir (dir)
	os.chdir (dir)

	cmm2="wget -nd %s" % fullHtml
	os.system (cmm2)

	cmm3 = "ello %s %s " % (os.path.basename (fullHtml), dir) 
	print cmm3
	os.system (cmm3)
	os.chdir ("..")
