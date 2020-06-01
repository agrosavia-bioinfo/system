
sudo notify-send -u critical "$1" "$2"; 
sleep 2; 
killall /usr/lib/x86_64-linux-gnu/notify-osd
