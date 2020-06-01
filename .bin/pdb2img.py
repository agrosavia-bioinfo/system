#!/usr/bin/python

# Get the image from PDBs in a compressed file (tgz) 
USAGE="prog <PDB filename>"

import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI

import sys, time, os
import pymol

#----------------------------------------------------------------------
def createImage (pdb):
	spath = pdb
	sname = pdb.split (".")[0] 

	print ">>>", spath, sname

	pymol.finish_launching()
	pymol.cmd.reinitialize()

	pymol.cmd.load (spath, sname)
	pymol.cmd.hide ("all")
	pymol.cmd.bg_color ("white")
	pymol.cmd.color ("red", "ss h")
	pymol.cmd.color ("yellow", "ss s")
	pymol.cmd.color ("green", "ss l+''")
	pymol.cmd.show ("cartoon","all")
	pymol.cmd.ray (0, 0)
	pymol.cmd.png (sname)
#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------
import tarfile

args = sys.argv
pdbFilename = args [1]
#pngFilename = pdbFilename.split (".")[0] + ".png"

createImage (pdbFilename)
