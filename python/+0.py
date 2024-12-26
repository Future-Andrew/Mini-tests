import pandas as pd

# 定义文件路径
file_path = r"C:\Users\王国聪\Downloads\广州贸易职业技术学校测试数据(2)(修改版).xlsx"

# 读取Excel文件
df = pd.read_excel(file_path, sheet_name="测试数据")

# 假设时间数据在名为'时间'的列中
# 处理时间字符串的函数
def format_time_string(s):
    # 检查字符串长度
    if len(s) == 3:  # 如果长度为3，即只有小时和分钟，没有秒
        # 在第三位添加0
        return s[:2] + '0' + s[2:]
    elif len(s) == 4:  # 如果长度为4，即小时、分钟和秒都有
        # 跳过，不做任何改变
        return s
    else:
        # 如果长度既不是3也不是4，可以选择抛出异常或者返回原字符串
        return s  # 或者 raise ValueError("Invalid time string length")

# 应用函数到'时间'列的每个元素
# 确保列名与你的Excel文件中的列名相匹配
df['800米跑成绩'] = df['800米跑成绩'].apply(format_time_string)

# 保存结果到新的Excel文件
output_path = r"C:\Users\王国聪\Downloads\广州贸易职业技术学校测试数据(2)(修改版)_Formatted.xlsx"
df.to_excel(output_path, index=False)

# 打印结果以验证
print(df['800米跑成绩'].head())
