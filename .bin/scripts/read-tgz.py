#!/usr/bin/python

import tarfile, os

tar = tarfile.open("path.tar.gz", "r|gz")

tar.extractall (path="pdbs")

listOfFiles = os.listdir ("pdbs")
listOfPdbs = filter (lambda x: ".pdb" in x, listOfFiles)

os.chdir ("pdbs")
for pdb in listOfPdbs:
	name = pdb.split (".")[0].split ("-")[0]
	number = pdb.split (".")[0].split ("-")[1]

	newName = name + "-" + number.zfill (3) + ".pdb"

	print pdb, newName  
	os.rename (pdb, newName)
