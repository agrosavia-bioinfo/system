#!/usr/bin/python
# Change the x position of the currente window to the rigth or the left
# It uses the wmctrl command

#LOG:
#    Feb/2015: Modified for the ASUS screen

import os, sys, socket

barOnTop = 0  # 0/1 ToolBar on Top (0) / on bottom (1)
posWin = 0.0
sizeWin = 0.0
hostname = socket.gethostname ()
import subprocess as sp

WIDTH = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f1', shell=True, stdout=sp.PIPE).communicate()[0])
LARGE = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f2', shell=True, stdout=sp.PIPE).communicate()[0])
"""
if hostname == "LG":
	WIDTH = 1680 /2
	LARGE = 1050 - 50
elif hostname == "kamilo":
	WIDTH = 1024/2
	LARGE = 600 - 35
else:
	WIDTH = 1366/2
	LARGE = 768 - 35
"""

#WIDTH = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f1', shell=True, stdout=sp.PIPE).communicate()[0])
#LARGE = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f2', shell=True, stdout=sp.PIPE).communicate()[0])

tmpFile = "/tmp/pos-win.tmp"
args = sys.argv
try:
	posWin = float (open (tmpFile).read())
	if (len (args) >1):
		posWin  = 0.5 #0.40 #0.45 #0.60
		sizeWin = 1.0  # 1.0 # 0.8 #1.2
	else:
		if posWin == 0:	
			posWin = 1#0.8
			sizeWin = 1#1.2
		else:
			posWin = 0
			sizeWin = 1#0.8
except IOError:
	posWin = 0

x = posWin * WIDTH
w = sizeWin * WIDTH
print WIDTH, LARGE, x, w

#cmm = "wmctrl -r :ACTIVE: -e 0,%s,0,683,731" % int(x)
cmm = "wmctrl -r :ACTIVE: -e 25,%s,%s,%s,%s" % (int (x), 25*barOnTop, int(w), LARGE)
os.system (cmm)
print cmm

open (tmpFile,"w").write (str (round (posWin)))


