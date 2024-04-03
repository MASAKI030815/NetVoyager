#!/bin/bash
sudo rm -r NetVoyager
git clone https://github.com/Ginjo0815/NetVoyager.git
chmod +x ./NetVoyager/script.py
sudo nmcli c down eth0
sudo nmcli c up eth0
python3 ./NetVoyager/script.py
