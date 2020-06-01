TIME=1

for i in `seq 1 5`; do
	sleep $TIME
	xdotool key ctrl+p
	sleep $TIME
	xdotool key Down
	xdotool mousemove_relative 0 30
	sleep $TIME
	xdotool key Alt+Tab
done

xdotool key Alt+Tab
xdotool key Ctrl+f
