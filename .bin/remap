#!/usr/bin/python

import sys, os

keyNumber = sys.argv [1]
keyString = ""
for i in sys.argv [2:]:
	keyString += i + " "

command = 'xmodmap -e "keycode %s = %s"' % (keyNumber, keyString)
print command
os.system (command)
