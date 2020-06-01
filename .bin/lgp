#!/usr/bin/python

# Get the image from PDBs in a compressed file (tgz) 
USAGE="prog <PDB filename>"

import __main__
__main__.pymol_argv = [ 'pymol', '-q'] # Quiet and no GUI

import sys, time, os
import pymol


args = sys.argv
pdb = args [1]
#----------------------------------------------------------------------

pymol.finish_launching()
#pymol.cmd.reinitialize()

spath = pdb
sname = pdb.split (".")[0] 

pymol.cmd.load (spath, sname)
pymol.cmd.hide ("all")
#pymol.cmd.bg_color ("white")
pymol.cmd.color ("red", "ss h")
pymol.cmd.color ("yellow", "ss s")
pymol.cmd.color ("green", "ss l+''")
pymol.cmd.show ("cartoon","all")
#pymol.cmd.ray (800, 600)
#pymol.cmd.png (sname)
