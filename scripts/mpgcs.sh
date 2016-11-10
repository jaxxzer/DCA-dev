#!/bin/bash
cd ~
echo launching qgc...
~/Downloads/QGroundControl.AppImage &
echo launching mavproxy in new window...
gnome-terminal -e "python ~/git/MAVProxy/MAVProxy/mavproxy.py --target-system=1 --target-component=1 --master=0.0.0.0:14551 --out=udp:0.0.0.0:14550 --load-module=DGPS --aircraft=ROV_LOGS"
sleep 2
echo starting netcat...
echo 'netcat -u 127.0.0.1 13320 < /dev/ttyUSB0'
netcat -u 127.0.0.1 13320 < /dev/ttyUSB0 && echo netcat running..
echo
echo netcat stopped
