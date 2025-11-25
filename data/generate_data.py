import csv
import random

# 生成5000条测试数据
with open('data/sample_5000.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['学号', '姓名', '语文', '数学', '英语', '物理', '化学', '生物'])
    
    for i in range(1, 5001):
        student_id = f"2024{str(i).zfill(4)}"
        name = f"学生{i}"
        scores = [random.randint(40, 100) for _ in range(6)]
        writer.writerow([student_id, name] + scores)

print("✅ 5000条测试数据生成完成！")