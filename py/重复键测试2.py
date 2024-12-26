#pyautogui.keyDown() ： 模拟按键按下

#pyautogui.keyUp() ： 模拟按键释放

#pyautogui.press() ： 相当于先按下再释放
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

import pyautogui
pyautogui.FAILSAFE = True
#当鼠标在左上角时，自动强制停止程序（抛出一个程序错误，停止程序运行）

# 全局变量，用于控制程序的运行状态
running_event = threading.Event()
lock = threading.Lock()

def press_key_continuously(key):
    """持续按下指定的键"""
    while running_event.is_set():
        with lock:
            pyautogui.press(key)
            time.sleep(0.2)

def press_keys_periodically(key1, key2):
    """定期按下两个键"""
    while running_event.is_set():
        with lock:
            pyautogui.press(key1)
            time.sleep(2)  # 等待2秒
            pyautogui.press(key2)
            time.sleep(2)
            pyautogui.keyDown(key2)
            time.sleep(10)  # 等待10秒
            pyautogui.keyUp(key2)
            pyautogui.press(key1)  # 等待10秒
        # 每10分钟执行一次
        time.sleep(300)

def start_pressing():
    """启动按键线程"""
    global key_press_thread, periodic_key_press_thread
    running_event.set()  # 设置事件为True，开始运行
    key_press_thread = threading.Thread(target=press_key_continuously, args=(key,))
    periodic_key_press_thread = threading.Thread(target=press_keys_periodically, args=(key1, key2))
    key_press_thread.start()
    periodic_key_press_thread.start()

def stop_pressing():
    """停止按键线程"""
    running_event.clear()  # 清除事件，停止运行
    if key_press_thread.is_alive():
        key_press_thread.join()
    if periodic_key_press_thread.is_alive():
        periodic_key_press_thread.join()
    messagebox.showinfo("信息", "按键程序已停止")

# 创建主窗口
root = tk.Tk()
root.title("按键控制程序")

# 获取用户输入
key = simpledialog.askstring("输入", '请输入需要不停按下的键：', parent=root)

if key is None:
    root.destroy()
    exit("用户取消了输入。")

key1 = "n"
key2 = "m"

# 创建控制按钮
start_button = tk.Button(root, text="开始", command=start_pressing)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="停止", command=stop_pressing)
stop_button.pack(pady=20)

# 运行GUI主循环
root.mainloop()