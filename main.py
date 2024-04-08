import sys
import time
from threading import Thread
import tkinter as tk
from queue import Queue
from myip_local_v4v6 import myip_local_v4v6
from ping_gateway_v4 import ping_gateway_v4
from ping_internet_v4 import ping_internet_v4
from ping_internet_v6 import ping_internet_v6

def worker(func, queue, key):
    while True:
        result = func()
        queue.put((key, result))
        time.sleep(1)

def display_result(text_widget, result):
    ansi_to_tkinter_color = {
        "92": "green",
        "91": "red",
        "93": "yellow",
        "0": "white",  # ANSIエスケープシーケンスのリセットを白色にマップ
    }

    parts = result.split('\033[')
    for part in parts:
        if 'm' in part:
            color_code, text = part.split('m', 1)
            color = ansi_to_tkinter_color.get(color_code[-2:], "white")  # デフォルトの色は白に設定
            text_widget.insert('end', text, color)
        else:
            text_widget.insert('end', part, "white")
    text_widget.insert('end', '\n')
    
def update_gui(text_widget, queue, order, results):
    while not queue.empty():
        key, result = queue.get()
        results[key] = result

    # 全てのキーに対する結果が存在するか確認
    if all(key in results for key in order):
        # テキストウィジェットをクリア
        text_widget.delete('1.0', tk.END)

        # 定義された順序に基づいて結果を表示
        for key in order:
            result = results[key]
            display_result(text_widget, result)

        # 全て表示したら結果をクリアする（次のサイクルのため）
        results.clear()

    # 再帰的に自身を呼び出し、継続的に更新を試みる
    text_widget.after(1000, lambda: update_gui(text_widget, queue, order, results))

if __name__ == '__main__':
    root = tk.Tk()
    text_widget = tk.Text(root, height=30, width=100, bg='black')
    text_widget.pack()

    for color, hex_color in [("green", "green"), ("red", "red"),("yellow", "yellow"),  ("white", "white")]:
        text_widget.tag_configure(color, foreground=hex_color)

    queue = Queue()
    order = ['myip_local_v4v6', 'ping_gateway_v4', 'ping_internet_v4', 'ping_internet_v6']
    functions = [myip_local_v4v6, ping_gateway_v4, ping_internet_v4, ping_internet_v6]

    results = {}  # 結果を保持する辞書
    for func, name in zip(functions, order):
        Thread(target=worker, args=(func, queue, name), daemon=True).start()

    update_gui(text_widget, queue, order, results)
    root.mainloop()
