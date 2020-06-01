#!/usr/bin/python
import os, sys


while True:
	word = raw_input ("Word to speech >> ")
	
	cmm1 = "echo %s|xclip -i" % word 
	os.system (cmm1)
	cmm = "lg-espeak.sh 2>1 /dev/null &" 
	os.system (cmm)
