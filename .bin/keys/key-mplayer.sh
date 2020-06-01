WID=`xdotool search  --name "mplayer"`
xdotool windowactivate $WID;sleep 0.2;xdotool key space;sleep 0.1;xdotool windowminimize $WID
