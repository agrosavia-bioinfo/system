#!/usr/bin/python

"""
  Activates / Desactivates xmc window with only alt+c key
"""

import os

VISIBLE = open ("/home/lg/tmp/config/mc-visible.cfg").read()
if VISIBLE == 'actived':
	os.system ('WID=`xdotool search --desktop 0  --name "xterm-S"`;\
	           `xdotool windowminimize $WID`')
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("minimized")
else:
	cmd='WID=`xdotool search --desktop 0 --name "xterm-S"`;\
	     xdotool windowactivate $WID'
	os.system (cmd)
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("actived")
#x mc
