import pandas as pd

# 读取Excel文件
file_path = '测试.xlsx'
df = pd.read_excel(file_path)

# 定义计算器类
class HealthScoreCalculator:
    def __init__(self, gender, scores):
        self.gender = gender
        self.scores = scores
        self.weights = {
            'BMI': 15, '肺活量': 15, '50米跑': 20, '坐位体前屈': 10, '立定跳远': 10
        }
        if gender == '男':
            self.weights['引体向上'] = 10
            self.weights['1000米跑'] = 20
        else:
            self.weights['1分钟仰卧起坐'] = 10
            self.weights['800米跑'] = 20

    def calculate_standard_score(self):
        standard_score = 0
        for item, score in self.scores.items():
            if item in self.weights:
                standard_score += score * (self.weights[item] / 100)
        return standard_score

    def calculate_bonus_score(self):
        bonus_score = 0
        if self.gender == '男':
            bonus_item = '引体向上' if '引体向上' in self.scores else '1000米跑'
        else:
            bonus_item = '1分钟仰卧起坐' if '1分钟仰卧起坐' in self.scores else '800米跑'
        
        if bonus_item in self.scores and self.scores[bonus_item] > 100:
            bonus_score = min(self.scores[bonus_item] - 100, 10)
        return bonus_score

    def calculate_total_score(self):
        return self.calculate_standard_score() + self.calculate_bonus_score()

    def grade(self):
        total_score = self.calculate_total_score()
        if total_score >= 90:
            return '优秀'
        elif total_score >= 80:
            return '良好'
        elif total_score >= 60:
            return '及格'
        else:
            return '不及格'

# 处理数据
results = []
for index, row in df.iterrows():
    if row['年级编号'] == 31 and row['班级编号'] in [11, 14, 202401]:  # 高一级1班、4班和2024级01班
        scores = {
            'BMI': row['体重'] / (row['身高'] / 100) ** 2,
            '肺活量': row['肺活量'],
            '50米跑': row['50米跑'],
            '坐位体前屈': row['坐位体前屈'],
            '立定跳远': row['立定跳远']
        }
        if row['性别'] == 1:  # 男
            scores['引体向上'] = row['引体向上']
            scores['1000米跑'] = row['1000米跑'] / 240  # 将时间转换为秒
        else:  # 女
            scores['1分钟仰卧起坐'] = row['一分钟仰卧起坐']
            scores['800米跑'] = row['800米跑'] / 240  # 将时间转换为秒

        calculator = HealthScoreCalculator(row['性别'], scores)
        total_score = calculator.calculate_total_score()
        grade = calculator.grade()
        results.append({
            '学籍号': row['学籍号'],
            '姓名': row['姓名'],
            '性别': row['性别'],
            '总得分': total_score,
            '等级': grade
        })

# 输出结果
    output_file_path = fr'C:\Users\王国聪\Desktop\广州市贸易职业高级中学体测模版(合).xlsx'
    df.to_excel(output_file_path, index=False)
    print=("完成", f"数据已成功更新并保存到 {output_file_path}")