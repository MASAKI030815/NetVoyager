import time
import sys
from myipaddr import myipaddr

def update_cli():
    global response_myipaddr

#    response_myipaddr = ""
#    ipv4_addr = ""
#   netmask = ""
#   gateway = ""
#    ipv6_addr = ""

    ipv4_addr, netmask, gateway, ipv6_addr = myipaddr()
    if ipv4_addr and netmask:
        print(f"IPv4 Address: {ipv4_addr}")
        print(f"Netmask: {netmask}")
    if gateway:
        print(f"Default Gateway: {gateway}")
    if ipv6_addr:
        print(f"IPv6 Address: {ipv6_addr}")
    
if __name__ == '__main__':       
    while True:
        update_cli()
        time.sleep(10) 
