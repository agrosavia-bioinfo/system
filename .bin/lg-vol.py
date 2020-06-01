#!/usr/bin/python

# Change volume --see alsamixer--
# With parameter + raise, - lower, n: increments at n (n between 0..9)

MAX = 100
INCREMENT = 10

import os, sys

if len (sys.argv) == 1:
	currentValue = int (open ("/home/lg/.bin/volume/vol.value").readline().strip())
	print currentValue
	sys.exit(0)

value = sys.argv [1]
vol = 1

if value == "+":
	currentValue = int (open ("/home/lg/.bin/volume/vol.value").readline().strip())
	if currentValue < MAX:
		vol = currentValue + INCREMENT
elif value == "-":
	currentValue = int (open ("/home/lg/.bin/volume/vol.value").readline().strip())
	if currentValue > 0:
		vol = currentValue - INCREMENT
else:
	vol = int (value)

pcm  = int (100*float (vol)/MAX)

open ("/home/lg/.bin/volume/vol.value", "w").write (str(vol))

cmm = "amixer -D pulse sset Master " + str(pcm)+"%"
print vol, pcm, cmm

os.system (cmm)
