#!/usr/bin/python

import time, os

while True:
	prozCommand = 'echo r | proz "http://ufpr.dl.sourceforge.net/project/ubuntu-eee/Easy Peasy/1.5/easypeasy-1.5.img.iso"'
	print prozCommand
	os.system (prozCommand)

	idCommand = "ps -C bash | tail -1 | cut -d " " -f1"
	print (idCommand)

	time.sleep (55)

	killCommand = "kill -9 " + idCommand
	print (killCommand)

