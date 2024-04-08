import config
import subprocess
import netifaces
import tkinter as tk
import tkinter.font as tkFont

def ping_gateway_v4():
    results = {}
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    
    short_packet_cmd = ["ping"] + config.pingv4_short_option + [default_gateway]
    short_packet_result = subprocess.run(short_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['short'] = short_packet_result.returncode

    large_packet_cmd = ["ping"] + config.pingv4_large_option + [default_gateway]
    large_packet_result = subprocess.run(large_packet_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    results['large'] = large_packet_result.returncode
    return results

def display_gateway_v4():
    title = "-------Gateway Ping Results-------\n"
    results = ping_gateway_v4()
    short_result = results['short']
    large_result = results['large']

    # 全体のステータスがOKかNGかを判断し、NGのみを表示
    if short_result != 0 or large_result != 0:
        overall_status_text = "NG"
    else:
        overall_status_text = "OK"

    gateway_ip = netifaces.gateways()['default'][netifaces.AF_INET][0]
    result_text = f"{title}{overall_status_text} (Short / Large) : {gateway_ip}\n\n"
    widget_gateway_text.insert(tk.END, result_text)

    widget_gateway_text.tag_add(f"1", f"1.0",f"1.end")
    widget_gateway_text.tag_config(f"1", foreground="yellow",font=bold_font)    

    # 全体のステータスに対するタグ設定
    widget_gateway_text.tag_add("overall", "2.0", f"2.{len(overall_status_text)}")
    widget_gateway_text.tag_config("overall", foreground="green" if overall_status_text == "OK" else "red", font=bold_font)

    # Short の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("short", "2.4", "2.10")  # "Short"
    widget_gateway_text.tag_config("short", foreground="green" if short_result == 0 else "red", font=bold_font)

    # Large の結果に適用するタグを追加（文字色で表示）
    widget_gateway_text.tag_add("large", "2.12", "2.17")  # "Large"
    widget_gateway_text.tag_config("large", foreground="green" if large_result == 0 else "red", font=bold_font)

root = tk.Tk()
root.title("Network Diagnostic Tool")
root.configure(bg="black")

# 太字フォントの設定
bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
widget_gateway_text = tk.Text(root, height=3, width=50, bg="black", fg="white",borderwidth=0, highlightthickness=0)
widget_gateway_text.grid(row=0, column=0, padx=10, pady=10)

display_gateway_v4()

root.mainloop()