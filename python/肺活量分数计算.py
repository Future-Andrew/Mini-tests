import pandas as pd

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.1.xlsx'
df = pd.read_excel(file_path)

# 将'肺活量'列转换为浮点数
df['肺活量'] = pd.to_numeric(df['肺活量'], errors='coerce')

# 肺活量单项评分表
male_scores = {
    '100': [4540.0, 4740.0, 4940.0],
    '95': [4420.0, 4620.0, 4820.0],
    '90': [4300.0, 4500.0, 4700.0],
    '85': [4050.0, 4250.0, 4450.0],
    '80': [3800.0, 4000.0, 4200.0],
    '78': [3680.0, 3880.0, 4080.0],
    '76': [3560.0, 3760.0, 3960.0],
    '74': [3440.0, 3640.0, 3840.0],
    '72': [3320.0, 3520.0, 3720.0],
    '70': [3200.0, 3400.0, 3600.0],
    '68': [3080.0, 3280.0, 3480.0],
    '66': [2960.0, 3160.0, 3360.0],
    '64': [2840.0, 3040.0, 3240.0],
    '62': [2720.0, 2920.0, 3120.0],
    '60': [2600.0, 2800.0, 3000.0],
    '50': [2470.0, 2660.0, 2850.0],
    '40': [2340.0, 2520.0, 2700.0],
    '30': [2210.0, 2380.0, 2550.0],
    '20': [2080.0, 2240.0, 2400.0],
    '10': [1950.0, 2100.0, 2250.0]
}

female_scores = {
    '100': [3150.0, 3250.0, 3350.0],
    '95': [3100.0, 3200.0, 3300.0],
    '90': [3050.0, 3150.0, 3250.0],
    '85': [2900.0, 3000.0, 3100.0],
    '80': [2750.0, 2850.0, 2950.0],
    '78': [2650.0, 2750.0, 2850.0],
    '76': [2550.0, 2650.0, 2750.0],
    '74': [2450.0, 2550.0, 2650.0],
    '72': [2350.0, 2450.0, 2550.0],
    '70': [2250.0, 2350.0, 2450.0],
    '68': [2150.0, 2250.0, 2350.0],
    '66': [2050.0, 2150.0, 2250.0],
    '64': [1950.0, 2050.0, 2150.0],
    '62': [1850.0, 1950.0, 2050.0],
    '60': [1750.0, 1850.0, 1950.0],
    '50': [1710.0, 1810.0, 1910.0],
    '40': [1670.0, 1770.0, 1870.0],
    '30': [1630.0, 1730.0, 1830.0],
    '20': [1590.0, 1690.0, 1790.0],
    '10': [1550.0, 1650.0, 1750.0]
}

def calculate_lung_capacity_score(gender, lung_capacity, grade):
    if gender == 1:  # 男性
        scores = male_scores
    elif gender == 2:  # 女性
        scores = female_scores
    else:
        return None  # 性别不识别

    # 根据年级选择对应的肺活量单项评分
    if '高一' in grade:
        grade_index = 0
    elif '高二' in grade:
        grade_index = 1
    elif '高三' in grade:
        grade_index = 2
    elif '2024' in grade:
        grade_index = 0
    elif '2023' in grade:
        grade_index = 1
    elif '2022' in grade:
        grade_index = 2
    else:
        return None  # 年级不识别

    # 根据肺活量找到对应的评分
    if lung_capacity >= scores['90'][grade_index]:
        return '优秀'
    elif lung_capacity >= scores['80'][grade_index]:
        return '良好'
    elif lung_capacity >= scores['60'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['10'][grade_index]:
        return '不及格'
    else:
        return None  # 小于10输出空值

# 计算肺活量评分并创建一个新列
df['肺活量成绩'] = df.apply(lambda row: calculate_lung_capacity_score(row['性别'], row['肺活量'], row['班级名称']), axis=1)

# 找到'肺活量'列的索引位置
index_of_lung_capacity = df.columns.get_loc('肺活量')

# 在'肺活量'列后面插入'肺活量成绩'列
# 注意：这里我们假设'肺活量评分'列已经存在于df中，只是需要移动位置
df.insert(index_of_lung_capacity + 1, '肺活量成绩', df.pop('肺活量成绩'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.2.xlsx'
df.to_excel(output_file_path, index=False)

print(f'肺活量单项评分已添加到新的Excel文件：{output_file_path}')