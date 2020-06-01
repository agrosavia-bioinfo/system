#!/bin/bash
# Open a colorful xterm with random background color
# The title can be passed as parameter or if the parameter is "bio"
# then, a "bio" shell is exectuted to connect to the bio server
# Author: Luis Garreta (Sep, 2009)

############## PROMPT COLORING ####################################
#export PS1="$COLOR[\W$COLOR\h$COLOR:\W$COLOR]\$ \e[-1m "
COLOR="\e[\034m\]"
COLOR1="\[\034[1;35m\]"
export PS1="$COLOR<\h><\W>$COLOR1\$ \e[m"
############## PROMPT COLORING ####################################

title=$1
COMMAND=""
FONT="8x16"
FG=cyan
#FONT="7x14"
#FONT="6x13"
TERM="xterm"
if [ "$1" == '' ]; then
	echo 
	dir=`pwd`
	title=`basename $dir`
fi

if [ "$1" == 'TEST' ]; then
	cd /home/lg/labrpi/contactmap/growing-for/test
	xed test.f90
fi

if [ "$1" == 'geofold' ]; then
	cd /home/lg/gfpy/python/new
fi
if [ "$1" == 'victor' ]; then
	COMMAND="victor"
fi
if [ "$1" == 'phd' ]; then
	COMMAND="phd"
fi
if [ "$1" == 'lab' ]; then
	COMMAND="lab"
fi
if [ "$1" == 'bio' ]; then
	COMMAND="bio"
fi
if [ "$1" == 'gebix' ]; then
	COMMAND="gebix"
fi
if [ "$1" == 'manolo' ]; then
	COMMAND="manolo"
fi
if [ "$1" == 'cluster' ]; then
	COMMAND="cluster"
fi
if [ "$1" == 'eisc' ]; then
	COMMAND="eisc"
fi
if [ "$1" == 'gebix' ]; then
	COMMAND="gebix"
fi
if [ "$1" == 'asus' ]; then
	COMMAND="asus"
fi
if [ "$1" == 'xed' ]; then
	title=`basename $2`
	COMMAND="-e vim $2"
fi
if [ "$1" == 'mc' ]; then
	TERM="xterm-xmc"
	COMMAND="-e mc $2"
fi

#ARRCOLOR[0]=rgb:a8/f5/90 	#lightblue
#ARRCOLOR[1]=rgb:ff/e6/cc 	#lightred
#ARRCOLOR[2]=rgb:cc/cc/cc 	#lightgray
#ARRCOLOR[3]=rgb:e6/ff/cc 	#lightgreen
#ARRCOLOR[4]=rgb:fb/c8/f8 	#lightviolet
#ARRCOLOR[5]=rgb:fd/cd/da 	#lightred
#ARRCOLOR[6]=rgb:ff/ff/99 	#lightred
ARRCOLOR[0]=rgb:ff/ff/ff 	#lightred

let NUMBER=$RANDOM%${#ARRCOLOR[@]}

BG=${ARRCOLOR[$NUMBER]}
export BG

FNT='UbuntuMono'
#BG=lightblue
FG=black
#command="$TERM -geometry 84x50 -fn $FONT -bg $BG -fg cyan -name $title -title $title $COMMAND" 
command="$TERM -fa $FNT -fs 18 -geometry 84x24 -fn $FONT -bg $BG -fg $FG -name $title -title $title $COMMAND" 
#echo $command
$command &
#wmctrl-set.py

#xterm -fn 8x16 -bu{g rgb:00/02/17 -fg cyan -n $title -ls &
