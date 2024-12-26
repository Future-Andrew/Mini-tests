import pandas as pd

# 读取Excel文件
file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.5.xlsx'
df = pd.read_excel(file_path)

# 将'长跑成绩'列转换为整数（秒）
def convert_time_to_seconds(time_str):
    """将时间字符串转换为秒"""
    if isinstance(time_str, float) and pd.isna(time_str):  # 检查是否为NaN
        return None
    if '/' in str(time_str):
        return None
    try:
        minutes, seconds = map(int, str(time_str).replace('’', "'").replace('"', "'").split("'"))
        total_seconds = minutes * 60 + seconds
        return total_seconds
    except ValueError:
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

    if '高一' in grade or '2024' in grade:
        grade_index = 0
    elif '高二' in grade or '2023' in grade:
        grade_index = 1
    elif '高三' in grade or '2022' in grade:
        grade_index = 2
    else:
        return None  # 年级不识别

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
df['1000米跑成绩评分'] = df.apply(lambda row: calculate_run_score(row['性别'], row['1000米跑'], row['班级名称']) if row['1000米跑'] != '/' else None, axis=1)
df['800米跑成绩评分'] = df.apply(lambda row: calculate_run_score(row['性别'], row['800米跑'], row['班级名称']) if row['800米跑'] != '/' else None, axis=1)

# 保存新的Excel文件
output_file_path = 'C:\\Users\\andre\\Desktop\\excel\\学校\\测试用表\\1.6.xlsx'
df.to_excel(output_file_path, index=False)

print(f'长跑单项评分已添加到新的Excel文件：{output_file_path}')