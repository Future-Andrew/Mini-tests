import pandas as pd
import numpy as np

# 获取文件路径
file_path = input("请问你的文件路径:")

# 读取Excel文件的所有工作表名称
try:
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print("工作表名称列表：", sheet_names)

    # 根据实际的工作表名称读取数据
    df = pd.read_excel(file_path, sheet_name=sheet_names[0])  # 假设我们选择第一个工作表

    # 处理时间字符串的函数
    def format_time_string(s):
        # 检查是否为字符串
        if isinstance(s, str):
            s = s.strip()  # 去除可能的空格
            if len(s) == 4 and s[1] == "'" or "’":  # 检查是否包含单引号分隔符
                # 分离分钟和秒
                minute = int(s[0])
                second = int(s[2:4])  # 直接取后两位作为秒
                
                # 执行计算，这里减去15秒
                total_seconds = (minute * 60 + second) - 15
                new_minute = total_seconds // 60
                new_second = total_seconds % 60
                
                # 格式化为新的字符串'm''ss'
                return f"{new_minute}'{new_second:02d}"
            elif len(s) == 3:  # 如果长度为3，即只有小时和分钟，没有秒
                return s[:2] + '0' + s[2:]
            else:
                return s  # 或者 raise ValueError("Invalid time string length")
        else:
            # 如果不是字符串，返回NaN
            return np.nan

    # 应用函数到指定列的每个元素
    columns_to_format = ['1000米跑', '800米跑']
    for column in columns_to_format:
        if column in df.columns:
            df[column] = df[column].apply(format_time_string)
        else:
            print(f"列名 '{column}' 不存在于DataFrame中。")

    # 减去300的函数
    def subtract_300(value):
        # 确保值是数字
        if isinstance(value, (int, float)):
            return value + 300
        else:
            return value

    # 应用函数到“肺活量”列
    if '肺活量' in df.columns:
        df['肺活量'] = df['肺活量'].apply(subtract_300)
    else:
        print("列名 '肺活量' 不存在于DataFrame中。")

    # 减去0.1秒的函数
    def subtract_0_1(value):
        # 确保值是数字
        if isinstance(value, (int, float)):
            return value - 0.1
        else:
            return value

    # 应用函数到“50米跑”列
    if '50米跑' in df.columns:
        df['50米跑'] = df['50米跑'].apply(subtract_0_1)
    else:
        print("列名 '50米跑' 不存在于DataFrame中。")

    # 保存结果到新的Excel文件
    output_path = file_path.replace('.xlsx', '+new.xlsx')  # 修改文件名以避免冲突
    try:
        df.to_excel(output_path, index=False)
        print(f"文件已成功保存到：{output_path}")
    except PermissionError as e:
        print(f"无法写入文件：{output_path}。请确保文件未被打开且有足够的权限。错误信息：{e}")
except FileNotFoundError as e:
    print(f"无法找到文件：{file_path}。请检查文件路径是否正确。错误信息：{e}")