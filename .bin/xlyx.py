#!/usr/bin/python

import os

lines = open ("/home/lg/.lyx/session").readlines()
lastDoc = lines [4]

cmm = "lyx %s" % lastDoc
print (cmm)
os.system (cmm)
