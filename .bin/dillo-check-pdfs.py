#!/usr/bin/python

import os, time

observerdDir = "/home/lg/tmp/dillo"

openPdfs = []
while True:
	listofpdfs = os.listdir (observerdDir)
	for pdf in listofpdfs:
		if pdf not in openPdfs:
			os.system ("pdf %s/%s" % (observerdDir,pdf))
			openPdfs.append (pdf)
	time.sleep (3)

