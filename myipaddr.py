import netifaces
import config

def myipaddr():
    ipv6_addr = None
    ipv4_addr = None
    netmask = None
    gateway = None
    try:
        addrs = netifaces.ifaddresses(config.interface)
        if netifaces.AF_INET in addrs:
            ipv4_info = addrs[netifaces.AF_INET][0]
            ipv4_addr = ipv4_info.get('addr')
            netmask = ipv4_info.get('netmask')
        gateways = netifaces.gateways()
        if netifaces.AF_INET in gateways['default']:
            gateway = gateways['default'][netifaces.AF_INET][0]
        if netifaces.AF_INET6 in addrs:
            for addr_info in addrs[netifaces.AF_INET6]:
                if addr_info['addr'].startswith('fe80') is False:
                    ipv6_addr = addr_info['addr'].split('%')[0]
                    break
    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")
    
    print(f"Interface: {config.interface}")
    if ipv4_addr and netmask:
        print(f"IPv4 Address: {ipv4_addr}")
        print(f"Netmask: {netmask}")
    if gateway:
        print(f"Default Gateway: {gateway}")
    if ipv6_addr:
        print(f"IPv6 Address: {ipv6_addr}")
