#!/usr/bin/python

import sys, os

filename = sys.argv [1]
stem = "http://www.colmundo.com/"

lines = open (filename).readlines()

lstMp3s = []
for ln in lines:
	if not "href" in ln: continue
	if not ".mp3" in ln: continue 
	#if not "../../" in ln: continue

	s1 = ln.split ('href="')[1]
	s2 = s1.split (">")[0]
	#s3 = s2.split ("../../")[1]
	s3 = s2[:-1]


	s4=""
	if "../../" in s3:
		s4 = s3.replace ("../../", stem)
	else:
		s4 = s3


	if not s4 in lstMp3s:
		lstMp3s.append (s4)

for mp3 in lstMp3s:
	cmm = "xdown " + mp3 + " &"
	print (cmm)
	#os.system (cmm)

