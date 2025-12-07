from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# ========== 修改这里！改成你的MySQL密码 ==========
DATABASE_URL = "mysql+pymysql://root:lfm0808@localhost:3306/student_system"
# ==========================================

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# 学生表模型
class Student(Base):
    __tablename__ = "students"
    
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    chinese = Column(Integer)
    math = Column(Integer)
    english = Column(Integer)
    physics = Column(Integer)
    chemistry = Column(Integer)
    biology = Column(Integer)
    total = Column(Integer)

# 创建表
Base.metadata.create_all(engine)
print("✅ 数据库表创建成功！")