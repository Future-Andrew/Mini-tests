#pyautogui.keyDown() ： 模拟按键按下

#pyautogui.keyUp() ： 模拟按键释放

#pyautogui.press() ： 相当于先按下再释放
import pyautogui
import time
import threading

# 全局变量，用于控制程序的运行状态
running = True

def press_key_continuously(key):
    """持续按下指定的键"""
    for i in range(1500):
        pyautogui.press(key)
        time.sleep(0.2)


def press_keys_periodically(key1, key2, interval1, interval2):
    """定期按下两个键"""
    for i in range(1):
        pyautogui.keyDown(key1)
        time.sleep(interval1)  # 等待5分钟
        pyautogui.press(key2)
        time.sleep(interval2)  # 等待10秒

# 获取用户输入
key = input('请输入需要不停按下的键：')
key1 = "n"
key2 = "m"

# 创建并启动线程
key_press_thread = threading.Thread(target=press_key_continuously, args=(key,))
periodic_key_press_thread = threading.Thread(target=press_keys_periodically, args=(key1, key2, 300, 10))

key_press_thread.start()  # 启动持续按键线程
periodic_key_press_thread.start()  # 启动定期按键线程

# 监听键盘事件，当按下'q'键时停止程序
def on_press(key):
    global running
    if key == keyboard.KeyCode.from_char('q'):
        running = False
        print("程序已停止")
        # 停止所有线程
        key_press_thread.join()
        periodic_key_press_thread.join()

# 使用pynput库监听键盘事件
from pynput import keyboard
listener = keyboard.Listener(on_press=on_press)
listener.start()

# 防止主线程退出
key_press_thread.join()
periodic_key_press_thread.join()