import pandas as pd
import numpy as np
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

# 打印DataFrame的头部以检查BMI列
print("BMI列已添加:")
print(df.head())

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
        if (low is None or bmi >= low) and (high is None or bmi < high):
            return category
    return None  # 不符合任何类别

# 计算BMI评分并创建一个新列
df['BMI评分'] = df.apply(lambda row: calculate_bmi_score(row['性别'], row['班级名称'], row['BMI']), axis=1)

# 打印DataFrame的头部以检查BMI评分列
print("BMI评分列已添加:")
print(df.head())

# 检索体重列的位置
weight_index = df.columns.get_loc('体重')

# 将BMI和BMI评分列插入到体重列后面
df.insert(weight_index + 1, 'BMI', df.pop('BMI'))
df.insert(weight_index + 2, 'BMI评分', df.pop('BMI评分'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.1.xlsx'
df.to_excel(output_file_path, index=False)

print(f'BMI及评分已添加到新的Excel文件：{output_file_path}')

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
    if lung_capacity >= scores['100'][grade_index]:
        return '优秀'
    elif lung_capacity >= scores['95'][grade_index]:
        return '优秀'
    elif lung_capacity >= scores['90'][grade_index]:
        return '优秀'
    elif lung_capacity >= scores['85'][grade_index]:
        return '良好'
    elif lung_capacity >= scores['80'][grade_index]:
        return '良好'
    elif lung_capacity >= scores['78'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['76'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['74'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['72'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['70'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['68'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['66'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['64'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['62'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['60'][grade_index]:
        return '及格'
    elif lung_capacity >= scores['50'][grade_index]:
        return '不及格'
    elif lung_capacity >= scores['40'][grade_index]:
        return '不及格'
    elif lung_capacity >= scores['30'][grade_index]:
        return '不及格'
    elif lung_capacity >= scores['20'][grade_index]:
        return '不及格'
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

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.2.xlsx'
df = pd.read_excel(file_path)

# 将'50米跑成绩'列转换为浮点数
df['50米跑'] = pd.to_numeric(df['50米跑'], errors='coerce')

# 男生50米跑单项评分表
male_scores = {
    '100': [7.1, 7.0, 6.8],
    '95': [7.2, 7.1, 6.9],
    '90': [7.3, 7.2, 7.0],
    '85': [7.4, 7.3, 7.1],
    '80': [7.5, 7.4, 7.2],
    '78': [7.7, 7.6, 7.4],
    '76': [7.9, 7.8, 7.6],
    '74': [8.1, 8.0, 7.8],
    '72': [8.3, 8.2, 8.0],
    '70': [8.5, 8.4, 8.2],
    '68': [8.7, 8.6, 8.4],
    '66': [8.9, 8.8, 8.6],
    '64': [9.1, 9.0, 8.8],
    '62': [9.3, 9.2, 9.0],
    '60': [9.5, 9.4, 9.2],
    '50': [9.7, 9.6, 9.4],
}

# 女生50米跑单项评分表
female_scores = {
    '100': [7.8, 7.7, 7.6],
    '95': [7.9, 7.8, 7.7],
    '90': [8.0, 7.9, 7.8],
    '85': [8.3, 8.2, 8.1],
    '80': [8.6, 8.5, 8.4],
    '78': [8.8, 8.7, 8.6],
    '76': [9.0, 8.9, 8.8],
    '74': [9.2, 9.1, 9.0],
    '72': [9.4, 9.3, 9.2],
    '70': [9.6, 9.5, 9.4],
    '68': [9.8, 9.7, 9.6],
    '66': [10.0, 9.9, 9.8],
    '64': [10.2, 10.1, 10.0],
    '62': [10.4, 10.3, 10.2],
    '60': [10.6, 10.5, 10.4],
    '50': [10.8, 10.7, 10.6],
}

def calculate_running_score(gender, running_time, grade):
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

    # 根据50米跑成绩找到对应的评分
    if running_time <= scores['90'][grade_index]:
        return '优秀'
    elif running_time <= scores['80'][grade_index]:
        return '良好'
    elif running_time <= scores['60'][grade_index]:
        return '及格'
    elif running_time >= 10:
        return '不及格'
    else:
        return None  # 小于10输出空值

# 计算50米跑成绩评分并创建一个新列
df['50米跑成绩'] = df.apply(lambda row: calculate_running_score(row['性别'], row['50米跑'], row['班级名称']), axis=1)

# 找到'50米跑成绩'列的索引位置
index_of_running = df.columns.get_loc('50米跑')

# 在'50米跑成绩'列后面插入'50米跑成绩评分'列
# 注意：这里我们假设'50米跑成绩评分'列已经存在于df中，只是需要移动位置
df.insert(index_of_running + 1, '50米跑成绩', df.pop('50米跑成绩'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.3.xlsx'
df.to_excel(output_file_path, index=False)

print(f'50米跑单项评分已添加到新的Excel文件：{output_file_path}')

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.3.xlsx'
df = pd.read_excel(file_path)

# 将'立定跳远成绩'列转换为浮点数
df['立定跳远'] = pd.to_numeric(df['立定跳远'], errors='coerce')

# 男生立定跳远单项评分表
male_scores = {
    '100': [260, 265, 270],
    '95': [255, 260, 265],
    '90': [250, 255, 260],
    '85': [243, 248, 253],
    '80': [235, 240, 245],
    '78': [231, 236, 241],
    '76': [227, 232, 237],
    '74': [223, 228, 233],
    '72': [219, 224, 229],
    '70': [215, 220, 225],
    '68': [211, 216, 221],
    '66': [207, 212, 217],
    '64': [203, 208, 213],
    '62': [199, 204, 209],
    '60': [195, 200, 205],
    '50': [190, 195, 200],
    '40': [185, 190, 195],
    '30': [180, 185, 190],
    '20': [175, 180, 185],
    '10': [170, 175, 180],
}

# 女生立定跳远单项评分表
female_scores = {
    '100': [204, 205, 206],
    '95': [198, 199, 200],
    '90': [192, 193, 194],
    '85': [185, 186, 187],
    '80': [178, 179, 180],
    '78': [175, 176, 177],
    '76': [172, 173, 174],
    '74': [169, 170, 171],
    '72': [166, 167, 168],
    '70': [163, 164, 165],
    '68': [160, 161, 162],
    '66': [157, 158, 159],
    '64': [154, 155, 156],
    '62': [151, 152, 153],
    '60': [148, 149, 150],
    '50': [143, 144, 145],
    '40': [138, 139, 140],
    '30': [133, 134, 135],
    '20': [128, 129, 130],
    '10': [123, 124, 125],
}

def calculate_jump_score(gender, jump_distance, grade):
    if gender == 1:  # 男性
        scores = male_scores
    elif gender == 2:  # 女性
        scores = female_scores
    else:
        return None  # 性别不识别

    # 根据年级选择对应的立定跳远单项评分
    if '高一' in grade or '2024' in grade:
        grade_index = 0
    elif '高二' in grade or '2023' in grade:
        grade_index = 1
    elif '高三' in grade or '2022' in grade:
        grade_index = 2
    else:
        return None  # 年级不识别

    # 根据跳远成绩找到对应的评分
    if jump_distance >= scores['100'][grade_index]:
        return '优秀'
    elif jump_distance >= scores['95'][grade_index]:
        return '优秀'
    elif jump_distance >= scores['90'][grade_index]:
        return '优秀'
    elif jump_distance >= scores['85'][grade_index]:
        return '良好'
    elif jump_distance >= scores['80'][grade_index]:
        return '良好'
    elif jump_distance >= scores['78'][grade_index]:
        return '良好'
    elif jump_distance >= scores['76'][grade_index]:
        return '良好'
    elif jump_distance >= scores['74'][grade_index]:
        return '良好'
    elif jump_distance >= scores['72'][grade_index]:
        return '良好'
    elif jump_distance >= scores['70'][grade_index]:
        return '良好'
    elif jump_distance >= scores['68'][grade_index]:
        return '良好'
    elif jump_distance >= scores['66'][grade_index]:
        return '良好'
    elif jump_distance >= scores['64'][grade_index]:
        return '良好'
    elif jump_distance >= scores['62'][grade_index]:
        return '良好'
    elif jump_distance >= scores['60'][grade_index]:
        return '良好'
    elif jump_distance >= scores['50'][grade_index]:
        return '不及格'
    elif jump_distance >= scores['40'][grade_index]:
        return '不及格'
    elif jump_distance >= scores['30'][grade_index]:
        return '不及格'
    elif jump_distance >= scores['20'][grade_index]:
        return '不及格'
    elif jump_distance >= scores['10'][grade_index]:
        return '不及格'
    else:
        return '不及格'  # 成绩小于10分

# 计算立定跳远成绩评分并创建一个新列
df['立定跳远成绩'] = df.apply(lambda row: calculate_jump_score(row['性别'], row['立定跳远'], row['班级名称']), axis=1)

# 找到'立定跳远'列的索引位置
index_of_jump = df.columns.get_loc('立定跳远')

# 确保索引位置在有效范围内
if index_of_jump < len(df.columns) - 1:
    # 在'立定跳远'列后面插入'立定跳远成绩'列
    df.insert(index_of_jump + 1, '立定跳远成绩', df.pop('立定跳远成绩'))
else:
    # 如果'立定跳远'是最后一列，则直接赋值
    df['立定跳远成绩'] = df.pop('立定跳远成绩')

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.4.xlsx'
df.to_excel(output_file_path, index=False)

print(f'立定跳远单项已添加到新的Excel文件：{output_file_path}')

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.4.xlsx'
df = pd.read_excel(file_path)

# 将'坐位体前屈成绩'列转换为浮点数
df['坐位体前屈'] = pd.to_numeric(df['坐位体前屈'], errors='coerce')

# 男生坐位体前屈单项评分表
male_sit_and_reach_scores = {
    '100': [23.6, 24.3, 24.6],
    '95': [21.5, 22.4, 22.8],
    '90': [19.4, 20.5, 21.0],
    '85': [17.2, 18.3, 19.1],
    '80': [15.0, 16.1, 17.2],
    '78': [13.6, 14.7, 15.8],
    '76': [12.2, 13.3, 14.4],
    '74': [10.8, 11.9, 13.0],
    '72': [9.4, 10.5, 11.6],
    '70': [8.0, 9.1, 10.2],
    '68': [6.6, 7.7, 8.8],
    '66': [5.2, 6.3, 7.4],
    '64': [3.8, 4.9, 6.0],
    '62': [2.4, 3.5, 4.6],
    '60': [1.0, 2.1, 3.2],
    '50': [0.0, 1.1, 2.2],
    '40': [-1.0, 0.1, 1.2],
    '30': [-2.0, -0.9, 0.2],
    '20': [-3.0, -1.9, -0.8],
    '10': [-4.0, -2.9, -1.8],
}

# 女生坐位体前屈单项评分表
female_sit_and_reach_scores = {
    '100': [24.2, 24.8, 25.3],
    '95': [22.5, 23.1, 23.6],
    '90': [20.8, 21.4, 21.9],
    '85': [19.1, 19.7, 20.2],
    '80': [17.4, 18.0, 18.5],
    '78': [16.1, 16.7, 17.2],
    '76': [14.8, 15.4, 15.9],
    '74': [13.5, 14.1, 14.6],
    '72': [12.2, 12.8, 13.3],
    '70': [10.9, 11.5, 12.0],
    '68': [9.6, 10.2, 10.7],
    '66': [8.3, 8.9, 9.4],
    '64': [7.0, 7.6, 8.1],
    '62': [5.7, 6.3, 6.8],
    '60': [4.4, 5.0, 5.5],
    '50': [3.6, 4.2, 4.7],
    '40': [2.8, 3.4, 3.9],
    '30': [2.0, 2.6, 3.1],
    '20': [1.2, 1.8, 2.3],
    '10': [0.4, 1.0, 1.5],
}

def calculate_sit_and_reach_score(gender, sit_and_reach_distance, grade):
    if gender == 1:  # 男性
        scores = male_sit_and_reach_scores
    elif gender == 2:  # 女性
        scores = female_sit_and_reach_scores
    else:
        return None  # 性别不识别

    # 根据年级选择对应的坐位体前屈单项评分
    if '高一' in grade or '2024' in grade:
        grade_index = 0
    elif '高二' in grade or '2023' in grade:
        grade_index = 1
    elif '高三' in grade or '2022' in grade:
        grade_index = 2
    else:
        return None  # 年级不识别

    # 根据坐位体前屈成绩找到对应的评分
    if sit_and_reach_distance >= scores['100'][grade_index]:
        return '优秀'
    elif sit_and_reach_distance >= scores['95'][grade_index]:
        return '优秀'
    elif sit_and_reach_distance >= scores['90'][grade_index]:
        return '优秀'
    elif sit_and_reach_distance >= scores['85'][grade_index]:
        return '良好'
    elif sit_and_reach_distance >= scores['80'][grade_index]:
        return '良好'
    elif sit_and_reach_distance >= scores['78'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['76'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['74'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['72'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['70'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['68'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['66'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['64'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['62'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['60'][grade_index]:
        return '及格'
    elif sit_and_reach_distance >= scores['50'][grade_index]:
        return '不及格'
    elif sit_and_reach_distance >= scores['40'][grade_index]:
        return '不及格'
    elif sit_and_reach_distance >= scores['30'][grade_index]:
        return '不及格'
    elif sit_and_reach_distance >= scores['20'][grade_index]:
        return '不及格'
    elif sit_and_reach_distance >= scores['10'][grade_index]:
        return '不及格'
    else:
        return None  # 小于10输出空值
# 计算坐位体前屈成绩评分并创建一个新列
df['坐位体前屈成绩'] = df.apply(lambda row: calculate_sit_and_reach_score(row['性别'], row['坐位体前屈'], row['班级名称']), axis=1)

# 找到'坐位体前屈'列的索引位置
index_of_sit_and_reach = df.columns.get_loc('坐位体前屈')

# 确保索引位置在有效范围内
if index_of_sit_and_reach < len(df.columns) - 1:
    # 在'坐位体前屈'列后面插入'坐位体前屈成绩'列
    df.insert(index_of_sit_and_reach + 1, '坐位体前屈成绩', df.pop('坐位体前屈成绩'))
else:
    # 如果'坐位体前屈'是最后一列，则直接赋值
    df['坐位体前屈成绩'] = df.pop('坐位体前屈成绩')

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.5.xlsx'
df.to_excel(output_file_path, index=False)

print(f'坐位体前屈单项已添加到新的Excel文件：{output_file_path}')

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.5.xlsx'
df = pd.read_excel(file_path)

# 将'长跑成绩'列转换为整数（秒）
def convert_time_to_seconds(time_str):
    """将时间字符串转换为秒"""
    if pd.isna(time_str) or time_str == '/':
        return None
    try:
        # 分割分钟和秒，这里假设时间格式为 '3’30' 或 '3'30'
        minutes, seconds = map(int, str(time_str).replace('’', "'").replace('"', "'").split("'"))
        # 计算总秒数
        total_seconds = minutes * 60 + seconds
        return total_seconds
    except ValueError:
        # 如果转换失败，返回None
        return None

# 男生1000米单项表
male_run_time = {
    '100': [210, 205, 200],
    '95': [215, 210, 205],
    '90': [220, 215, 210],
    '85': [227, 222, 217],
    '80': [235, 230, 225],
    '78': [240, 235, 230],
    '76': [245, 240, 235],
    '74': [250, 245, 240],
    '72': [255, 250, 245],
    '70': [260, 255, 250],
    '68': [265, 260, 255],
    '66': [270, 265, 260],
    '64': [275, 270, 265],
    '62': [280, 275, 270],
    '60': [285, 280, 275],
    '50': [305, 300, 295],
    '40': [325, 320, 315],
    '30': [345, 340, 335],
    '20': [365, 360, 355],
    '10': [385, 380, 375],
}

# 女生800米单项表
female_run_time = {
    '100': [202, 198, 194],
    '95': [208, 204, 200],
    '90': [216, 212, 208],
    '85': [223, 219, 215],
    '80': [230, 226, 222],
    '78': [235, 231, 227],
    '76': [240, 236, 232],
    '74': [245, 241, 237],
    '72': [250, 246, 242],
    '70': [255, 251, 247],
    '68': [260, 256, 252],
    '66': [265, 261, 257],
    '64': [270, 266, 262],
    '62': [275, 271, 267],
    '60': [280, 276, 272],
    '50': [290, 286, 282],
    '40': [300, 296, 292],
    '30': [310, 306, 302],
    '20': [320, 316, 312],
    '10': [330, 326, 322],
}


def calculate_run_score(gender, run_time, grade):
    if gender == 1:  # 男性
        scores = male_run_time
    elif gender == 2:  # 女性
        scores = female_run_time
    else:
        return None  # 性别不识别

    grade_index = 0  # 默认高一
    if '高二' in grade:
        grade_index = 1
    elif '高三' in grade:
        grade_index = 2

    run_time_seconds = convert_time_to_seconds(run_time)
    if run_time_seconds is None:
        return None  # 如果时间格式不正确，返回None

     # 根据长成绩找到对应的
    if run_time_seconds <= scores['100'][grade_index]:
        return '优秀'
    elif run_time_seconds <= scores['95'][grade_index]:
        return '优秀'
    elif run_time_seconds <= scores['90'][grade_index]:
        return '优秀'
    elif run_time_seconds <= scores['85'][grade_index]:
        return '良好'
    elif run_time_seconds <= scores['80'][grade_index]:
        return '良好'
    elif run_time_seconds <= scores['78'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['76'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['74'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['72'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['70'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['68'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['66'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['64'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['62'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['60'][grade_index]:
        return '及格'
    elif run_time_seconds <= scores['50'][grade_index]:
        return '不及格'
    elif run_time_seconds <= scores['40'][grade_index]:
        return '不及格'
    elif run_time_seconds <= scores['30'][grade_index]:
        return '不及格'
    elif run_time_seconds <= scores['20'][grade_index]:
        return '不及格'
    elif run_time_seconds <= scores['10'][grade_index]:
        return '不及格'
    else:
        return None  # 小于10输出空值

# 应用函数计算男生1000米和女生800米成绩
df['1000米跑成绩评分'] = df.apply(lambda row: calculate_run_score(row['性别'], row['1000米跑'], row['班级名称']), axis=1)
df['800米跑成绩评分'] = df.apply(lambda row: calculate_run_score(row['性别'], row['800米跑'], row['班级名称']), axis=1)

# 找到'1000米跑'列的索引位置
index_of_1000m_run = df.columns.get_loc('1000米跑')

# 确保索引位置在有效范围内
if index_of_1000m_run < len(df.columns) - 1:
    # 在'1000米跑'列后面插入'1000米跑成绩评分'列
    df.insert(index_of_1000m_run + 1, '1000米跑成绩评分', df.pop('1000米跑成绩评分'))
else:
    # 如果'1000米跑'是最后一列，则直接赋值
    df['1000米跑成绩评分'] = df.pop('1000米跑成绩评分')

# 找到'800米跑'列的索引位置
index_of_800m_run = df.columns.get_loc('800米跑')

# 确保索引位置在有效范围内
if index_of_800m_run < len(df.columns) - 1:
    # 在'800米跑'列后面插入'800米跑成绩评分'列
    df.insert(index_of_800m_run + 1, '800米跑成绩评分', df.pop('800米跑成绩评分'))
else:
    # 如果'800米跑'是最后一列，则直接赋值
    df['800米跑成绩评分'] = df.pop('800米跑成绩评分')

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.6.xlsx'
df.to_excel(output_file_path, index=False)

print(f'长跑单项评分已添加到新的Excel文件：{output_file_path}')

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.6.xlsx'
df = pd.read_excel(file_path)

# 清理数据，将非数值的字符替换为NaN，然后转换为整数
df.replace('/', pd.NA, inplace=True)
df['引体向上'] = pd.to_numeric(df['引体向上'], errors='coerce')
df['一分钟仰卧起坐'] = pd.to_numeric(df['一分钟仰卧起坐'], errors='coerce')

# 填充NaN值，例如用0或某个特定的值填充
df['引体向上'].fillna(0, inplace=True)
df['一分钟仰卧起坐'].fillna(0, inplace=True)

# 将填充后的列转换为整数
df['引体向上'] = df['引体向上'].astype(int)
df['一分钟仰卧起坐'] = df['一分钟仰卧起坐'].astype(int)

# 男生引体向上单项表
male_pull_up = {
    '100': [16, 17, 18],
    '95': [15, 16, 17],
    '90': [14, 15, 16],
    '85': [13, 14, 15],
    '80': [12, 13, 14],
    '78': [12, 13, 14],
    '76': [11, 12, 13],
    '74': [11, 12, 13],
    '72': [10, 11, 12],
    '70': [10, 11, 12],
    '68': [9, 10, 11],
    '66': [9, 10, 11],
    '64': [8, 9, 10],
    '62': [8, 9, 10],
    '60': [7, 8, 9],
    '50': [6, 7, 8],
    '40': [5, 6, 7],
    '30': [4, 5, 6],
    '20': [3, 4, 5],
    '10': [2, 3, 4],
}

# 女生一分钟仰卧起坐单项表
female_sit_up = {
    '100': [53, 54, 55],
    '95': [51, 52, 53],
    '90': [49, 50, 51],
    '85': [46, 47, 48],
    '80': [43, 44, 45],
    '78': [41, 42, 43],
    '76': [39, 40, 41],
    '74': [37, 38, 39],
    '72': [35, 36, 37],
    '70': [33, 34, 35],
    '68': [31, 32, 33],
    '66': [29, 30, 31],
    '64': [27, 28, 29],
    '62': [25, 26, 27],
    '60': [23, 24, 25],
    '50': [21, 22, 23],
    '40': [19, 20, 21],
    '30': [17, 18, 19],
    '20': [15, 16, 17],
    '10': [13, 14, 15],
}

def calculate_pull_up_score(gender, pull_up_count, grade):
    if gender == 1:  # 男性
        scores = male_pull_up
    elif gender == 2:  # 女性
        scores = female_sit_up
    else:
        return None  # 性别不识别

    grade_index = 0  # 默认高一
    if '高二' in grade:
        grade_index = 1
    elif '高三' in grade:
        grade_index = 2

    # 根据引体向上或一分钟仰卧起坐次数找到对应的等级
    if pull_up_count >= scores['100'][grade_index]:
        return '优秀'
    elif pull_up_count >= scores['95'][grade_index]:
        return '优秀'
    elif pull_up_count >= scores['90'][grade_index]:
        return '优秀'
    elif pull_up_count >= scores['85'][grade_index]:
        return '良好'
    elif pull_up_count >= scores['80'][grade_index]:
        return '良好'
    elif pull_up_count >= scores['78'][grade_index]:
        return '及格' 
    elif pull_up_count >= scores['76'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['74'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['72'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['70'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['68'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['66'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['64'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['62'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['60'][grade_index]:
        return '及格'
    elif pull_up_count >= scores['50'][grade_index]:
        return '不及格'
    elif pull_up_count >= scores['40'][grade_index]:
        return '不及格'
    elif pull_up_count >= scores['30'][grade_index]:
        return '不及格'
    elif pull_up_count >= scores['20'][grade_index]:
        return '不及格'
    elif pull_up_count >= scores['10'][grade_index]:
        return '不及格'
    else:
        return None  # 小于10输出空值

# 应用函数计算男生引体向上和女生一分钟仰卧起坐成绩
df['引体向上成绩'] = df.apply(lambda row: calculate_pull_up_score(row['性别'], row['引体向上'], row['班级名称']), axis=1)
df['一分钟仰卧起坐成绩'] = df.apply(lambda row: calculate_pull_up_score(row['性别'], row['一分钟仰卧起坐'], row['班级名称']), axis=1)

# 将NaN值替换回'/'
df.replace({0: '/', pd.NA: '/'}, inplace=True)

# 找到'引体向上'列的索引位置
index_of_pull_up = df.columns.get_loc('引体向上')

# 确保索引位置在有效范围内
if index_of_pull_up < len(df.columns) - 1:
    # 在'引体向上'列后面插入'引体向上成绩'列
    df.insert(index_of_pull_up + 1, '引体向上成绩', df.pop('引体向上成绩'))
else:
    # 如果'引体向上'是最后一列，则直接赋值
    df['引体向上成绩'] = df.pop('引体向上成绩')

# 找到'一分钟仰卧起坐'列的索引位置
index_of_sit_up = df.columns.get_loc('一分钟仰卧起坐')

# 确保索引位置在有效范围内
if index_of_sit_up < len(df.columns) - 1:
    # 在'一分钟仰卧起坐'列后面插入'一分钟仰卧起坐成绩'列
    df.insert(index_of_sit_up + 1, '一分钟仰卧起坐成绩', df.pop('一分钟仰卧起坐成绩'))
else:
    # 如果'一分钟仰卧起坐'是最后一列，则直接赋值
    df['一分钟仰卧起坐成绩'] = df.pop('一分钟仰卧起坐成绩')

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.7.xlsx'
df.to_excel(output_file_path, index=False)

print(f'引体向上和一分钟仰卧起坐单项已添加到新的Excel文件：{output_file_path}')