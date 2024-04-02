import time
import sys
from win_myipaddr import myipaddr

def update_cli():

    ipv4_addr, subnet_mask, gateway, ipv6_addr = myipaddr()
    if ipv4_addr and subnet_mask:
        print(f"IPv4 Address: {ipv4_addr}")
        print(f"Netmask: {subnet_mask}")
    if gateway:
        print(f"Default Gateway: {gateway}")
    if ipv6_addr:
        print(f"IPv6 Address: {ipv6_addr}")
    
if __name__ == '__main__':       
    while True:
        update_cli()
        time.sleep(10) 
