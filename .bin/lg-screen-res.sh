xdpyinfo | grep dimensions | awk '{print $2}' | awk -Fx '{print $1, $2}'
