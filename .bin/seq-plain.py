#!/usr/bin/python
import os, sys
from Bio.Blast.Applications import NcbiblastnCommandline
from Bio import SeqIO

args          = sys.argv
filename      = args [1]

seqRecords    = SeqIO.parse (filename, "fasta")
seqRecordsLst = list (seqRecords)
nSeqs         = len (seqRecordsLst)

newFilename   = filename.split (".")[0] + "-plain.fna"

##SeqIO.write (seqRecordsLst, newFilename, "fasta")

from Bio.SeqIO import FastaIO
with open (newFilename, "w") as target:
	fasta_out = FastaIO.FastaWriter(target, wrap=None)
	fasta_out.write_file(seqRecordsLst)
