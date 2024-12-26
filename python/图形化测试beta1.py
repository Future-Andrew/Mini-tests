import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

def get_current_username():
    return os.environ.get('USERNAME')  # 在Windows系统中获取用户名

def read_and_merge_files(file1, file2, file3):
    current_username = get_current_username()
    file1_path = fr'C:\Users\{current_username}\Desktop\{file1}.xlsx'
    file2_path = fr'C:\Users\{current_username}\Desktop\{file2}.xlsx'
    file3_path = fr'C:\Users\{current_username}\Desktop\{file3}.xlsx'

# 确保文件存在
    if not (os.path.exists(file1_path) and os.path.exists(file2_path) and os.path.exists(file3_path)):
        print("文件路径错误或文件不存在，请检查文件名和路径。")
    else:
        try:
            df1 = pd.read_excel(file1_path)
            print("成功读取工作簿1")
            print("工作簿1的前三个学籍号:", df1['学籍号'].head(3).tolist())
        except Exception as e:
            print(f"读取工作簿1时出错: {e}")
            exit()

        try:
            df2 = pd.read_excel(file2_path)
            print("成功读取工作簿2")
            print("工作簿2的前三个学籍号:", df2['证件号码'].head(3).tolist())
        except Exception as e:
            print(f"读取工作簿2时出错: {e}")
            exit()

        try:
            df3 = pd.read_excel(file3_path)
            print("成功读取工作簿3")
            print("工作簿3的前三个学籍号:", df3['证件号码'].head(3).tolist())
        except Exception as e:
            print(f"读取工作簿3时出错: {e}")
            exit()
    scores_map = {}

    # 合并df2和df3的数据到scores_map
    for df in [df2, df3]:
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

    # 填充df1
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
    print(f"数据已成功更新并保存到 {output_file_path}")

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, os.path.basename(file_path))  # 只插入文件名

def on_merge():
    file1 = os.path.splitext(file1_entry.get())[0] + '.xlsx'  # 确保文件名有.xlsx扩展名
    file2 = os.path.splitext(file2_entry.get())[0] + '.xlsx'
    file3 = os.path.splitext(file3_entry.get())[0] + '.xlsx'
    read_and_merge_files(file1, file2, file3)

root = tk.Tk()
root.title("Excel文件合并工具")

tk.Label(root, text="输入你要合并的文件名（不含.xlsx）：").grid(row=0, column=0)
file1_entry = tk.Entry(root)
file1_entry.grid(row=0, column=1)

tk.Label(root, text="输入你的数据来源1文件名（不含.xlsx）：").grid(row=1, column=0)
file2_entry = tk.Entry(root)
file2_entry.grid(row=1, column=1)

tk.Label(root, text="输入你的数据来源2文件名（不含.xlsx）：").grid(row=2, column=0)
file3_entry = tk.Entry(root)
file3_entry.grid(row=2, column=1)

browse_button = tk.Button(root, text="浏览文件", command=lambda: [browse_file(entry) for entry in [file1_entry, file2_entry, file3_entry]])
browse_button.grid(row=3, column=0, columnspan=2)

merge_button = tk.Button(root, text="合并文件", command=on_merge)
merge_button.grid(row=4, column=0, columnspan=2)

root.mainloop()