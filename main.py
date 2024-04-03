import sys
import time
import threading
import config
from myipaddr import myipaddr
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4

response_myipaddr = ""
response_ping_gateway_v4 = ""
response_ping_internet_v4 = []
response_ping_internet_v4_lock = threading.Lock()
response_ping_internet_v6 = []
response_ping_internet_v6_lock = threading.Lock()
response_http_checks = []
response_http_checks_lock = threading.Lock()
response_virus_checks = []
response_virus_checks_lock = threading.Lock()
response_mtr_checks = []
response_mtr_checks_lock = threading.Lock()

def update_cli():
    global response_myipaddr
    global response_ping_gateway_v4
    global response_ping_internet_v4
    global response_ping_internet_v6
    global response_mtr_checks

    response_myipaddr = myipaddr()
    response_ping_gateway_v4 = ping_gateway_v4()
    response_ping_internet_v4.clear()
    response_ping_internet_v6.clear()
    response_http_checks.clear()
    response_virus_checks.clear()
    response_mtr_checks.clear()

    v4_thread = threading_ping_v4()
    v6_thread = threading_ping_v6()
    threading_http_checks()
    threading_virus_checks()
    threading_mtr_checks()

    v4_thread.join()
    v6_thread.join()

    response_ping_internet_v4.sort()
    response_ping_internet_v6.sort()
    response_http_checks.sort()
    response_virus_checks.sort()
    response_mtr_checks.sort()

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
    for status in ping_internet_v4(response_ping_internet_v4):
        print(status)

    print("\033[1m\033[93m\n-------IPv6 Ping Results-------\033[0m")
    for status in response_ping_internet_v6:
        print(status)

    print("\033[1m\033[93m\n-------HTTP IPv4 Results-------\033[0m")
    for status in response_http_checks:
        if "IPv4" in status:
            print(status)

    print("\033[1m\033[93m\n-------HTTP IPv6 Results-------\033[0m")
    for status in response_http_checks:
        if "IPv6" in status:
            print(status)

    print("\033[1m\033[93m\n-------Virus Check Results-------\033[0m")
    for status in response_virus_checks:
        print(status)

    print("\033[1m\033[93m\n-------IPv4 MTR Results-------\033[0m")
    for result in response_mtr_checks:
        if 'IPv4' in result:
            print(result)

    print("\033[1m\033[93m\n-------IPv6 MTR Results-------\033[0m")
    for result in response_mtr_checks:
        if 'IPv6' in result:
            print(result)
    
if __name__ == '__main__':       
    while True:
        update_cli()
        time.sleep(1) 
