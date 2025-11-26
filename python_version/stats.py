import pandas as pd

df = pd.read_csv('../data/sample_5000.csv', encoding='utf-8')
df['总分'] = df[['语文','数学','英语','物理','化学','生物']].sum(axis=1)

print("📊 成绩统计报告")
print("=" * 30)
print(f"总人数：{len(df)}人")
print(f"平均总分：{df['总分'].mean():.2f}分")
print(f"最高分：{df['总分'].max()}分")
print(f"最低分：{df['总分'].min()}分")
print(f"及格率：{(df['总分'] >= 360).mean()*100:.2f}%")
print("\n各科不及格人数：")
print((df[['语文','数学','英语','物理','化学','生物']] < 60).sum())