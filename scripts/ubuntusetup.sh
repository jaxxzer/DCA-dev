#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y git
sudo apt-get install -y openjdk-7-jdk
sudo apt-get install -y gawk
sudo apt-get install -y python-empy
sudo apt-get install -y python-pip
sudo pip install catkin_pkg

sudo apt-get install -y lib32gcc1
sudo apt-get install -y genromfs
sudo apt-get remove modemmanager
sudo usermod -a -G dialout $USER
#^^^needs reboot

sudo apt-get install -y screen
sudo apt-get install -y python-dev


#gcc-arm-none-eabi-4_9-2015q3 in /opt
#from: http://firmware.ardupilot.org/Tools/PX4-tools/

#add
#export PATH=$PATH:/opt/gcc-arm-none-eabi-4_9-2015q3/bin
#to end of $HOME/.bashrc

#eclipse mars

#qt 5.5.1
sudo apt-get install -y espeak libespeak-dev libudev-dev libsdl1.2-dev

#For MAVExploerer:
sudo apt-get install -y libfreetype6-dev
sudo pip install matplotlib

#to build execuables for pi, bbb
sudo apt-get install -y g++-arm-linux-gnueabihf

#for mavexplorer:
sudo pip install matplotlib
sudo apt-get install -y python-wxtools

#for mavproxy map module:
sudo apt-get install -y python-opencv

#for hypack-translation script:
sudo pip install pyproj

#for mavgenerate:
sudo apt-get install -y python-tk


sudo apt-get install -y gparted

#for sd-xc memory cards:
sudo apt-get install -y exfat-fuse exfat-utils

sudo apt-get upgrade -y



mkdir ~/git
cd ~/git

# configure git to save password for 2 hours at at a time
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=7200'
git config --global user.name "jaxxzer"
git config --global user.email "jwalser90@gmail.com"

git clone --recursive https://github.com/bluerobotics/qgroundcontrol.git
git clone --recursive https://github.com/bluerobotics/ardusub.git
git clone https://github.com/jaxxzer/MAVProxy.git
git clone https://github.com/jaxxzer/mavlink.git
git clone https://github.com/jaxxzer/companion.git
git clone --recursive https://github.com/jaxxzer/DCA-dev.git

cd ~/Downloads

#Download/extract Arduino
wget https://www.arduino.cc/download.php?f=/arduino-1.6.9-linux64.tar.xz -O ~/Downloads/arduino-1.6.9-linux64.tar.xz
sudo tar -xvJf ~/Downloads/arduino-1.6.9-linux64.tar.xz --directory /opt
/opt/arduino-1.6.9/install.sh

#Download/extract arm compiler for pixhawk
wget http://firmware.us.ardupilot.org/Tools/PX4-tools/gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar.bz2 -O ~/Downloads/gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar.bz2
sudo tar -xvjf ~/Downloads/gcc-arm-none-eabi-4_9-2015q3-20150921-linux.tar.bz2 --directory /opt

sed -i "\$aPATH=\$PATH:/opt/gcc-arm-none-eabi-4_9-2015q3/bin" $HOME/.bashrc


mkdir ~/Arduino
cd ~/Arduino
git clone https://github.com/jaxxzer/Mavlink-monitor.git
git clone https://github.com/jaxxzer/Mavlink-sony.git

mkdir ~/Arduino/hardware
cd ~/Arduino/hardware
git clone https://github.com/rogerclarkmelbourne/Arduino_STM32.git

mkdir ~/Arduino/hardware/esp8266com
cd ~/Arduino/hardware/exp8266com
git clone https://github.com/esp8266/Arduino.git

wget download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run -O ~/Downloads/qt-unified-linux-x64-online.run
chmod +x ~/Downloads/qt-unified-linux-x64-online.run
~/Downloads/qt-unified-linux-x64-online.run



