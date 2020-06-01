#!/bin/bash

cd /opt/apps/dics/everest
echo "Everest dictionary < t:Technical | s:Synonims | st:Standard > "
read dic

if [ "$dic" == "t" ]; then
	cp Everest-tech.ini Everest.ini
fi
if [ "$dic" == "s" ]; then
	cp Everest-syn.ini Everest.ini
fi
if [ "$dic" == "st" ]; then
	cp Everest-std.ini Everest.ini
fi

everest
