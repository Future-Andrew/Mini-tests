import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

def get_current_username():
    return os.environ.get('USERNAME')  # 在Windows系统中获取用户名

def read_and_merge_files(file_names):
    current_username = get_current_username()
    file_paths = []
    for file_name in file_names:
        file_path = fr'C:\Users\{current_username}\Desktop\{file_name}.xlsx'
        if not os.path.exists(file_path):
            messagebox.showerror("错误", f"文件 {file_name}.xlsx 不存在，请检查文件名和路径。")
            return
        file_paths.append(file_path)

    try:
        df_list = [pd.read_excel(path) for path in file_paths]
    except Exception as e:
        messagebox.showerror("错误", f"读取文件时出错: {e}")
        return

    scores_map = {}
    # 合并df的数据到scores_map
    for df in df_list:
        for index, row in df.iterrows():
            student_id = row['证件号码']
            scores_map[student_id] = {
                '肺活量': row['肺活量成绩'],
                '坐位体前屈': row['坐位体前屈成绩'],
                '立定跳远': row['立定跳远成绩'],
                '50米跑': row['50米跑成绩'],
                '1000米跑': row['1000米跑成绩'],
                '身高': row['身高成绩'],
                '体重': row['体重成绩'],
                '800米跑': row['800米跑成绩'],
                '一分钟仰卧起坐': row['一分钟仰卧起坐'],
                '引体向上': row['引体向上'],
            }

    # 假设第一个文件是主文件，需要填充数据
    df1 = df_list[0]
    for index, row in df1.iterrows():
        student_id = row['学籍号']
        if student_id in scores_map:
            df1.at[index, '肺活量'] = scores_map[student_id]['肺活量']
            df1.at[index, '坐位体前屈'] = scores_map[student_id]['坐位体前屈']
            df1.at[index, '立定跳远'] = scores_map[student_id]['立定跳远']
            df1.at[index, '50米跑'] = scores_map[student_id]['50米跑']
            df1.at[index, '1000米跑'] = scores_map[student_id]['1000米跑']
            df1.at[index, '身高'] = scores_map[student_id]['身高']
            df1.at[index, '体重'] = scores_map[student_id]['体重']
            df1.at[index, '800米跑'] = scores_map[student_id]['800米跑']
            df1.at[index, '一分钟仰卧起坐'] = scores_map[student_id]['一分钟仰卧起坐']
            df1.at[index, '引体向上'] = scores_map[student_id]['引体向上']

    output_file_path = fr'C:\Users\{current_username}\Desktop\广州市贸易职业高级中学体测模版(合).xlsx'
    df1.to_excel(output_file_path, index=False)
    messagebox.showinfo("完成", f"数据已成功更新并保存到 {output_file_path}")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, os.path.splitext(os.path.basename(file_path))[0])  # 只插入文件名，不含扩展名

def on_merge():
    num_files = int(file_num_entry.get())
    file_entries = [file_entry.get() for file_entry in file_entries_list]
    if not all(file_entries):
        messagebox.showerror("错误", "所有文件名必须填写完整。")
        return
    file_names = [f"{entry}.xlsx" for entry in file_entries]
    read_and_merge_files(file_names)

root = tk.Tk()
root.title("Excel文件合并工具")

tk.Label(root, text="请输入文件数量：").grid(row=0, column=0)
file_num_entry = tk.Entry(root)
file_num_entry.grid(row=0, column=1)

file_entries_list = []
for i in range(3):  # 根据需要调整范围
    tk.Label(root, text=f"输入文件{i+1}名（不含.xlsx）：").grid(row=i+1, column=0)
    file_entry = tk.Entry(root)
    file_entry.grid(row=i+1, column=1)
    file_entries_list.append(file_entry)

browse_button = tk.Button(root, text="浏览文件", command=lambda: [browse_file(entry) for entry in file_entries_list])
browse_button.grid(row=4, column=0, columnspan=2)

merge_button = tk.Button(root, text="合并文件", command=on_merge)
merge_button.grid(row=5, column=0, columnspan=2)

root.mainloop()