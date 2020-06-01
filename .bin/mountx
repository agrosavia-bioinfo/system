#!/bin/bash
# Show connected devices, read one of them, and mount it
if [ "$1" == "" ]; then
	sudo fdisk -l
	read DEV
else
	DEV=$1
fi

sudo mkdir $DEV
sudo chmod a+w $DEV
sudo mount /dev/$DEV $DEV




