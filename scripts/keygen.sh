#!/bin/bash
# generate rsa key and move add to RPi
ssh-keygen
ssh-copy-id -i ~/.ssh/id_rsa.pub pi@20.0.0.20

