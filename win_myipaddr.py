import subprocess
import re

def myipaddr():
    try:
        # ipconfig コマンドを実行して結果を取得
        result = subprocess.check_output("ipconfig {}", encoding='utf-8', errors='ignore')

        # IPv4 アドレスの抽出
        ipv4_pattern = re.compile(r"IPv4 Address[ .:]+([\d.]+)")
        ipv4_addr = ipv4_pattern.findall(result)

        # サブネットマスクの抽出
        subnet_pattern = re.compile(r"Subnet Mask[ .:]+([\d.]+)")
        
        

        # デフォルトゲートウェイの抽出
        gateway_pattern = re.compile(r"Default Gateway[ .:]+([\d.]+)")
        gateway = gateway_pattern.findall(result)

        # IPv6 アドレスの抽出
        ipv6_pattern = re.compile(r"IPv6 Address[ .:]+([a-fA-F\d:]+)")
        ipv6_addr = ipv6_pattern.findall(result)

        # 複数のインターフェースがある場合があるため、リストを返す
        return ipv4_addr, subnet_mask, gateway, ipv6_addr
    except Exception as e:
        print(f"IPアドレス取得中にエラーが発生しました: {e}")
        return [], [], [], []
