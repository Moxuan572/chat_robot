import os
from fastapi import Depends
from openai import OpenAI
from pydantic import *
from database import *


client = OpenAI(
    api_key = os.getenv("DASHSCOPE_API_KEY"),
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

class Request(BaseModel):
    question: str
    user_id: str= "default_user"

def get_session():
    with Session() as session:
        yield session

# 储存所有的对话
user_context = {}


def chat_stream(question: str,user_id: str,db: Session):
    if user_id not in user_context:
        user_context[user_id] = [{"role":"system","content":"你是个ai助手，要友善,准确,简短的回答"}]

    user_context[user_id].append({"role":"user","content":question})

    response = client.chat.completions.create(
        model = "qwen-turbo",
        messages = user_context[user_id],
        stream = True
    )

    answer = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            answer += content
            yield content


    user_context[user_id].append({"role": "assistant", "content": answer})


    res = Record(
        name = user_id,
        answers = answer,
        questions = question
    )

    db.add(res)
    db.commit()




