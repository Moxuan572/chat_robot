from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import uvicorn
from prompt import *
from database import *

app = FastAPI(title="聊天机器人",tags=["chat"])

@app.post("/chat_robot")
def chat_robot(question:Request,db: Session=Depends(get_session)):
    return StreamingResponse(chat_stream(question.question,question.user_id,db),
                             headers = {"Content-Encoding":"identity"}
                             )

@app.delete("/delete_user")
def delete_user(user_id: str= "default_user",db: Session = Depends(get_session)):
    user = db.query(Record).filter(Record.name == user_id).first()
    db.delete(user)

    db.commit()

    return {"messages":"删除成功"}


@app.get("/")
def get_user():
    return {"messages":"聊天机器人启动成功"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)