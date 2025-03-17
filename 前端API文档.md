# 灵易万物API接口文档

## 基础信息

- 基础URL: `http://your-domain/api`
- 所有接口都支持CORS跨域请求
- 响应格式: JSON

## 接口列表

### 1. 聊天完成接口

#### 接口信息
- 请求路径：`/chat/completions`
- 请求方法：POST
- Content-Type: application/json

#### 请求参数

```javascript
{
  "model": "yi-lightning",  // 必填，模型名称
  "messages": [             // 必填，消息数组
    {
      "role": "user",      // 消息角色
      "content": "你好"    // 消息内容
    }
  ],
  "temperature": 0.3       // 可选，温度参数
}
```

#### 响应格式

```javascript
{
  "id": "cmpl-xxxxxx",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "回复内容",
        "role": "assistant"
      }
    }
  ]
}
```

#### Axios调用示例

```javascript
// 导入axios
import axios from 'axios';

// 发送聊天请求
async function sendChatMessage(message) {
  try {
    const response = await axios.post('/api/chat/completions', {
      model: "yi-lightning",
      messages: [{ role: "user", content: message }],
      temperature: 0.3
    });
    
    return response.data;
  } catch (error) {
    console.error('聊天请求失败:', error);
    throw error;
  }
}
```

### 2. 获取模型列表

#### 接口信息
- 请求路径：`/models`
- 请求方法：GET

#### 响应格式

```javascript
{
  "data": [
    {
      "id": "yi-lightning",
      "created": 1708671653,
      "object": "model",
      "owned_by": "01.ai"
    }
  ],
  "object": "list"
}
```

#### Axios调用示例

```javascript
// 导入axios
import axios from 'axios';

// 获取模型列表
async function getModelsList() {
  try {
    const response = await axios.get('/api/models');
    return response.data;
  } catch (error) {
    console.error('获取模型列表失败:', error);
    throw error;
  }
}
```

## 错误处理

所有接口在发生错误时会返回一个包含错误信息的JSON响应：

```javascript
{
  "error": "错误描述信息"
}
```

建议在使用axios时进行适当的错误处理：

```javascript
import axios from 'axios';

// 添加响应拦截器
axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response) {
      // 服务器返回错误状态码
      console.error('API错误:', error.response.data);
    } else if (error.request) {
      // 请求发送失败
      console.error('网络错误:', error.request);
    } else {
      // 请求配置错误
      console.error('请求错误:', error.message);
    }
    return Promise.reject(error);
  }
);
```