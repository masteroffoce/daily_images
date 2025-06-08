#!/usr/bin/env bash

if [ -f "$HOME/backgrounds/$(date +'%Y%m%d')" ]; then
	echo 'Background for this day already exists.'
else
	./dailybg.sh
fi
./paperconfig.sh
hyprctl dispatch exec hyprpaper
