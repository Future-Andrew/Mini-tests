import pyautogui
import time

key = input('请输入需要不停按下的键：')
while True:
    pyautogui.press(key)
    time.sleep(0.2)