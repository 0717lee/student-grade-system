# 学生成绩管理系统 v1.0 ✅

## 项目状态：已完成（2025-01-01）

## 🚀 三种使用方式

### 1️⃣ Flask API（后端接口）
```bash
cd python_version
python app.py
# 访问 http://127.0.0.1:5000/api/stats

### 2️⃣ Streamlit界面（可视化）
```bash
cd python_version
streamlit run dashboard.py --server.port=5001

### 3️⃣ 数据分析脚本
```bash
python stats.py
python stat_db.py

基于C语言+MySQL的学生成绩管理系统

## API文档

### 1. 获取学生列表
**GET** `/api/students?page=1&per_page=20`
git add README.md
### 2. 获取统计信息
**GET** `/api/stats`

### 3. 运行统计脚本
```bash
python python_version/stats.py

## 性能指标
- 查询响应：<100ms
- 支持数据量：5000条
- 内存占用：<50MB

## 项目结构
├── data/
├── python_version/
│   ├── app.py
│   └── stats.py
├── src/
└── sql/