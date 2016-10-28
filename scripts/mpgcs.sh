#!/bin/bash
echo launching qgc...
/home/jack/Downloads/QGroundControl.AppImage &
echo launching mavproxy in new window...
gnome-terminal -e "python /home/jack/git/MAVProxy/MAVProxy/mavproxy.py --master=udp:0.0.0.0:14551 --out=udp:0.0.0.0:14550 --load-module='DGPS'"
sleep 2
echo starting netcat...
echo 'netcat -u 127.0.0.1 13320 < /dev/ttyUSB0'
netcat -u 127.0.0.1 13320 < /dev/ttyUSB0 && echo netcat running..
echo
echo netcat stopped
