import pandas as pd
import os

def get_current_username():
    return os.getlogin()

current_username = get_current_username()
print(f"Current User: {current_username}")


# 读取两个Excel文件
# 使用.format()方法替换current_username变量
file1_path = r'C:\Users\{0}\Desktop\广州市贸易职业高级中学体测模版.xlsx'.format(current_username)
file2_path = r'C:\Users\{0}\Desktop\广州贸易职业技术学校测试数据(2)_new.xlsx'.format(current_username)  # 修正了文件名
file3_path = r'C:\Users\{0}\Desktop\广州贸易职业技术学校测试数据(2)(修改版)_Formatted.xlsx'.format(current_username)


# 接下来你可以使用pandas来读取这些Excel文件
# 例如：
df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)
try:
    # 读取第一个Excel文件
    df1 = pd.read_excel(file1_path)
    print("成功读取工作簿1")
except Exception as e:
    print(f"读取工作簿1时出错: {e}")

try:
    # 读取第二个Excel文件
    df2 = pd.read_excel(file2_path)
    print("成功读取工作簿2")
except Exception as e:
    print(f"读取工作簿2时出错: {e}")
    
try:
    # 读取第二个Excel文件
    df3 = pd.read_excel(file3_path)
    print("成功读取工作簿3")
except Exception as e:
    print(f"读取工作簿2时出错: {e}")

# 创建一个字典来存储学籍号与体育成绩的映射
scores_map = {}

# 遍历第三个文件，提取学籍号和成绩
for index, row in df3.iterrows():
    student_id = row['证件号码']  # 假设这里是学籍号
    scores_map[student_id] = {
        '肺活量': row['肺活量成绩'],
        '坐位体前屈': row['坐位体前屈成绩'],
        '立定跳远': row['立定跳远成绩'],
        '50米跑': row['50米跑成绩'],
        '1000米跑': row['1000米跑成绩'],
        '身高': row['身高成绩'],
        '体重': row['体重成绩'],
        '800米跑': row['800米跑成绩'],
        '一分钟仰卧起坐': row['仰卧起坐成绩'],
        '引体向上': row['引体向上成绩'],
    }

for index, row in df1.iterrows():
    student_id = row['学籍号']  # 假设这里是学籍号
    if student_id in scores_map:
        df1.at[index, '肺活量'] = scores_map[student_id]['肺活量']
        df1.at[index, '坐位体前屈'] = scores_map[student_id]['坐位体前屈']
        df1.at[index, '立定跳远'] = scores_map[student_id]['立定跳远']
        df1.at[index, '50米跑'] = scores_map[student_id]['50米跑']
        df1.at[index, '1000米跑'] = scores_map[student_id]['1000米跑']
        df1.at[index, '身高'] = scores_map[student_id]['身高']
        df1.at[index, '体重'] = scores_map[student_id]['体重']
        df1.at[index, '800米跑'] = scores_map[student_id]['800米跑']
        df1.at[index, '一分钟仰卧起坐'] = scores_map[student_id]['一分钟仰卧起坐']
        df1.at[index, '引体向上'] = scores_map[student_id]['引体向上']
        
# 遍历第二个文件，提取学籍号和成绩
for index, row in df2.iterrows():
    student_id = row['证件号码']  # 假设这里是学籍号
    scores_map[student_id] = {
        '肺活量': row['肺活量成绩'],
        '坐位体前屈': row['坐位体前屈成绩'],
        '立定跳远': row['立定跳远成绩'],
        '50米跑': row['50米跑成绩'],
        '1000米跑': row['1000米跑成绩'],
        '身高': row['身高成绩'],
        '体重': row['体重成绩'],
        '800米跑': row['800米跑成绩'],
        '一分钟仰卧起坐': row['仰卧起坐成绩'],
        '引体向上': row['引体向上成绩'],
    }

# 遍历第一个文件，填充成绩
for index, row in df1.iterrows():
    student_id = row['学籍号']  # 假设这里是学籍号
    if student_id in scores_map:
        df1.at[index, '肺活量'] = scores_map[student_id]['肺活量']
        df1.at[index, '坐位体前屈'] = scores_map[student_id]['坐位体前屈']
        df1.at[index, '立定跳远'] = scores_map[student_id]['立定跳远']
        df1.at[index, '50米跑'] = scores_map[student_id]['50米跑']
        df1.at[index, '1000米跑'] = scores_map[student_id]['1000米跑']
        df1.at[index, '身高'] = scores_map[student_id]['身高']
        df1.at[index, '体重'] = scores_map[student_id]['体重']
        df1.at[index, '800米跑'] = scores_map[student_id]['800米跑']
        df1.at[index, '一分钟仰卧起坐'] = scores_map[student_id]['一分钟仰卧起坐']
        df1.at[index, '引体向上'] = scores_map[student_id]['引体向上']

# 保存更新后的数据到新的Excel文件
output_file_path = r'C:\Users\王国聪\Desktop\广州市贸易职业高级中学体测模版(合).xlsx'
df1.to_excel(output_file_path, index=False)

print(f"数据已成功更新并保存到 {output_file_path}")