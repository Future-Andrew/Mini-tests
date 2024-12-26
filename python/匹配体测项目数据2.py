import pandas as pd

# 读取三个Excel文件
file1_path = r'C:\Users\王国聪\Desktop\广州市贸易职业高级中学体测模版.xls'
file2_path = r'C:\Users\王国聪\Desktop\广州贸易职业技术学校测试数据(2)+new.xlsx'
file3_path = r'C:\Users\王国聪\Desktop\111_Formatted.xlsx'

try:
    df1 = pd.read_excel(file1_path)
    print("成功读取工作簿1")
    print("工作簿1的前三个学籍号:", df1['学籍号'].head(3).tolist())
except Exception as e:
    print(f"读取工作簿1时出错: {e}")
    exit()

try:
    df2 = pd.read_excel(file2_path)
    print("成功读取工作簿2")
    print("工作簿2的前三个学籍号:", df2['证件号码'].head(3).tolist())
except Exception as e:
    print(f"读取工作簿2时出错: {e}")
    exit()

try:
    df3 = pd.read_excel(file3_path)
    print("成功读取工作簿3")
    print("工作簿3的前三个学籍号:", df3['证件号码'].head(3).tolist())
except Exception as e:
    print(f"读取工作簿3时出错: {e}")
    exit()

scores_map = {}

# 合并df2和df3的数据到scores_map
for df in [df2, df3]:
    for index, row in df.iterrows():
        student_id = row['证件号码'] 
        scores_map[student_id] = {
            '肺活量': row['肺活量成绩'],
            '坐位体前屈': row['坐位体前屈成绩'],
            '立定跳远': row['立定跳远成绩'],
            '50米跑': row['50米跑成绩'],
            '1000米跑': row['1000米跑成绩'],
            '身高': row['身高成绩'],
            '体重': row['体重成绩'],
            '800米跑': row['800米跑成绩'],
            '一分钟仰卧起坐': row['一分钟仰卧起坐'],
            '引体向上': row['引体向上'],
        }

# 填充df1
for index, row in df1.iterrows():
    student_id = row['学籍号']
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

# 检查输出文件是否有数据
try:
    combined_df = pd.read_excel(output_file_path)
    print("输出文件的前三个学籍号:", combined_df['学籍号'].head(3).tolist())
except Exception as e:
    print(f"读取输出文件时出错: {e}")