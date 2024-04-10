import netifaces

def myip_local_v4v6():
    ipv6_addr = ipv4_addr = netmask = gateway = interface = None

    try:
        # デフォルトの IPv4 ゲートウェイが存在するか確認
        default_gateway = netifaces.gateways().get('default', {}).get(netifaces.AF_INET)

        if default_gateway:
            interface = default_gateway[1]
            addrs = netifaces.ifaddresses(interface)

            if netifaces.AF_INET in addrs:
                ipv4_info = addrs[netifaces.AF_INET][0]
                ipv4_addr = ipv4_info.get('addr')
                netmask = ipv4_info.get('netmask')
            
            gateway = default_gateway[0]

            if netifaces.AF_INET6 in addrs:
                for addr_info in addrs[netifaces.AF_INET6]:
                    if not addr_info['addr'].startswith('fe80'):
                        ipv6_addr = addr_info['addr'].split('%')[0]
                        break

    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")
    
    response = "\033[1m\033[93m-------Network Setting-------\033[0m\n"
    if interface:
        response += f"Interface: {interface}\n"

    if ipv4_addr and netmask:
        response += f"IPv4 Address: {ipv4_addr}\n"
        response += f"Netmask: {netmask}\n"

    if gateway:
        response += f"Default Gateway: {gateway}\n"

    if ipv6_addr:
        response += f"IPv6 Address: {ipv6_addr}\n"

    return response

# test
#print(myip_local_v4v6())
