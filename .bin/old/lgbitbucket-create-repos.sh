#!/usr/bin/python2
# Create repositories in bitbucket using cli commands

import os

REPONAME=lgdocs

cmm = "bb create -u lgdocs -p chevive2001 --private --protocol ssh --scm git %s"
repos = open ("repos.txt").readlines()
repos = [x.strip() for x in repos]

print "\nCREATE...\n"
for i in repos:
	cmm2 = cmm % i
	print cmm2
	os.system(cmm2)

input()

print "\nCLONE...\n"
cmm = 'git clone https://lgdocs:chevive2001@bitbucket.org/lgdocs/%s'
for i in repos:
	cmm2 = cmm % i
	print cmm2
	os.system(cmm2)

input()

print "\nREADME\n"
for i in repos:
	campos  = i.split("-")
	fecha  = campos [0]
	nombre = "-".join (campos [1:])
	fullFecha = fecha[3:7] + "-" + fecha[7:]
	cmm2 = 'cd %s;echo "# Repositorio %s %s">README.md;cd ..' % (i, nombre,fullFecha) 
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
