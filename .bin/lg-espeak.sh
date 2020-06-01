#!/bin/bash
a=`xclip -o`
if [ "$1" == '-gd' ]; then
	/usr/bin/goldendict $a
else
	espeak $a 
	espeak $a
	echo $a|festival --tts
	echo $a|festival --tts
	#say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*"; }
	#say $a 
	#say $a 
fi


