#!/bin/bash
git clone https://github.com/Ginjo0815/NetVoyager.git
chmod +x ./NetVoyager/script.py
nmcli c down eth0
nmcli c up eth0
./NetVoyager/script.py
