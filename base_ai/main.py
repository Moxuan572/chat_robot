from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from prompt_ai import *


app = FastAPI(title="聊天")


@app.post("/input_ai")
def chat_ai(question:Request):
    #    流式输出并且告诉前端这是纯文本
    return  StreamingResponse(chat_stream(question.question),
                              media_type="text/plain",  # 可不加
                              headers={"Content-Encoding":"identity"}     #  流式输出关键
                              )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)







