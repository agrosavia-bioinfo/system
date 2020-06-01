\documentclass[11pt]{article}
\usepackage{adds/lgstyle}
\begin{document}
#!/usr/bin/python


# Change the x position of the currente window to the rigth or the left
# It uses the wmctrl command

import os, sys

posWin = 0.0
sizeWin = 0.0
WIDTH = 1366/2

tmpFile = "/tmp/pos-win.tmp"
args = sys.argv
if (len (args) >1):
	posWin = 0.35
else:
		try:
				posWin = float (open (tmpFile).read())
				if posWin == 0:	
						posWin = 0.8
						sizeWin = 1.2
				else:
						posWin = 0
						sizeWin = 0.8
		except IOError:
				posWin = 0

x = posWin * 683
w = sizeWin * 683

#cmm = "wmctrl -r :ACTIVE: -e 0,%s,0,683,731" % int(x)
cmm = "wmctrl -r :ACTIVE: -e 0,%s,0,%s,731" % (int (x), int(w))
os.system (cmm)
print cmm

open (tmpFile,"w").write (str (posWin))


\end{document}
