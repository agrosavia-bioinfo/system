#!/usr/bin/python

import os

obsDir = "/home/lg/downloads/pdfs"
os.chdir (obsDir)

files = sorted (os.listdir (obsDir), key=os.path.getctime)
lastFile = files [-1]
print lastFile
os.system ('pdf "%s"' % lastFile)

