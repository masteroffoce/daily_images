#!/usr/bin/env bash

WALL=~/backgrounds/$(date +'%Y%m%d')
cat > ~/.config/hypr/hyprpaper.conf <<EOF
preload = $WALL
wallpaper = , $WALL
EOF
