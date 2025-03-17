### 功能描述

根据提供的上下文，生成模型对应的输出。、



### 请求地址

```
https://api.lingyiwanwu.com/v1/chat/completions
```

API密钥:bf1973e0425c45559fd319f217d12a22

### 入参描述

**表1：总体参数**

| 传参方式 | 字段          | 类型             | 必选 | 描述                                                         | 默认值     | 示例值                                                       |
| -------- | ------------- | ---------------- | ---- | ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| Header   | Content-Type  | string           | 是   | 内容类型。                                                   | N/A        | application/json                                             |
| Header   | Authorization | string           | 是   | API Key。                                                    | N/A        | your-api-key                                                 |
| Body     | model         | string           | 是   | 使用的Yi Model模型ID。                                       | N/A        | yi-lightning                                                 |
| Body     | messages      | array            | 是   | 一个由历史消息组成的列表，由系统消息、用户消息和模型消息组成。 | N/A        | 示例值，参阅「[表 2 - messages 参数](https://platform.lingyiwanwu.com/docs/api-reference#表-2messages-参数)」 |
| Body     | tools         | array            | 否   | 模型可调用的工具列表。目前只支持函数作为工具。               | N/A        | 示例请参阅「[表 4 - tools 参数](https://platform.lingyiwanwu.com/docs/api-reference#表-4tools-参数)」 |
| Body     | tool_choice   | string 或 object | 否   | 控制模型是否会调用某个或某些工具。`none` 表示模型不会调用任何工具，而是以文字形式进行回复。`auto` 表示模型可选择以文本进行回复或者调用一个或多个工具。在调用时也可以通过将此字段设置为 `required` 或 ` {"type": "function", "function": {"name": "some_function"} }` 来更强的引导模型使用工具。 | N/A        | auto                                                         |
| Body     | max_tokens    | int or null      | 否   | 指定模型在生成内容时token的最大数量，它定义了生成的上限，但不保证每次都会产生到这个数量。 | 取决于模型 | 5000                                                         |
| Body     | top_p         | float            | 否   | 控制生成结果的随机性。数值越小，随机性越弱；数值越大，随机性越强。 | 0.9        | 取值范围：0到1之间。                                         |
| Body     | temperature   | float            | 否   | 控制生成结果的发散性和集中性。数值越小，越集中；数值越大，越发散。 | 0.3        | 取值范围：0到2之间。                                         |
| Body     | stream        | boolean          | 否   | 是否获取流式输出。                                           | false      | false                                                        |

**表2：messages 参数**

| 传参方式                                                     | 字段     | 类型                                                         | 必选 | 描述                                                         | 对象                                                         | 默认值 | 示例值                                                       |
| ------------------------------------------------------------ | -------- | ------------------------------------------------------------ | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| Body                                                         | messages | `array <message>`                                            | 是   | 一个由历史消息组成的列表，由系统消息、用户消息和模型消息组成。 | 系统消息content （string｜ 必选）：系统消息的内容。role （string 必选）：消息的发出者，此处需设置为 `system`。 | N/A    | `1 { 2   "content" : "you are a robot",3   "role": "system" 4 } ` |
| 用户消息content（string｜ 必选）：用户消息的内容。role（string 必选）：消息的发出者，此处需设置为 `user`。 | N/A      | `1 { 2   "content" : "hello",3   "role": "user" 4 } `        |      |                                                              |                                                              |        |                                                              |
| 模型消息content（string｜ 必选）：模型消息的内容。role（string 必选）：消息的发出者，此处需设置为 `assistant`。 | N/A      | `1 { 2   "content" : "Hello! How can I assist you today?",3   "role": "assistant" 4 } ` |      |                                                              |                                                              |        |                                                              |
| 工具消息content（string｜ 必选）：工具消息的内容。role（string 必选）：消息的发出者，此处需设置为 `tool`。tool_call_id（string 必选）：该条消息响应的工具调用 ID。 | N/A      | `1 { 2   "tool_call_id" : "call_8CHipbX0wSiaKvyMycUNxTbr",3   "role": "tool" 4   "content" : "{"location": "San Francisco", "temperature": "172", "unit": null}"5 } ` |      |                                                              |                                                              |        |                                                              |

**表3：content 参数**

| 传参方式 | 字段                                   | 类型   | 必选                                                         | 描述             | 对象            | 默认值 | 子对象 |
| -------- | -------------------------------------- | ------ | ------------------------------------------------------------ | ---------------- | --------------- | ------ | ------ |
| Body     | Content                                | string | 是  必须定义 string 或 array                                 | 用户消息的内容。 | text 输入的内容 | N/A    | N/A    |
| array    | 内容（dict 数据类型）的数组 输入的内容 | N/A    | Image part（可选项）type \| stringimage_url \| dictimage_url \| dicturl \| string （输入图片的 URL 或者以下格式的 Base64 图片 f"data:image/jpeg;base64,{base64_image}" ）Text part（可选项）type \| stringtext \| string 说明：`yi-vision-v2` 模型支持输入图片 URL 或者 Base64 图片字符串当前单次调用最多可支持 8 张图片作为输入图片支持以下格式：JPEG（.jpeg 和 .jpg）PNG（.png）Base64（f"data:image/jpeg;base64,{base64_image}"）输入的图片支持 2K 及以下分辨率，每张图片大小不应超过 10 MB模型每理解一张图片约消耗 500 ～ 700 token |                  |                 |        |        |

**表4：tools 参数**

| 传参方式 | 字段  | 类型              | 必选 | 描述                         | 对象                                                         |
| -------- | ----- | ----------------- | ---- | ---------------------------- | ------------------------------------------------------------ |
| Body     | tools | `List <function>` | 否   | 一个由自定义工具组成的列表。 | type （string｜必选）：工具的类型，目前只支持 `function`。function （object｜必选）：description （string｜可选）：对工具函数作用的描述，用于帮助模型理解工具的调用时机和方式。name （string｜必选）：要调用的工具函数的名称。必须是 a-z、A-Z、0-9，或包含下划线和破折号，最大长度为 64。parameters （object｜可选）：工具函数可接受的参数，需以 JSON 模式对象的形式进行描述。 |

### 出参描述

| 字段          | 类型                                                         | 子参数                                                       | 描述                                     | 示例值          |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------- | --------------- |
| id            | String                                                       | N/A                                                          | 本次请求的系统唯一码。                   | cmpl-1cfbad15   |
| object        | String                                                       | N/A                                                          | 对象类型，此处固定是 `chat.completion`。 | chat.completion |
| created       | Long                                                         | N/A                                                          | Unix 当前时间戳。                        | 1178759         |
| model         | String                                                       | N/A                                                          | 正在使用的模型名。                       | yi-lightning    |
| choices       | `List <choice>`                                              | index                                                        | 模型生成结果的序号。0 表示第一个结果。   | 0               |
| messages      | 详细说明，参阅「[表 2 - messages参数](https://platform.lingyiwanwu.com/docs/api-reference#表-2messages-参数)」。 | 示例值，参阅「[表 2 - messages参数](https://platform.lingyiwanwu.com/docs/api-reference#表-2messages-参数)」。 |                                          |                 |
| finish_reason | 段式 + 流式`stop`：表示模型返回了完整的输出。`length`：由于生成长度过长导致停止生成内容.以 `content_filter` 开头的表示安全过滤的结果。仅流式`null`：表示正在生成内容。 | stop                                                         |                                          |                 |
| usage         | `List <usage>`                                               | completion_tokens                                            | 内容生成的 tokens 数量。                 | 48              |
| prompt_tokens | prompt 使用的 tokens 数量。                                  | 18                                                           |                                          |                 |
| total_tokens  | 总 tokens 用量。                                             | 66                                                           |                                          |                 |

### 请求和响应示例

##### 同步调用

###### HTTP 示例

- **请求**



```bash
1curl https://api.lingyiwanwu.com/v1/chat/completions \
2  -H "Content-Type: application/json" \
3  -H "Authorization: Bearer $API_KEY" \
4  -d '{
        "model": "yi-lightning",
        "messages": [{"role": "user", "content": "Hi, who are you?"}],
        "temperature": 0.3
8  }'
```

- **响应**



```json
1{
2  "id": "cmpl-c730301f",
3  "object": "chat.completion",
4  "created": 7825887,
5  "model": "yi-lightning",
6  "usage": {
7    "completion_tokens": 65,
8    "prompt_tokens": 15,
9    "total_tokens": 80
10  },
11  "choices": [
12    {
13      "index": 0,
14      "message": {
15        "role": "assistant",
16        "content": "Hello! My name is Yi, and I am a language model based on the transformers architecture developed by 01.AI. My purpose is to be a helpful resource for you, capable of answering questions and offering insightful information across a wide range of topics. How may I be of service to you today?"
17      },
18      "finish_reason": "stop"
19    }
20  ]
21}
```

##### SDK 示例

- **请求**



```python
1import openai
2from openai import OpenAI
3API_BASE = "https://api.lingyiwanwu.com/v1"
4API_KEY = "your key"
5client = OpenAI(
6  api_key=API_KEY,
7  base_url=API_BASE
8)
9completion = client.chat.completions.create(
10  model="yi-lightning",
11  messages=[{"role": "user", "content": "Hi, who are you?"}]
12)
13print(completion)
```

- **响应**



```python
1ChatCompletion(id = 'cmpl-8062fda5',
2 choices = [
3    Choice(
4      finish_reason = 'stop',
5      index = 0,
6      logprobs = None,
7      message = ChatCompletionMessage(
8        content = 'Hello! My name is Yi, and I am a language model based on the transformers architecture developed by 01.AI. My purpose is to be a helpful resource for you, capable of answering questions and offering insightful information across a wide range of topics. How may I be of service to you today ? ',
9        role = 'assistant',
10        function_call = None,
11        tool_calls = None
12      )
13    )
14  ],
15  created = 7826404,
16  model = 'yi-lightning',
17  object = 'chat.completion',
18  system_fingerprint = None,
19  usage = CompletionUsage(
20    completion_tokens = 65,
21    prompt_tokens = 15,
22    total_tokens = 80
23  )
24)
```

##### 流式调用

###### HTTP 示例

- **请求**



```bash
1curl https://api.lingyiwanwu.com/v1/chat/completions \
2  -H "Content-Type: application/json" \
3  -H "Authorization: Bearer $API_KEY" \
4  -d '{
        "model": "yi-lightning",
        "messages": [{"role": "user", "content": "Hi, who are you?"}],
        "temperature": 0.3,
        "stream": true
9  }'
```

- **响应**



```json
1data: {"id":"cmpl78796a05","object":"chat.completion.chunk","created":7828777,"model":"yi-lightning","choices":[{"delta":{"role":"assistant"},"index":0}],"content":"","lastOne":false}
2data: {"id":"cmpl78796a05","object":"chat.completion.chunk","created":7828777,"model":"yi-lightning","choices":[{"delta":{"content":"Hello"},"index":0}],"content":"Hello","lastOne":false}
3...
4data: {"id":"cmpl78796a05","object":"chat.completion.chunk","created":7828777,"model":"yi-lightning","choices":[{"delta":{},"index":0,"finish_reason":"stop"}],"content":"Hello! My name is Yi, and I am a language model based on the transformers architecture developed by 01.AI. My purpose is to be a helpful resource for you, capable of answering questions and offering insightful information across a wide range of topics. How may I be of service to you today?","usage":{"completion_tokens":64,"prompt_tokens":17,"total_tokens":81},"lastOne":true}
5data: [DONE]
```

##### SDK 示例

- **请求**



```python
1import openai
2from openai import OpenAI
3API_BASE = "https://api.lingyiwanwu.com/v1"
4API_KEY = "your key"
5client = OpenAI(
6  api_key=API_KEY,
7  base_url=API_BASE
8)
9completion = client.chat.completions.create(
10  model="yi-lightning",
11  messages=[{"role": "user", "content": "Hi, who are you?"}],
12  stream=True
13)
14for chunk in completion:
15  print(chunk.choices[0].delta.content or "", end="", flush=True)
```

- **响应**

```
Hello! My name is Yi, and I am a language model based on the transformers architecture developed by 01.AI. My purpose is to be a helpful resource for you, capable of answering questions and offering insightful information across a wide range of topics. How may I be of service to you today?
```

## List models

### 功能描述

显示可用的模型。

### 请求地址

```
https://api.lingyiwanwu.com/v1/models
```

### 出参描述

| 字段    | 类型   | 描述                              | 示例值       |
| ------- | ------ | --------------------------------- | ------------ |
| id      | String | 可用的模型ID。                    | yi-lightning |
| object  | String | 对象类型，此处固定是`model`。     | model        |
| created | Long   | Unix当前时间戳。                  | 1178759      |
| ownedBy | String | 模型所属的公司，此处固定是01.ai。 | 01.ai        |

### 请求和响应提示

#### HTTP 示例

- **请求**



```bash
1curl --location 'https://api.lingyiwanwu.com/v1/models' \
2  --header "Authorization: Bearer $API_KEY"
```

- **响应**



```json
1{
2  "data": [
3    {
4      "id": "yi-lightning",
5      "object": "model",
6      "created": 1708258504,
7      "ownedBy": "01.ai",
8      "root": "",
9      "parent": ""
10    }
11  ],
12  "object": "list"
13}
```

#### SDK 示例

- **请求**



```python
1import openai
2from openai import OpenAI
3API_BASE = 'https://api.lingyiwanwu.com/v1'
4API_KEY = "your key"
5client = OpenAI(
6  api_key=API_KEY,
7  base_url=API_BASE,
8  timeout=300
9)
10models = client.models.list()
11print(models)
```

- **响应**



```python
1SyncPage[Model](
2  data=[
3    Model(
4      id='yi-lightning',
5      created=1708671653,
6      object='model',
7      owned_by=None,
8      ownedBy='01.ai',
9      root='',
10      parent=''
11    )
12  ],
13  object='list'
14)
```

# 状态码

| HTTP 返回码    | 错误代码                                                     | 原因                                                  | 解决方案                                         |
| -------------- | ------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------ |
| 400            | Bad request                                                  | 模型的输入+输出（max_tokens）超过了模型的最大上下文。 | 减少模型的输入，或将 max_tokens 参数值设置更小。 |
| 输入格式错误。 | 检查输入格式，确保正确。例如，模型名必须全小写，yi-lightning。 |                                                       |                                                  |
| 401            | Authentication Error                                         | API Key缺失或无效。                                   | 请确保你的 API Key 有效。                        |
| 404            | Not found                                                    | 无效的 Endpoint URL 或模型名。                        | 确保使用正确的 Endpoint URL 或模型名。           |
| 429            | Too Many Requests                                            | 在短时间内发出的请求太多。                            | 控制请求速率。                                   |
| 500            | Internal Server Error                                        | 服务端内部错误。                                      | 请稍后重试。                                     |
| 529            | System busy                                                  | 系统繁忙，请重试。                                    | 请 1 分钟后重试。                                |