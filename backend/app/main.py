from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_allowed_origins
from app.routes import router

app = FastAPI(
    title="ChatGPT-like Chatbot API",
    description="A production-style chatbot backend using FastAPI, LangChain, and Groq.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    return {
        "message": "Welcome to the ChatGPT-like Chatbot API",
        "docs": "/docs",
        "chat_endpoint": "/api/chat",
    }
