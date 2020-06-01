#!/bin/bash

#*******************************
# Multiple dropbox instances
#*******************************

dropboxes=".dropbox-uv .dropbox-gnz .dropbox-phd"

for dropbox in $dropboxes
do
    HOME=/home/$USER
    if ! [ -d $HOME/$dropbox ];then
       mkdir $HOME/$dropbox 2> /dev/null
       ln -s $HOME/.Xauthority $HOME/$dropbox/ 2> /dev/null
    fi

    HOME=$HOME/$dropbox /usr/bin/dropbox start -i 2> /dev/null &
	
done
