#!/usr/bin/python

import os, sys

file = sys.argv [1]
lines = open (file).readlines ()

for passwd in lines:
    path = passwd.split (":")[5]
    user = path.split("/")[3]

    #cmm = "sudo mkdir /home/ed1/%s\n" % user
    cmm = "\necho %s\n" % user
    cmm += "useradd -d /home/ed/%s -s /bin/bash -m %s -p %s" % (user, user, user)
    cmm += "\npasswd %s" % user
    print cmm

