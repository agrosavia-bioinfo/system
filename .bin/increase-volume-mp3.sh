infile=$1
name=`echo $1|cut -d'.' -f 1`
outfile=$name-3l.mp3
lame --scale 3 $infile $outfile &> /dev/null &
