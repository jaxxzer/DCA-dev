#!/bin/bash
ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream.sh;"
ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream_rec.sh;"

VIDSPATH=/home/jack/ROVVIDEOS
NAME=/video$(ls $VIDSPATH | wc -l)

mkdir $VIDSPATH

ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream_5000.sh;"

screen -dm -S video_rec gst-launch-1.0 -e -v udpsrc port=5000 ! tee name=t ! queue ! application/x-rtp, encoding-name=H264, payload=96 ! rtpjitterbuffer ! rtph264depay ! filesink location=$VIDSPATH$NAME t. ! queue ! udpsink port=5600




screen -XS video_rec quit
ssh pi@20.0.0.20 "sudo screen -XS video quit; sudo screen -dm -S video /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_videostream.sh;"
