# student-grade-system

基于C语言+MySQL的学生成绩管理系统

## API文档

### 1. 获取学生列表
**GET** `/api/students?page=1&per_page=20`

### 2. 获取统计信息
**GET** `/api/stats`

### 3. 运行统计脚本
```bash
python python_version/stats.py