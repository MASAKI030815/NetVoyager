import sys
import time
import threading
import config
from myipaddr import myipaddr
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4


def update_cli():
    global response_myipaddr
    global response_ping_gateway_v4

    response_myipaddr = myipaddr()
    response_ping_gateway_v4 = ping_gateway_v4()

    sys.stdout.write("\033[H\033[J")

    ipv4_addr, netmask, gateway, ipv6_addr = myipaddr()

    print("\033[1m\033[93m-------Network Setting-------\033[0m")
    print(f"Interface: {config.interface}")
    if ipv4_addr and netmask:
        print(f"IPv4 Address: {ipv4_addr}")
        print(f"Netmask: {netmask}")
    if gateway:
        print(f"Default Gateway: {gateway}")
    if ipv6_addr:
        print(f"IPv6 Address: {ipv6_addr}")

    print("\033[1m\033[93m\n-------Gateway Ping Result-------\033[0m")
    print(response_ping_gateway_v4)

    print("\033[1m\033[93m\n-------IPv4 Ping Results-------\033[0m")
    for host, name,pingv4_short_option,pingv4_large_option in config.pingv4_targets():
        print(ping_internet_v4(host, name,pingv4_short_option,pingv4_large_option))

#    print("\033[1m\033[93m\n-------IPv6 Ping Results-------\033[0m")
#    for status in response_ping_internet_v6:
#        print(status)

#    print("\033[1m\033[93m\n-------HTTP IPv4 Results-------\033[0m")
#    for status in response_http_checks:
#        if "IPv4" in status:
#            print(status)

#    print("\033[1m\033[93m\n-------HTTP IPv6 Results-------\033[0m")
#    for status in response_http_checks:
#        if "IPv6" in status:
#            print(status)

#    print("\033[1m\033[93m\n-------Virus Check Results-------\033[0m")
#    for status in response_virus_checks:
#        print(status)

#    print("\033[1m\033[93m\n-------IPv4 MTR Results-------\033[0m")
#    for result in response_mtr_checks:
#        if 'IPv4' in result:
#            print(result)

#    print("\033[1m\033[93m\n-------IPv6 MTR Results-------\033[0m")
#    for result in response_mtr_checks:
#        if 'IPv6' in result:
#            print(result)
    
if __name__ == '__main__':       
    while True:
        update_cli()
        time.sleep(1) 
