#!/usr/bin/python

## Load multiple files (PDFs) with the same command (mupdf)

import os, sys

COMODIN = sys.argv[1]

listOfPDFs = filter (lambda x: COMODIN in x, os.listdir("."))

for pdf in listOfPDFs:
	os.system ("mupdf %s &" % pdf)
