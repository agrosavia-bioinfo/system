FILE=$1
NAME=`echo "$FILE" | cut -d'.' -f1`
EXTENSION=`echo "$FILE" | cut -d'.' -f2`

mplayer -dumpaudio $NAME.avi -dumpfile $NAME.mp3
