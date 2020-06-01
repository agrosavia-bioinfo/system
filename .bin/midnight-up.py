#!/usr/bin/python

"""
  Activates / Desactivates xmc window with only alt+c key
"""

import os
VISIBLE = open ("/home/lg/tmp/config/mc-visible.cfg").read()
cmdMin ='WID=`xdotool search --desktop 0  --name "xterm-S"`;\
	           `xdotool windowminimize $WID &`'
cmdAct = 'WID=`xdotool search --desktop 0 --name "xterm-S"`;\
	     xdotool windowactivate $WID &'
if VISIBLE == 'actived':
	os.system (cmdAct)
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("minimized")
else:
	os.system (cmdAct)
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("actived")
#x mc
