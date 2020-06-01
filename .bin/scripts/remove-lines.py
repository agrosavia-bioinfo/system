#!/usr/bin/python

"Remove lines matching the PATTERN in a file"

import sys
PATTERN="ANISOU"
filename = sys.argv[1]


import sys
for i in open (sys.argv[1]):
	if "ANISOU" in i:
		continue
	else:
		print i.strip()


