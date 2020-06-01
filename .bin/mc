#'Open the MC filemanage according to line arguments (a directory) or
#'taking the last directory from a saved file.
#'At final, the current directory is saved to remember the last directory

FILE=$HOME/tmp/mc.pwd
OLDFILE=$FILE".old"

SHELL=/bin/bash

if [ -f ~/tmp/mc.pwd ]; then
	:
else
	cp $OLDFILE $FILE
fi

LWD=`sed 's/[^(]*(//;s/).*//' $FILE`

rm $FILE

if [ $1 ]; then
	/usr/bin/mc --printwd="$FILE" $1
else
	/usr/bin/mc --printwd="$FILE" $LWD
fi

cp $FILE $OLDFILE
