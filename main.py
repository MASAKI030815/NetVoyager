import sys
import time
from myipaddr import myipaddr
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4
from ping_internet_v6 import ping_internet_v6

def update_cli():
    sys.stdout.write("\033[H\033[J")

    print("\033[1m\033[93m-------Network Setting-------\033[0m")
    myipaddr()

    print("\033[1m\033[93m\n-------Gateway Ping Result-------\033[0m")
    ping_gateway_v4()
    

    print("\033[1m\033[93m\n-------IPv4 Ping Results-------\033[0m")
    ping_internet_v4()

    print("\033[1m\033[93m\n-------IPv6 Ping Results-------\033[0m")
    ping_internet_v6()
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
        time.sleep(3)
