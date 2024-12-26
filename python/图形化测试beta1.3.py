import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def get_current_username():
    return os.environ.get('USERNAME')  # 在Windows系统中获取用户名

def read_and_merge_files(file_paths):
    current_username = get_current_username()
    for file_path in file_paths:
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {os.path.basename(file_path)} 不存在，请检查文件名和路径。")
            return

    try:
        df_list = [pd.read_excel(path) for path in file_paths]
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出错: {e}")
        return

    # 打印成功读取的文件信息
    for i, df in enumerate(df_list, start=1):
        if '学籍号' in df.columns:
            print(f"成功读取工作簿{i}")
            print("工作簿的前三个学籍号:", df['学籍号'].head(3).tolist())
        elif '证件号码' in df.columns:
            print(f"成功读取工作簿{i}")
            print("工作簿的前三个证件号码:", df['证件号码'].head(3).tolist())
        else:
            messagebox.showerror("错误", "工作簿中没有找到 '学籍号' 或 '证件号码' 列。")
            return

    scores_map = {}
# 合并df的数据到scores_map
    for df in df_list[1:]:  # 假设第一个文件是主文件，不包含成绩数据
        for index, row in df.iterrows():
            student_id = row.get('证件号码')
            if student_id is None:
                continue  # 如果找不到'证件号码'，跳过这一行
            scores_map[student_id] = {
                '肺活量': row.get('肺活量成绩'),
                '坐位体前屈': row.get('坐位体前屈成绩'),
                '立定跳远': row.get('立定跳远成绩'),
                '50米跑': row.get('50米跑成绩'),
                '1000米跑': row.get('1000米跑成绩'),
                '身高': row.get('身高成绩'),
                '体重': row.get('体重成绩'),
                '800米跑': row.get('800米跑成绩'),
                # 检查可能的列名，并使用第一个找到的非空值
                '一分钟仰卧起坐': row.get('一分钟仰卧起坐') or row.get('仰卧起坐成绩') or row.get("仰卧起坐"),
                '引体向上': row.get('引体向上'),
            }

    # 填充df1
    df1 = df_list[0]
    for index, row in df1.iterrows():
        student_id = row.get('学籍号')
        if student_id is None:
            continue  # 如果找不到'学籍号'，跳过这一行
        if student_id in scores_map:
            for key, value in scores_map[student_id].items():
                df1.at[index, key] = value

    output_file_path = fr'C:\Users\{current_username}\Desktop\广州市贸易职业高级中学体测模版(合).xlsx'
    df1.to_excel(output_file_path, index=False)
    messagebox.showinfo("完成", f"数据已成功更新并保存到 {output_file_path}")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)  # 插入完整文件路径

def on_merge():
    num_files = file_num_entry.get()
    if not num_files.isdigit():
        messagebox.showerror("错误", "请输入有效的文件数量。")
        return
    num_files = int(num_files)
    file_entries = [file_entry.get() for file_entry in file_entries_list]
    if not all(file_entries):
        messagebox.showerror("错误", "所有文件名必须填写完整。")
        return
    file_paths = [entry for entry in file_entries]  # 获取完整文件路径
    read_and_merge_files(file_paths)

root = tk.Tk()
root.title("Excel文件合并工具")

tk.Label(root, text="请输入文件数量：").grid(row=0, column=0)
file_num_entry = tk.Entry(root)
file_num_entry.grid(row=0, column=1)

file_entries_list = []
for i in range(3):  # 根据需要调整范围
    tk.Label(root, text=f"输入文件{i+1}名（含路径）：").grid(row=i+1, column=0)
    file_entry = tk.Entry(root)
    file_entry.grid(row=i+1, column=1)
    file_entries_list.append(file_entry)

browse_button = tk.Button(root, text="浏览文件", command=lambda: [browse_file(entry) for entry in file_entries_list])
browse_button.grid(row=4, column=0, columnspan=2)

merge_button = tk.Button(root, text="合并文件", command=on_merge)
merge_button.grid(row=5, column=0, columnspan=2)

root.mainloop()