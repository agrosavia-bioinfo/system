if [ "$1" == "+" ]; then
	par="+10%"
fi
if [ "$1" == "-" ]; then
	par="-10%"
fi
if [ "$1" == "0" ]; then
	par="0%"
fi
echo $par

cmm="pactl -- set-sink-volume 0 $par"
echo $cmm
eval $cmm
