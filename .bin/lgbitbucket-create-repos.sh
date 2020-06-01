#!/usr/bin/python2
# Create repositories in bitbucket using cli commands

import os, sys

REPNAME=sys.argv[1]

cmm = "bb create -u lgdocs -p chevive2001 --private --protocol ssh --scm git %s"

print "\nCREATE...\n"
cmm2 = cmm % REPNAME
print cmm2
os.system(cmm2)


print "\nCLONE...\n"
cmm = 'git clone https://lgdocs:chevive2001@bitbucket.org/lgdocs/%s'
cmm2 = cmm % REPNAME
print cmm2
os.system(cmm2)

print "\nREADME...\n"
cmm2 = 'cd %s;echo "# Repositorio %s">README.md;cd ..' % (REPNAME, REPNAME) 
print cmm2
os.system(cmm2)

"""
print "\nMOVE...\n"
cmm = "mv ../%s/* %s"
for i in repos:
	cmm2 = cmm % (i,i)
	print cmm2
	os.system(cmm2)

input()

print "\nGITT...\n"
cmm = 'cd %s;pwd;echo chevive2001|gitt "Firt backup %s";cd ..'
for i in repos:
	cmm2 = cmm % (i,i)
	print cmm2
	os.system(cmm2)
"""
