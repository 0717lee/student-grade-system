import pandas as pd
from database import SessionLocal, Student

session = SessionLocal()
students = session.query(Student).all()
session.close()

df = pd.DataFrame([{
    "语文": s.chinese, "数学": s.math, "英语": s.english,
    "物理": s.physics, "化学": s.chemistry, "生物": s.biology
} for s in students])

df['总分'] = df.sum(axis=1)

print("📊 从MySQL读取的成绩统计报告")
print("=" * 30)
print(f"总人数：{len(df)}人")
print(f"平均总分：{df['总分'].mean():.2f}分")
print(f"及格率：{(df['总分']>=360).mean()*100:.2f}%")