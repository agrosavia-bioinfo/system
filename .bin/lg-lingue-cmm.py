#!/usr/bin/python

import os, sys

args = sys.argv

query=""
for i in args[1:]:
	query += i + "+"
query = query [:-1]


url="http://www.linguee.com/english-spanish/search?source=auto&query="
url2="http://www.linguee.com/english-spanish/search?source=auto&query=hola+como+estas"
#cmm = url.join (query) 

cmm = "google-chrome --disable-extensions --incognito " + '"' + url + "".join(query) + '"' 
#cmm = "midori " + '"' + url + "".join(query) + '"' 
#cmm = "dillo " + '"' + url + "".join(query) + '"' 
cmm = "qupzilla " + '"' + url + "".join(query) + '"' 
print ">>>>", cmm
os.system (cmm) 
