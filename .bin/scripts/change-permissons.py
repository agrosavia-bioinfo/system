
import os, sys

def changePermissions (parentDir):
	print parentDir
	dirs = os.listdir(parentDir)
	for dir in dirs:
		dir = parentDir + "/" + dir
		print dir, os.path.isdir (dir)
		if os.path.isdir (dir):
			os.chmod (dir, 448)
			changePermissions (dir)


parentDir = sys.argv [1]
changePermissions (parentDir)




