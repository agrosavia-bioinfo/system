#!/usr/bin/python

"""
  Activates / Desactivates xmc window with only alt+c key
"""

import os
VISIBLE = open ("/home/lg/tmp/config/mc-visible.cfg").read()
cmdEnable  ='wmctrl -a mc'
cmdDisable = 'xdotool windowminimize $(xdotool search -name mc)'

if VISIBLE == 'actived':
	os.system (cmdDisable)
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("minimized")
else:
	os.system (cmdEnable)
	open ("/home/lg/tmp/config/mc-visible.cfg", "w").write ("actived")
#x mc
