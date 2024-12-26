import pandas as pd

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

    # 根据年级选择对应的50米跑单项评分
    if '高一' in grade:
        grade_index = 0
    elif '高二' in grade:
        grade_index = 1
    elif '高三' in grade:
        grade_index = 2
    else:
        return None  # 年级不识别

    # 根据50米跑成绩找到对应的评分
    for key, value in scores.items():
        if running_time <= value[grade_index]:
            return key
    return None  # 如果成绩不在任何等级内，返回None

# 计算50米跑成绩评分并创建一个新列
df['50米跑评分'] = df.apply(lambda row: calculate_running_score(row['性别'], row['50米跑'], row['班级名称']), axis=1)

# 找到'50米跑成绩'列的索引位置
index_of_running = df.columns.get_loc('50米跑')

# 在'50米跑成绩'列后面插入'50米跑成绩评分'列
# 注意：这里我们假设'50米跑成绩评分'列已经存在于df中，只是需要移动位置
df.insert(index_of_running + 1, '50米跑评分', df.pop('50米跑评分'))

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.3.xlsx'
df.to_excel(output_file_path, index=False)

print(f'50米跑单项评分已添加到新的Excel文件：{output_file_path}')