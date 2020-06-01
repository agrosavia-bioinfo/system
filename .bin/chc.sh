#!/bin/bash
# Open a colorful xterm with random background color
ARRCOLOR[0]=rgb:00/02/17 	#darkblue
ARRCOLOR[1]=rgb:0A/14/14	#darkgreen 
ARRCOLOR[2]=rgb:39/04/0c	#darkred
ARRCOLOR[3]=rgb:248/107/109	#darkred2
ARRCOLOR[4]=rgb:17/17/00		#darkyellow
ARRCOLOR[5]=rgb:13/03/2a		#darkpurple
ARRCOLOR[6]=rgb:19/0e/00		#darkbrown
ARRCOLOR[7]=rgb:08/28/02		#darkgreen
ARRCOLOR[8]=rgb:2c/05/35		#darkgreen
ARRCOLOR[9]=rgb:2d/1e/10		#darkbrown
ARRCOLOR[10]=rgb:00/00/00		#black
ARRCOLOR[12]=rgb:00/00/00		#black
ARRCOLOR[13]=rgb:12/11/21 		#black purple
ARRCOLOR[14]=rgb:07/1B/06 		#black green
ARRCOLOR[15]=rgb:11/13/05 		#black yellow
ARRCOLOR[16]=rgb:24/10/14
ARRCOLOR[17]=rgb:00/28/00 		#black steel
## Change foreground
ARRCOLOR[18]=rgb:13/13/13 		#black steel
ARRCOLOR[19]=rgb:07/08/13 		#black steel
ARRCOLOR[20]=rgb:00/00/00 		#black steel
ARRCOLOR[21]=rgb:00/00/00 		#black steel
ARRCOLOR[22]=rgb:00/00/00 		#black steel
ARRCOLOR[23]=rgb:00/00/00 		#black steel
## Dark
ARRCOLOR[24]=rgb:10/10/10 		#black steel
ARRCOLOR[25]=rgb:1e/00/00 		#black steel
ARRCOLOR[26]=rgb:00/0d/1a 		#black steel
ARRCOLOR[27]=rgb:00/00/18		#black steel
ARRCOLOR[28]=rgb:17/0d/04 		#black steel

let NUMBER=$RANDOM%${#ARRCOLOR[@]}
FG=white
if [ $NUMBER -gt 17 ]; then
	FG=rgb:88/99/B9    # LightSlateBlue
fi

BG=${ARRCOLOR[$NUMBER]}
str='\e]11;'$BG'\a'
#echo $str
echo -e $str

