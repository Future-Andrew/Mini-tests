import pandas as pd
import numpy as np

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