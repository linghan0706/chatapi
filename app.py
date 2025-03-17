from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用CORS以允许前端调用

# 灵易万物API的基础URL
API_BASE = "https://api.lingyiwanwu.com/v1"
# API密钥
API_KEY = "bf1973e0425c45559fd319f217d12a22"

@app.route('/api/chat/completions', methods=['POST'])
def chat_completions():
    """代理灵易万物的聊天完成接口"""
    try:
        # 从请求中获取数据
        data = request.json
        
        # 准备请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        
        # 转发请求到灵易万物API
        response = requests.post(
            f"{API_BASE}/chat/completions",
            json=data,
            headers=headers
        )
        
        # 返回API响应
        return jsonify(response.json()), response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/models', methods=['GET'])
def list_models():
    """代理灵易万物的模型列表接口"""
    try:
        # 准备请求头
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }
        
        # 转发请求到灵易万物API
        response = requests.get(
            f"{API_BASE}/models",
            headers=headers
        )
        
        # 返回API响应
        return jsonify(response.json()), response.status_code
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()