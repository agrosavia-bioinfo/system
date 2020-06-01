unix=$1
name=`echo $1|cut -d'.' -f 1`
ext=`echo $1|cut -d'.' -f 2`
win=$name-win.$ext
awk 'sub("$", "\r")' $unix > $win
