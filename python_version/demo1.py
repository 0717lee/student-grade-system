import csv

def read_and_calculate(filename):
    """读取CSV并计算总分"""
    students = []
    with open('../data/sample_5000.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 计算6科总分
            scores = [int(row['语文']), int(row['数学']), int(row['英语']), 
          int(row['物理']), int(row['化学']), int(row['生物'])]
            row['总分'] = sum(scores)
            students.append(row)
    return students

# 测试
data = read_and_calculate('../data/sample_5000.csv')
print(f"✅ 读取成功！共{len(data)}条记录")
print(f"第一条：{data[0]['姓名']}，总分：{data[0]['总分']}")