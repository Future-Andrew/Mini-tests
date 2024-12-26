import pandas as pd

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