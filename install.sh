#!/bin/sh

#Install dependencies

sudo apt install python3 git-core
git clone https://github.com/Red-Hide/ZeroP_Software.git
cd ZeroP_Software-main
pip3 install -r requirements.txt


