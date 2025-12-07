# 学生成绩管理系统 v1.0 

## 项目状态：已完成

---

## 🚀 三种使用方式

### 1️⃣ Flask API（后端接口）
```bash
cd python_version
python app.py
# 访问 http://127.0.0.1:5000/api/stats
```

### 2️⃣ Streamlit界面（可视化）
```bash
cd python_version
streamlit run dashboard.py --server.port=5001
# 访问 http://localhost:5001
```

### 3️⃣ 数据分析脚本
```bash
# 从CSV读取分析
python stats.py

# 从MySQL读取分析
python stats_db.py
```

---

## 📦 技术栈

| 模块 | 技术 | 说明 |
|------|------|------|
| **后端** | Flask 3.1.2 | RESTful API，响应时间<100ms |
| **数据库** | MySQL 8.0 + SQLAlchemy 2.0 | 5000条数据持久化存储 |
| **数据分析** | Pandas 2.3.3 | 统计报表、及格率计算 |
| **可视化** | Streamlit 1.30.0 | 交互式Web界面，支持数据下载 |
| **版本控制** | Git | 10+次提交，Conventional Commits规范 |

---

## 📊 性能指标

- **查询响应**：<100ms（Flask API）
- **数据规模**：5000条学生记录（可扩展至10万条）
- **内存占用**：<50MB（Pandas处理）
- **并发支持**：10 QPS（Flask开发服务器）

---

## 📁 项目结构

```
student-grade-system/
├── data/                          # 数据集
│   ├── generate_data.py          # 生成5000条测试数据
│   └── sample_5000.csv           # CSV数据文件
├── python_version/                # Python重构版本
│   ├── app.py                    # Flask API服务端
│   ├── dashboard.py              # Streamlit可视化界面
│   ├── database.py               # SQLAlchemy数据库连接
│   ├── import_data.py            # 导入CSV到MySQL
│   ├── stats.py                  # CSV数据分析脚本
│   └── stats_db.py               # MySQL数据分析脚本
├── src/                           # C语言原始版本
│   └── main.c                    # 核心框架代码
├── sql/                           # 数据库脚本
│   └── schema.sql                # 表结构定义
└── README.md                     # 项目文档
```

---

## 🎯 v1.0 已完成功能

### ✅ 数据库模块
- [x] SQLAlchemy ORM集成
- [x] MySQL表结构创建（students表）
- [x] CSV数据导入（5000条）
- [x] 从MySQL读取数据

### ✅ API模块
- [x] `/api/stats` 统计接口（平均总分、最高分、不及格）
- [x] `/api/students` 查询接口（支持分页）
- [x] JSON中文正常显示（无转义）

### ✅ 可视化模块
- [x] Streamlit统计卡片（4个核心指标）
- [x] 各科不及格率柱状图
- [x] 完整数据表格展示
- [x] CSV下载功能

---

## 🚀 快速开始（完整流程）

### 第1步：创建MySQL数据库
```bash
mysql -u root -p
# 输入密码
CREATE DATABASE student_system DEFAULT CHARACTER SET utf8mb4;
exit
```

### 第2步：导入数据
```bash
cd python_version
python database.py          # 创建表
python import_data.py       # 导入5000条数据
```

### 第3步：启动Streamlit界面
```bash
streamlit run dashboard.py --server.port=5001
# 访问 http://localhost:5001
```

### 第4步：启动Flask API（可选）
```bash
python app.py
# 访问 http://127.0.0.1:5000/api/stats
```

