
FNT='UbuntuMono'

DARKMAGENTA=rgb:26/00/26
echo "Running xroot..."
xterm-root -fa $FNT -fs 13 -bg $DARKMAGENTA -fg yellow -e sudo -i &

sleep 1.5
WIN2=`xdotool search --desktop 1 --name sudo`
xdotool key l + g + e
xdotool key Return
