#!/bin/bash
cd $TEX_PATH
pdflatex $TEX_DOC

read x 
if [ $x == 1 ]; then
	sleep 10
fi
if [ $x == q ]; then
	exit
fi

sleep 3
