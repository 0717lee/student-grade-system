from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Flask 3.x 解决中文转义（只改这一行）
app.json.ensure_ascii = False

# 读取数据
df = pd.read_csv('../data/sample_5000.csv', encoding='utf-8')
df['总分'] = df[['语文','数学','英语','物理','化学','生物']].sum(axis=1)

@app.route('/api/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))
    start = (page-1)*per_page
    end = start + per_page
    
    result = df.iloc[start:end].to_dict('records')
    return jsonify({
        'total': len(df),
        'page': page,
        'data': result
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = {
        'avg_total': float(df['总分'].mean()),
        'max_total': int(df['总分'].max()),
        'min_total': int(df['总分'].min()),
        'fail_count': {k: int(v) for k, v in (df[['语文','数学','英语','物理','化学','生物']] < 60).sum().to_dict().items()}
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)