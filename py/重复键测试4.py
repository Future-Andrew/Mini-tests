import pyautogui
import time
import threading
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# 全局变量，用于控制程序的运行状态
running = True

def press_key_continuously(key):
    """持续按下指定的键"""
    while running:
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)

def press_right_then_space():
    """先按下右键再按空格"""
    while running:
        pyautogui.press('right')
        time.sleep(0.1)
        pyautogui.press('space')

def start_pressing():
    """启动按键线程"""
    global key_press_thread, right_space_thread
    key_press_thread = threading.Thread(target=press_key_continuously, args=(key,))
    right_space_thread = threading.Thread(target=press_right_then_space)
    key_press_thread.start()
    right_space_thread.start()

def stop_pressing():
    """停止按键线程"""
    global running
    running = False
    if key_press_thread.is_alive():
        key_press_thread.join()
    if right_space_thread.is_alive():
        right_space_thread.join()
    messagebox.showinfo("信息", "按键程序已停止")

# 创建主窗口
root = tk.Tk()
root.title("按键控制程序")

# 获取用户输入
key = simpledialog.askstring("输入", '请输入需要不停按下的键：', parent=root)

if key is None:
    root.destroy()
    exit("用户取消了输入。")

# 创建控制按钮
start_button = tk.Button(root, text="开始", command=start_pressing)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="停止", command=stop_pressing)
stop_button.pack(pady=20)

# 运行GUI主循环
root.mainloop()
