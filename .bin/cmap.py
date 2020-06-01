#!/usr/bin/python

import os, sys
args = sys.argv

filename = args [1]

cmm = "bin %s" % filename 
print ">>>", cmm
os.system (cmm)

binName = filename.split (".")[0] + "b" + ".mat"

os.system ("img %s" % binName)

imgName = binName.split (".")[0] + ".png"

#cmm = "feh -g 400x400 --title `basename %s` -Z %s" % (imgName, imgName)
cmm = "feh -g 400x400 --title `basename %s` -Z %s" % (imgName, imgName)
print ">>>", cmm
os.system (cmm)
