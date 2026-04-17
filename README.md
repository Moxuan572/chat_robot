# 🤖 大模型聊天机器人 API 服务

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Streaming](https://img.shields.io/badge/Streaming-SSE-orange.svg)

基于大模型API的智能聊天机器人服务，支持流式输出、上下文记忆和多会话管理，完整的大模型应用落地实践。

## ✨ 功能特性
- 🧩 集成第三方大模型API（阿里通义千问/OpenAI）
- 🔥 支持Server-Sent Events(SSE)流式实时输出
- 🗨️ 自动维护对话上下文，支持多轮对话
- 👥 多用户会话隔离，安全管理对话历史
- 📦 轻量化部署，开箱即用

## 🛠️ 技术栈
| 技术 | 用途 |
|------|------|
| Python 3.9+ | 开发语言 |
| FastAPI | 后端Web框架 |
| Uvicorn | ASGI服务器 |
| Pydantic | 数据验证 |
| SQLAlchemy | 数据库ORM |

## 🚀 快速启动
```bash
# 克隆项目
git clone https://github.com/Moxuan572/chat_robot.git
cd chat_robot

# 安装依赖
pip install fastapi uvicorn sqlalchemy openai

# 启动服务,在main.py文件下启动
uvicorn.run("main:app",host="127.0.0.1",post=8080)
