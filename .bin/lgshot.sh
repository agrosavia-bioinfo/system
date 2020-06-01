#!/bin/bash
sleep 0.3
/usr/bin/scrot -s /tmp/a.png 
xclip -selection clipboard -t image/png <"/tmp/a.png"
img /tmp/a.png
