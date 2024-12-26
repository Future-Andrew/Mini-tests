import pandas as pd

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.xlsx'
df = pd.read_excel(file_path)

# 将'体重'和'身高'列转换为浮点数
df['体重'] = pd.to_numeric(df['体重'], errors='coerce')
df['身高'] = pd.to_numeric(df['身高'], errors='coerce')

# 如果身高是以厘米为单位，转换为米
df['身高'] = df['身高'] / 100  # 这里假设身高单位是厘米

# 计算BMI并创建一个新列
df['BMI'] = df.apply(lambda row: round(row['体重'] / (row['身高'] ** 2), 1) if row['身高'] > 0 else None, axis=1)

# BMI评分表
bmi_scores = {
    '男': {
        '高一': {'正常': (16.5, 23.2), '低体重': (None, 16.4), '超重': (23.3, 26.3), '肥胖': (26.4, None)},
        '高二': {'正常': (16.8, 23.7), '低体重': (None, 16.7), '超重': (23.8, 26.5), '肥胖': (26.6, None)},
        '高三': {'正常': (17.3, 23.8), '低体重': (None, 17.2), '超重': (23.9, 27.3), '肥胖': (27.4, None)}
    },
    '女': {
        '高一': {'正常': (16.5, 22.7), '低体重': (None, 16.4), '超重': (22.8, 25.2), '肥胖': (25.3, None)},
        '高二': {'正常': (16.9, 23.2), '低体重': (None, 16.8), '超重': (23.3, 25.4), '肥胖': (25.5, None)},
        '高三': {'正常': (17.1, 23.3), '低体重': (None, 17.0), '超重': (23.4, 25.7), '肥胖': (25.8, None)}
    }
}

def calculate_bmi_score(gender, grade, bmi):
    if gender not in ['男', '女']:
        return None  # 性别不识别
    if grade not in ['高一', '高二', '高三']:
        return None  # 年级不识别
    
    scores = bmi_scores[gender][grade]
    for category, (low, high) in scores.items():
        if low is None or bmi >= low:
            if high is None or bmi < high:
                return category
    return None  # 不符合任何类别

# 计算BMI评分并创建一个新列
df['BMI评分'] = df.apply(lambda row: calculate_bmi_score(row['性别'], row['班级名称'], row['BMI']), axis=1)

# 检索体重列的位置
weight_index = df.columns.get_loc('体重')

# 将BMI和BMI评分列插入到体重列后面
df.insert(weight_index + 1, 'BMI', df.pop('BMI'))
df.insert(weight_index + 2, 'BMI评分', df.pop('BMI评分'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.1.xlsx'
df.to_excel(output_file_path, index=False)

# 打印DataFrame的头部以检查输出
print(df.head())

print(f'BMI及评分已添加到新的Excel文件：{output_file_path}')