#!/usr/bin/python

import os, sys

args = sys.argv

f = args [1]
newF = f.split(".")[0]+"-small.pdf"
cmm = "convert -density 200x200 -quality 300 -compress jpeg %s %s" % (f, newF)
print cmm
os.system (cmm)



