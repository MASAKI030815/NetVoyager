import subprocess
import re
import config

def myipaddr():
    interface = config.interface
    # インターフェース名から IPv4 アドレスを取得
    try:
        ip_cmd = f"ip addr show {interface}"
        result = subprocess.check_output(ip_cmd.split()).decode('utf-8')
        
        # IPv4 アドレスの抽出
        ipv4_pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ipv4_match = re.search(ipv4_pattern, result)
        ipv4_addr = ipv4_match.group(1) if ipv4_match else None
        
        # ネットマスクの抽出
        netmask_pattern = r'inet \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/(\d{1,2})'
        netmask_match = re.search(netmask_pattern, result)
        netmask = netmask_match.group(1) if netmask_match else None

        # IPv6 アドレスの抽出
        ipv6_pattern = r'inet6 ([a-f0-9:]+)/\d{1,3} scope global'
        ipv6_match = re.search(ipv6_pattern, result)
        ipv6_addr = ipv6_match.group(1) if ipv6_match else None

        # ゲートウェイの取得
        gw_cmd = "ip route show default"
        gw_result = subprocess.check_output(gw_cmd.split()).decode('utf-8')
        gw_pattern = rf'default via (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) dev {config.interface}'
        gw_match = re.search(gw_pattern, gw_result)
        gateway = gw_match.group(1) if gw_match else None
        
        return ipv4_addr, netmask, gateway, ipv6_addr
    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")
        return None, None, None, None
