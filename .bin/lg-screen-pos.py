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

screenWidth = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f1', shell=True, stdout=sp.PIPE).communicate()[0])
screenLarge = int (sp.Popen ('lg-screen-res.sh|cut -d" "  -f2', shell=True, stdout=sp.PIPE).communicate()[0])

WIDTH = screenWidth/2
LARGE = screenLarge-30

tmpFile = "/home/lg/tmp/config/pos-win.tmp"
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
	posWin = 100

x = posWin * WIDTH
w = sizeWin * WIDTH
print WIDTH, LARGE, x, w

#cmm = "wmctrl -r :ACTIVE: -e 0,%s,0,683,731" % int(x)
cmm = "wmctrl -r :ACTIVE: -e 25,%s,%s,%s,%s" % (int (x), 25*barOnTop, int(w), LARGE)
os.system (cmm)
print cmm

open (tmpFile,"w").write (str (round (posWin)))


