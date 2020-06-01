#!/usr/bin/python

## Reduce the video size using ffmpeg

import os, sys

inputFile = sys.argv [1]
name = inputFile.split (".")[0]
ext = inputFile.split (".")[1]

outputFile = name + "-low." + ext


cmm = "ffmpeg -i %s -ab 56k -ar 22050 -b 300k -r 15 -s 480x360 %s" % (inputFile, outputFile)
#cmm = "ffmpeg -i %s %s" % (inputFile, outputFile)
#cmm = "avconv -i %s -b:a 192k %s" % (inputFile, outputFile)
#cmm = "avconv -i %s %s" % (inputFile, outputFile)

print cmm
os.system (cmm)


