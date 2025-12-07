import csv
from database import SessionLocal, Student

session = SessionLocal()

with open('../data/sample_5000.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        student = Student(
            id=row['学号'],
            name=row['姓名'],
            chinese=int(row['语文']),
            math=int(row['数学']),
            english=int(row['英语']),
            physics=int(row['物理']),
            chemistry=int(row['化学']),
            biology=int(row['生物']),
            total=sum([int(row[c]) for c in ['语文','数学','英语','物理','化学','生物']])
        )
        session.add(student)
    session.commit()

session.close()
print("✅ 5000条数据导入MySQL完成！")