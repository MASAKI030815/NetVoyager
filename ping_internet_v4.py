import subprocess
import config
import threading


response_ping_internet_v4 = []
response_ping_internet_v4_lock = threading.Lock()

def ping_internet_v4(host,name,pingv4_short_option,pingv4_large_option):
    short_packet_cmd = ["ping"] + pingv4_short_option + [host]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    short_status = "OK" if short_packet_result.returncode == 0 else "NG"
    short_color = "\033[92m" if short_status == "OK" else "\033[91m"

    large_packet_cmd = ["ping"] + pingv4_large_option + [host]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    large_status = "OK" if large_packet_result.returncode == 0 else "NG"
    large_color = "\033[92m" if large_status == "OK" else "\033[91m"
    
    status = "OK" if short_status == "OK" and large_status == "OK" else "NG"
    status_color = "\033[92m" if status == "OK" else "\033[91m"

    combined_status = f"{status_color}{status}\033[0m ({short_color}Short\033[0m / {large_color}Large\033[0m) : {host} ({name})"
    
    with response_ping_internet_v4_lock:
        response_ping_internet_v4.append(combined_status)
        return response_ping_internet_v4
    
def theading_ping_internet_v4():
    threads = []
    for i in range(len(config.pingv4_targets)):
        thread = threading.Thread(target=ping_internet_v4, args=(config.pingv4_targets[i][0], config.pingv4_targets[i][1]))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def threading_ping_v4():
    thread = threading.Thread(target=theading_ping_internet_v4)
    thread.start()
    return thread

