#!/usr/bin/python

import os, sys

args = sys.argv

var = "PATH"
if len (args) > 1:
	var = args[1]

env = os.getenv (var)
profileList = env.split (":")

for i in profileList:
	print i
