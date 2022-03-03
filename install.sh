#!/bin/sh

#Install dependencies

sudo apt update && sudo apt upgrade
sudo apt install python3 git-core
git clone https://github.com/Red-Hide/ZeroP_Software.git
cd ZeroP_Software
pip3 install -r requirements.txt


