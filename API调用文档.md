# 302.AI API 调用文档

## 错误分析

**问题**：用户在API调试中使用了GET请求，并在URL中传递大量音色ID，导致URL过长（414 Request-URI Too Large错误）。

**原因**：
- GET请求的URL长度有限制（通常为2048字符）
- 当传递大量音色ID时，URL会超出这个限制
- 正确的做法是使用POST请求，将数据放在请求体中

## 正确的API调用方式

### 1. 直接调用302.AI API

**请求方式**：POST
**URL**：`https://api.302.ai/fish-audio/v1/tts`
**请求头**：
- `Authorization: Bearer {API_KEY}`
- `Content-Type: application/json`

**请求体**：
```json
{
  "text": "您要转换的文本",
  "reference_id": "音色ID",
  "chunk_length": 200,
  "normalize": true,
  "format": "mp3",
  "mp3_bitrate": 64,
  "latency": "normal"
}
```

**示例代码**：
```python
import requests

api_key = "sk-B4V1pwfJF1OzG8PLGEuvo6hvBNonBrb8oWRtHVIUxsRYdPVD"
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    "text": "您好，这是测试文本",
    "reference_id": "c4f09481bf514fd2a864977042119f07",  # 台湾机车妹
    "chunk_length": 200,
    "normalize": true,
    "format": "mp3",
    "mp3_bitrate": 64,
    "latency": "normal"
}

response = requests.post(
    "https://api.302.ai/fish-audio/v1/tts",
    headers=headers,
    json=data
)

if response.status_code == 200:
    result = response.json()
    print("音频URL:", result['url'])
else:
    print("错误:", response.text)
```

### 2. 调用本地API服务

**请求方式**：POST
**URL**：`http://127.0.0.1:39903/fish/tts`
**请求头**：
- `Content-Type: application/json`

**请求体**：
```json
{
  "text": "您要转换的文本",
  "voice": "音色ID"
}
```

**注意**：本地服务需要先登录认证，否则会返回401错误。

**登录方式**：
1. 访问 `http://127.0.0.1:39903/login`
2. 输入用户名：`1585546839`
3. 输入密码：`1585546839@qq.com`
4. 登录后获取会话cookie，在后续请求中携带

### 3. 调用/api302/tts路由

**请求方式**：POST
**URL**：`http://127.0.0.1:39903/api302/tts`
**请求体**：与/fish/tts相同

## 可用的音色ID

| 音色名称 | 音色ID |
|---------|--------|
| 台湾机车妹 | c4f09481bf514fd2a864977042119f07 |
| 麦当劳 | 4066d617322e41abb30ed70eaeaf273f |

## 常见错误及解决方案

1. **401 Unauthorized**：
   - 原因：未登录或会话过期
   - 解决：先登录系统，获取有效的会话

2. **400 Bad Request**：
   - 原因：请求参数不完整或格式错误
   - 解决：确保text和voice参数都已提供

3. **500 Internal Server Error**：
   - 原因：服务器内部错误
   - 解决：检查API密钥是否正确，或联系管理员

4. **414 Request-URI Too Large**：
   - 原因：使用GET请求传递过多参数
   - 解决：使用POST请求，将数据放在请求体中

## 测试结果

直接调用302.AI API测试成功，返回了音频URL：
- 状态码：200
- 响应：`{"url":"https://file.302ai.cn/gpt/imgs/20260407/bd126acd9013463387f89b5668766105.mp3"}`

本地服务需要登录后才能使用，这是正常的安全机制。

## 最佳实践

1. **使用POST请求**：始终使用POST请求传递数据，避免URL长度限制
2. **参数验证**：确保提供所有必需参数
3. **错误处理**：添加适当的错误处理逻辑
4. **会话管理**：对于本地服务，确保保持有效的登录会话
5. **API密钥安全**：不要在代码中硬编码API密钥，使用配置文件或环境变量
