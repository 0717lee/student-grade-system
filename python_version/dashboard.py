import streamlit as st
import pandas as pd
from database import SessionLocal, Student

# 页面配置
st.set_page_config(page_title="学生成绩管理系统", layout="wide")
st.title("📊 学生成绩管理系统 v1.0")

# 从MySQL读取数据
session = SessionLocal()
students = session.query(Student).all()
session.close()

df = pd.DataFrame([{
    "学号": s.id, "姓名": s.name, "语文": s.chinese, "数学": s.math,
    "英语": s.english, "物理": s.physics, "化学": s.chemistry,
    "生物": s.biology, "总分": s.total
} for s in students])

# 显示统计卡片
st.subheader("核心指标")
col1, col2, col3, col4 = st.columns(4)
col1.metric("👥 总人数", f"{len(df)}人")
col2.metric("📈 平均分", f"{df['总分'].mean():.1f}分")
col3.metric("🏆 最高分", f"{df['总分'].max()}分")
col4.metric("✅ 及格率", f"{(df['总分']>=360).mean()*100:.1f}%")

# 各科不及格率柱状图
st.subheader("各科不及格情况")
fail_counts = (df[['语文','数学','英语','物理','化学','生物']] < 60).sum()
st.bar_chart(fail_counts)

# 显示完整表格
st.subheader("成绩明细")
st.dataframe(df, use_container_width=True)

# 下载按钮
st.download_button(
    label="📥 下载成绩单(CSV)",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='学生成绩单.csv',
    mime='text/csv'
)