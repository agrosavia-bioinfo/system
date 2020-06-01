#!/usr/bin/python
import os, sys

args = sys.argv

if len (args)<2:
    cmm="readlink -f /home/lg/.bin/txt"
else:
    option = args [1]
    cmm = ""
    if 'x' in option:
            cmm = 'ln -sf /home/lg/.bin/xed /home/lg/.bin/txt'
    elif 'v' in option:
            cmm = 'ln -sf /usr/bin/vim /home/lg/.bin/txt'
    elif 's' in option:
            cmm = 'ln -sf /opt/bin/subl /home/lg/.bin/txt'
    elif "c" in option:
            cmm = 'ln -sf /usr/bin/codeblocks /home/lg/.bin/txt'
    elif "g" in option:
            cmm = 'ln -sf /usr/bin/gedit /home/lg/.bin/txt'
print  cmm
os.system (cmm)
