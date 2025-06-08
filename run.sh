#!/usr/bin/env bash

if [ -f "$HOME/backgrounds/$(date +'%Y%m%d')" ]; then
	echo 'Background for this day already exists.'
else
	echo 'Making background for today.'
	nix-shell --run './dailybg.sh 0'
fi
./paperconfig.sh
hyprctl dispatch exec hyprpaper

if [ -f "$HOME/backgrounds/$(date -d "+1 day" +'%Y%m%d')" ]; then
	echo 'Background for tomorrow already exists.'
else
	echo 'Making background for tomorrow.'
	nix-shell --run './dailybg.sh 1'
fi
