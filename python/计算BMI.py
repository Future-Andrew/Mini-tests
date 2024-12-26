import pandas as pd

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.xlsx'  # 假设你的文件名为1.xlsx
df = pd.read_excel(file_path)

# 计算BMI，跳过空值，并精确到小数点后一位
def calculate_bmi(height, weight):
    if pd.notnull(height) and pd.notnull(weight):
        # 将height和weight转换为数值类型
        height = pd.to_numeric(height, errors='coerce')
        weight = pd.to_numeric(weight, errors='coerce')
        if pd.notnull(height) and pd.notnull(weight):
            # 计算BMI并四舍五入到小数点后一位
            bmi = weight / ((height / 100) ** 2)
            return round(bmi, 1)
        else:
            return None  # 返回None以表示空值或转换失败
    else:
        return None  # 返回None以表示空值

# 假设身高和体重数据在不同的列，我们需要遍历DataFrame的每一行
for index, row in df.iterrows():
    height = row['身高']
    weight = row['体重']
    df.at[index, 'BMI'] = calculate_bmi(height, weight)

# 保存新的Excel文件，你可以自定义文件名
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.1.xlsx'
df.to_excel(output_file_path, index=False)

print(f'BMI列已添加到新的Excel文件：{output_file_path}')