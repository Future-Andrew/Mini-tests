import pandas as pd

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

    # 根据立定跳远成绩找到对应的评分
    for score, distances in scores.items():
        if jump_distance >= int(distances[grade_index]):
            return score
    return None  # 成绩不在任何等级内

# 计算立定跳远成绩评分并创建一个新列
df['立定跳远成绩'] = df.apply(lambda row: calculate_jump_score(row['性别'], row['立定跳远'], row['班级名称']), axis=1)

# 找到'立定跳远成绩评分'列的索引位置
index_of_jump = df.columns.get_loc('立定跳远成绩')

# 在'立定跳远成绩评分'列后面插入'立定跳远成绩评分'列
# 注意：这里我们假设'立定跳远成绩评分'列已经存在于df中，只是需要移动位置
df.insert(index_of_jump + 1, '立定跳远成绩', df.pop('立定跳远成绩'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.4.xlsx'
df.to_excel(output_file_path, index=False)

print(f'立定跳远单项评分已添加到新的Excel文件：{output_file_path}')