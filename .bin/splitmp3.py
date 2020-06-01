#!/usr/bin/python

import os, sys
import subprocess

appName = sys.argv [0]
USAGE  = "Get a slice from a MP3 file given initial seconds and end seconds  \n"
USAGE += appName + "  <input file> <output file stem> <Total duration> <split time>"

inMp3File = sys.argv [1]
outMp3File = sys.argv [2]

cmm = 'mp3info -p "%S" englishpronunciationpod_76.mp3'
out = os.popen(cmm)
totalTime = int (out.next())



iniTime = 11* (totalTime/100)
endTime = 95 * (totalTime/100)


print (iniTime, endTime, totalTime)

command = "ffmpeg -i %s -ss %s -t %s %s%.2d.mp3 &" % (inMp3File, startTime, endTime, outMp3File)

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
  
