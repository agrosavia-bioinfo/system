# Execute a key action on an inactive window and return to the main window
WIN1=20971556
WIN2=31457298
WIN1=`xdotool search --desktop 1 --name mplayer`
xdotool windowactivate --sync $WIN1
xdotool key space
WIN2=`xdotool search --desktop 1 --name lyx`
xdotool windowactivate --sync $WIN2
