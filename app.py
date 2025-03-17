from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 启用CORS以允许前端调用

# 灵易万物API的基础URL
API_BASE = "https://api.lingyiwanwu.com/v1"
# API密钥，实际应用中应该从环境变量或配置文件中获取
API_KEY = "bf1973e0425c45559fd319f217d12a22"  # 这里使用文档中提供的API密钥

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

# 提供一个简单的首页
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>灵易万物API代理</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            textarea { width: 100%; height: 100px; margin-bottom: 10px; }
            button { padding: 10px 15px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
            button:hover { background-color: #45a049; }
            pre { background-color: #f5f5f5; padding: 10px; overflow: auto; }
        </style>
    </head>
    <body>
        <h1>灵易万物API测试页面</h1>
        <h2>聊天接口测试</h2>
        <div>
            <textarea id="userInput" placeholder="输入您的问题..."></textarea>
            <button onclick="sendMessage()">发送</button>
        </div>
        <h3>响应结果：</h3>
        <pre id="response">响应将显示在这里...</pre>
        
        <h2>模型列表测试</h2>
        <button onclick="getModels()">获取模型列表</button>
        <h3>模型列表：</h3>
        <pre id="modelsList">模型列表将显示在这里...</pre>
        
        <script>
            // 发送消息到聊天接口
            async function sendMessage() {
                const userInput = document.getElementById('userInput').value;
                if (!userInput.trim()) return;
                
                document.getElementById('response').textContent = '请求中...';
                
                try {
                    const response = await axios.post('/api/chat/completions', {
                        model: "yi-lightning",
                        messages: [{role: "user", content: userInput}],
                        temperature: 0.3
                    });
                    
                    document.getElementById('response').textContent = 
                        JSON.stringify(response.data, null, 2);
                } catch (error) {
                    document.getElementById('response').textContent = 
                        `错误: ${error.message}\n${JSON.stringify(error.response?.data || {}, null, 2)}`;
                }
            }
            
            // 获取模型列表
            async function getModels() {
                document.getElementById('modelsList').textContent = '请求中...';
                
                try {
                    const response = await axios.get('/api/models');
                    document.getElementById('modelsList').textContent = 
                        JSON.stringify(response.data, null, 2);
                } catch (error) {
                    document.getElementById('modelsList').textContent = 
                        `错误: ${error.message}\n${JSON.stringify(error.response?.data || {}, null, 2)}`;
                }
            }
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)