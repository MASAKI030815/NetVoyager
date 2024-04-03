import subprocess

def ping_internet_v4(host, name, pingv4_short_option, pingv4_large_option):
    # 小さいパケットでの ping 結果
    short_packet_cmd = ["ping"] + pingv4_short_option + [host]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    short_status = "OK" if short_packet_result.returncode == 0 else "NG"
    short_color = "\033[92m" if short_status == "OK" else "\033[91m"

    # 大きいパケットでの ping 結果
    large_packet_cmd = ["ping"] + pingv4_large_option + [host]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    large_status = "OK" if large_packet_result.returncode == 0 else "NG"
    large_color = "\033[92m" if large_status == "OK" else "\033[91m"
    
    # 総合的なステータス
    status = "OK" if short_status == "OK" and large_status == "OK" else "NG"
    status_color = "\033[92m" if status == "OK" else "\033[91m"

    # 結果の文字列を作成
    combined_status = f"{status_color}{status}\033[0m ({short_color}Short\033[0m / {large_color}Large\033[0m) : {host} ({name})"
    
    return combined_status
