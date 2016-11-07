#!/bin/bash
VIDSPATH=/home/jack/ROVVIDEOS
NAME=/video$(ls $VIDSPATH | wc -l).mp4

mkdir $VIDSPATH

#stop, if already recording
screen -XS video_rec stuff $'\003'

#switch pi to stream on port 5000
ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream_5000.sh;" &&

screen -dm -S video_rec gst-launch-1.0 -e -v udpsrc port=5000 ! tee name=t ! queue ! application/x-rtp, encoding-name=H264, payload=96 ! rtph264depay ! h264parse ! mp4mux ! filesink location=$VIDSPATH$NAME t. ! queue ! udpsink port=5600
