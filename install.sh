#!/bin/sh

#Install dependencies

sudo apt update && sudo apt upgrade -y
sudo apt install python3 git-core python3-pyqt5 pigpio -y
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
git clone https://github.com/Red-Hide/ZeroP_Software.git
cd ZeroP_Software
pip3 install -r requirements.txt


