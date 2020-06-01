#!/usr/bin/python
import os

while (True):
	url = raw_input(">")
	cmm = "axel http://www.bioinfbook.org/"+url+" > errors.log &"
	print (cmm)
	os.system (cmm)
