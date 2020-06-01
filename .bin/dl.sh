
#dillo www.linguee.com &
#sleep 1
#xdotool search --name "Dillo: Lingue | Dictionary for German, French, Spanish, and more" windowactivate key Tab+Tab

SITE=$1
echo ">>>" "$SITE" > /tmp/a
dillo -g 800x1600 $SITE &

sleep 1
#wmctrl -r :ACTIVE: -e 25,0,0,840,1000
if [ "$SITE" = "www.linguee.com" ]; then
	#( speaker-test -t sine -f 1000 )& pid=$! ; sleep 1s ; kill -9 $pid
	xdotool key --window "$(xdotool search --class dillo | head -n 1)" Tab + Tab
else
	#( speaker-test -t sine -f 3000 )& pid=$! ; sleep 1s ; kill -9 $pid
	xdotool key --window "$(xdotool search --class dillo | head -n 1)" Tab 
fi
