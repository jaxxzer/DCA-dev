#!/bin/bash

# flash firmware to pixhawk connected to remote host
# Jacob Walser September 2016

DATE=$(date +%y-%m-%d.%H:%M:%S)
BRANCH=$(git rev-parse --abbrev-ref HEAD)
COMMIT=$(git rev-parse --short HEAD)

# Name the firmware with descriptive information
FILENAME=$DATE.$BRANCH.$COMMIT.px4
echo $FILENAME

# copy the firmware to remote host
scp ~/git/ArduSub/ArduSub/ArduSub-v2.px4 pi@20.0.0.20:~/$FILENAME
ssh pi@20.0.0.20 \

# quit mavproxy on remote host
# move old firmware
# move new firmware
# flash new firmware
# wait 5 seconds for pixhawk to reboot
# restart mavproxy
"sudo screen -X -s mavproxy quit; \
mv ~/Pixhawk_FW/current/*.px4 ~/Pixhawk_FW/previous/; \
mv $FILENAME ~/Pixhawk_FW/current/;
python px_uploader.py --port /dev/ttyACM0 ~/Pixhawk_FW/current/$FILENAME; \
sleep 5; \
sudo screen -dm -S mavproxy /home/pi/git/DCA-dev/companion/RPI2/Raspbian/start_mavproxy.sh; \
echo Done."
