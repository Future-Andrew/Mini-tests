import pandas as pd
import numpy as np

# 定义文件路径
file_path = r"C:\Users\王国聪\Desktop\111.xlsx"

# 读取Excel文件的所有工作表名称
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names
print("工作表名称列表：", sheet_names)

# 根据实际的工作表名称读取数据
df = pd.read_excel(file_path, sheet_name=sheet_names[0])  # 假设我们选择第一个工作表

# 处理时间字符串的函数
def format_time_string(s):
    # 检查是否为字符串
    if isinstance(s, str):
        if len(s) == 3:  # 如果长度为3，即只有小时和分钟，没有秒
            return s[:2] + '0' + s[2:]
        elif len(s) == 4:  # 如果长度为4，即小时、分钟和秒都有
            return s
        else:
            return s  # 或者 raise ValueError("Invalid time string length")
    else:
        # 如果不是字符串，返回原值
        return s

# 应用函数到指定列的每个元素
columns_to_format = ['1000米跑', '800米跑']
for column in columns_to_format:
    if column in df.columns:
        df[column] = df[column].apply(format_time_string)
    else:
        print(f"列名 '{column}' 不存在于DataFrame中。")

# 保存结果到新的Excel文件
output_path = r"C:\Users\王国聪\Desktop\111_Formatted.xlsx"  # 修改文件名以避免冲突
try:
    df.to_excel(output_path, index=False)
    print(f"文件已成功保存到：{output_path}")
except PermissionError as e:
    print(f"无法写入文件：{output_path}。请确保文件未被打开且有足够的权限。错误信息：{e}")

# 打印结果以验证
for column in columns_to_format:
    if column in df.columns:
        print(f"{column} 列的前几行数据:")
        print(df[column].head())