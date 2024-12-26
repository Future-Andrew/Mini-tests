import ctypes, sys
import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import time

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    # 主程序写在这里
    # 指定RAMMap的完整路径
    rammap_path = r"C:\Users\Andrew-WTG\Desktop\RAMMap.exe"

    class App:
        def __init__(self, root):
            self.root = root
            self.root.title("RAMMap自动清理程序")

            self.start_button = tk.Button(root, text="开始", command=self.start_cleaning)
            self.start_button.pack(pady=20)

            self.stop_button = tk.Button(root, text="停止", command=self.stop_cleaning)
            self.stop_button.pack(pady=20)

            self.running = False
            self.thread = None

        def start_cleaning(self):
            if not self.running:
                self.running = True
                self.start_button.config(state="disabled")
                self.thread = threading.Thread(target=self.cleaning_loop)
                self.thread.start()
            else:
                messagebox.showwarning("警告", "清理程序已经在运行了！")

        def stop_cleaning(self):
            self.running = False
            if self.thread:
                self.thread.join()  # 等待线程结束
            self.start_button.config(state="normal")

        def cleaning_loop(self):
            while self.running:
                try:
                    # 调用RAMMap命令，这里需要确保RAMMap的路径正确
                    subprocess.run([rammap_path, "-Ew"], check=True)
                    time.sleep(30)
                    subprocess.run([rammap_path, "-Es"], check=True)
                    time.sleep(30)
                    subprocess.run([rammap_path, "-Em"], check=True)
                    time.sleep(30)
                    subprocess.run([rammap_path, "-Et"], check=True)
                    time.sleep(30)
                    subprocess.run([rammap_path, "-E0"], check=True)
                    time.sleep(30)  # 延迟一分钟
                except subprocess.CalledProcessError as e:
                    self.root.after(0, lambda: messagebox.showerror("错误", f"命令执行失败: {e}"))
                    self.running = False
                except Exception as e:
                    self.root.after(0, lambda e=e: messagebox.showerror("错误", f"发生未知错误: {e}"))
                    self.running = False

    if __name__ == "__main__":
        root = tk.Tk()
        app = App(root)
        root.mainloop()
else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, '"{}"'.format(sys.argv[0]), None, 1)
