#!/usr/bin/python

import sys

filename = sys.argv[1]

packageNames = open (filename)
listSizes = []
for package in packageNames:
	size = package.split()[0]

	if 'K' in size:
		val = float (size[:-1])*1000
	elif 'M' in size:
		val = float (size[:-1])*1000000
	else:
		val = float (size[:-1])

	listSizes.append ((val, package))


listSizes.sort (None, None, True)

for package in listSizes:
	print package[1].strip()
