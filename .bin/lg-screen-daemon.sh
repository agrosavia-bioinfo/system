# Restarting gnome-settings-daemon fixed it for me:
gnome-settings-daemon --replace > /dev/null 2>&1 &
