#!/usr/bin/python

import os, sys

appName = sys.argv [0]
USAGE  = "Splites a MP3 file in subfiles of specific duration \n"
USAGE += appName + "  <input file> <output file stem> <Total duration> <split time>"

if len (sys.argv) != 5:
	print USAGE
	sys.exit (0)

inMp3File = sys.argv [1]
outMp3File = sys.argv [2]
endtime = int (sys.argv [3])
minutes = int (sys.argv [4])

endtimeInSeconds = 60*endtime
minutesInSeconds = 60*minutes

time, nextHours, nextMinutes, nextSeconds, sequence = 0,0,0,0,0
while (time <= endtimeInSeconds):
	startTime = "%.2d:%.2d:%.2d" % (nextHours, nextMinutes, nextSeconds)

	time += minutesInSeconds
	sequence += 1

	seconds = time % 60
	allMinutes = time / 60
	nextMinutes = allMinutes % 60
	nextHours   = allMinutes / 60

	endTime = "%.2d:%.2d:%.2d" % (0, minutes, 0)

	command = "ffmpeg -i %s -ss %s -t %s %s%.2d.mp3 &" % (inMp3File, startTime, endTime, outMp3File, sequence)
	print command
  
