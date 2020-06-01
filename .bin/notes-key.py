#!/usr/bin/python

import os, sys

lsnotes = sys.argv[1:];
#lsnotes = args.split ()  

for i in lsnotes:
    cmm1 = "xdotool type %s" % i.strip()
    os.system (cmm1)
    cmm2 = "xdotool key Tab"
    os.system (cmm2)


