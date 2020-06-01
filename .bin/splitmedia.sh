INFILE=$1
START=$2
END=$3
OUTFILE=$4

command="ffmpeg -i $INFILE -ss 00:$START:00 -t 00:$END:00 $OUTFILE"
echo $command
eval $command
