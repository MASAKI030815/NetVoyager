import netifaces
import config

def myip_local_v4v6():
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
    
    response_myip_local_v4v6 = "\033[1m\033[93m-------Network Setting-------\033[0m\n"
    response_myip_local_v4v6 +=f"Interface: {config.interface}\n"
    if ipv4_addr and netmask:
        response_myip_local_v4v6 +=f"IPv4 Address: {ipv4_addr}\n"
        response_myip_local_v4v6 +=f"Netmask: {netmask}\n"
    if gateway:
        response_myip_local_v4v6 +=f"Default Gateway: {gateway}\n"
    if ipv6_addr:
        response_myip_local_v4v6 +=f"IPv6 Address: {ipv6_addr}\n"
    return response_myip_local_v4v6
