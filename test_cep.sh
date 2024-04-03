#!/bin/bash
sudo rm -r NetVoyager
git clone https://github.com/Ginjo0815/NetVoyager.git
sudo nmcli c down eth0
sudo nmcli c up eth0
chmod +x ./NetVoyager/main.py
python3 ./NetVoyager/main.py
