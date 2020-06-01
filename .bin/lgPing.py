#!/usr/bin/python
import os, sys

start = int (sys.argv [1])
end   = int (sys.argv [2])

ip = "172.16.70"

for i in range (start, end):
	cmm = "ping -c 5 %s.%s &" % (ip, i)

	print ">>>>>>>>>>>>>>>> %s.%s <<<<<<<<<<<<<<<<" % (ip, i)

	os.system (cmm)



	

