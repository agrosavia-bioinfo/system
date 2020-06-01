#!/usr/bin/python

import os, sys

filestatus = "/tmp/mouse-status.txt"
value = 1
if os.path.exists (filestatus):
	value = int (open (filestatus).read())

if value == 1:
	os.system ("sudo rmmod psmouse")
	open (filestatus, "w").write ("0")
else:
	os.system ("sudo modprobe psmouse")
	open (filestatus, "w").write ("1")

