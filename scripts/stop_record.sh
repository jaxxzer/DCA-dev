#!/bin/bash

screen -XS video_rec stuff $'\003'
ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream.sh;"
