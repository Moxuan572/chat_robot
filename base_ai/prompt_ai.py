import os
from openai import OpenAI
from pydantic import BaseModel

# 从环境变量取 key   连接阿里云
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

#   参数校验
class Request(BaseModel):
    question: str


# 流式输出 AI 回答
def chat_stream(question):
    # 重点：加了 stream=True
    response = client.chat.completions.create(
        model="qwen-turbo",
        messages=[{"role": "user", "content": question}],
        stream=True  # 👈 开启流式输出
    )

    # 逐字接收、逐字打印
    for chunk in response:
        # 取出当前返回的文字
        content = chunk.choices[0].delta.content
        if content:  # 如果有内容才打印
            yield content






