#!/bin/bash

python more_video_control.py &
sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -vo sdl -framedrop -input file=/home/pi/Documents/lab2/videoplayer ../video.mp4
