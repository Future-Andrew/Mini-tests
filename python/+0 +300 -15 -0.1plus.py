import pandas as pd
import numpy as np

# 获取文件路径
file_path = input("请问你的文件路径:")

try:
    # 读取Excel文件的所有工作表名称
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print("工作表名称列表：", sheet_names)

    # 根据实际的工作表名称读取数据
    df = pd.read_excel(file_path, sheet_name=sheet_names[0])  # 假设我们选择第一个工作表

    # 新的DataFrame用于存储结果
    new_df = pd.DataFrame()

    # 处理时间字符串的函数
    def format_time_string(x):
        try:
            if isinstance(x, str):
                x = x.strip()  # 去除可能的空格
                if len(x) == 4 and (x[1] == "'" or x[1] == "’"):  # 检查是否包含单引号分隔符
                    # 分离分钟和秒
                    minute = int(x[0])
                    second = int(x[2:4])  # 直接取后两位作为秒
                    
                    # 执行计算，这里减去15秒
                    total_seconds = (minute * 60 + second) - 15
                    new_minute = total_seconds // 60
                    new_second = total_seconds % 60
                    
                    # 格式化为新的字符串'm''ss'
                    return f"{new_minute}'{new_second:02d}"
                elif len(x) == 3:  # 如果长度为3，即只有小时和分钟，没有秒
                    return x[:2] + '0' + x[2:]
                else:
                    return x  # 或者 raise ValueError("Invalid time string length")
            else:
                # 如果不是字符串，返回NaN
                return pd.NA
        except ValueError:
            # 如果转换失败，返回原始值
            return x

    # 减去300的函数
    def subtract_300(value):
        if isinstance(value, (int, float)):
            return value + 300
        else:
            return value

    # 减去0.1秒的函数
    def subtract_0_1(value):
        if isinstance(value, (int, float)):
            return value - 0.1
        else:
            return value

    # 遍历所有列
    for column in df.columns:
        # 检查列名是否包含关键词“得分”
        if '得分' in column:
            # 如果包含“得分”，则直接将该列添加到新的DataFrame中
            new_df[column] = df[column]
        else:
            # 如果不包含“得分”，则根据其他条件进行处理
            if '50米' in column:
                # 对“50米”列进行减去0.1秒的处理
                new_df[column] = df[column].apply(subtract_0_1)
            elif '800米' in column or '1000米' in column:
                new_df[column] = df[column].apply(format_time_string)
            elif '肺活量' in column:
                new_df[column] = df[column].apply(subtract_300)
            else:
                new_df[column] = df[column]

    # 保存结果到新的Excel文件
    output_path = file_path.replace('.xlsx', '+new.xlsx')  # 修改文件名以避免冲突
    new_df.to_excel(output_path, index=False)
    print(f"文件已成功保存到：{output_path}")

except FileNotFoundError as e:
    print(f"无法找到文件：{file_path}。请检查文件路径是否正确。错误信息：{e}")
except Exception as e:
    print(f"处理文件时发生错误：{e}")