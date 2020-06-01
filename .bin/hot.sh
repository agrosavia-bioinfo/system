
#Scritp to write the current directory to the hotlist of midnight commander"

if [ "$1" == "" ]; then
	DIR=`pwd`
else
	DIR=$1
fi

echo "\"$DIR\" into mc hotlist: "

cat /home/lg/.mc/hotlist > /tmp/a

echo "ENTRY \"$DIR\"" "URL \"$DIR\"" > /home/lg/.mc/hotlist

cat /tmp/a >> /home/lg/.mc/hotlist 
