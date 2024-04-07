import sys
import time
import threading
from myip_local_v4v6 import myip_local_v4v6
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4
from ping_internet_v6 import ping_internet_v6

def worker(func, results, key):
    result = func()
    results[key] = result

def update_cli():

    results = {}
    keys = ['myip_local_v4v6', 'ping_gateway_v4', 'ping_internet_v4', 'ping_internet_v6']
    functions = [myip_local_v4v6, ping_gateway_v4, ping_internet_v4, ping_internet_v6]

    threads = []
    for key, func in zip(keys, functions):
        thread = threading.Thread(target=worker, args=(func, results, key))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
    sys.stdout.write("\033[H\033[J")
    # 関数が完了した順ではなく、定義された順序で結果を表示
    for key in keys:
        print(results[key])

if __name__ == '__main__':       
    while True:
        update_cli()
        time.sleep(3)