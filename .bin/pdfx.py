#!/usr/bin/python

import os, sys

fullPath = sys.argv [1]
listPath = os.path.split (fullPath)
(path, prog) = (listPath[0], listPath[1])
os.chdir (path)
os.system ("PDFXCview.exe %s" % prog)

