WIN1=20971556
WIN2=31457298
WIN1=`xdotool search --desktop 1 --name mplayer`
xdotool windowfocus --sync $WIN1
xdotool key Left
WIN2=`xdotool search --desktop 1 --name lyx`
xdotool windowactivate --sync $WIN2
