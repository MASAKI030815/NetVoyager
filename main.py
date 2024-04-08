import sys
import time
import threading
import tkinter
from myip_local_v4v6 import myip_local_v4v6
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4
from ping_internet_v6 import ping_internet_v6

def worker(func, results, key, callback):
    result = func()
    results[key] = result
    callback(key, result)  # 結果をコールバック関数を使って通知

def update_gui(key, result):
    # GUIを更新する関数
    labels[key].config(text=f"{key}: {result}")

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Network Status")
    root.geometry("800x600")

    ansi_to_tkinter_color = {
        "\033[91m": "red",
        "\033[92m": "green",
        # 他の色に関するマッピングも追加可能
    }
    # ANSIエスケープシーケンスをTkinterの色に変換
    tkinter_color = ansi_to_tkinter_color.get(ansi_color_string, "black")  # デフォルトは黒色

    # 結果を表示するためのラベルを作成
    labels = {}
    keys = ['myip_local_v4v6', 'ping_gateway_v4', 'ping_internet_v4', 'ping_internet_v6']
    for key in keys:
        label = tkinter.Label(root, text=f"{key}: Waiting for result...")
        label.pack()
        labels[key] = label

    # スレッドを開始して非同期に情報を取得し、GUIを更新
    functions = [myip_local_v4v6, ping_gateway_v4, ping_internet_v4, ping_internet_v6]
    results = {}
    for key, func in zip(keys, functions):
        thread = threading.Thread(target=worker, args=(func, results, key, lambda k, r: root.after(0, update_gui, k, r)))
        thread.start()

    root.mainloop()