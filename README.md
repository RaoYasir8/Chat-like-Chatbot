# ChatGPT-like Chatbot using FastAPI, LangChain, and Groq

This project is a production-style AI chatbot built with:

- FastAPI for the backend API
- LangChain as the LLM framework
- Groq as the LLM provider
- HTML, CSS, and JavaScript for the frontend

## Features

- ChatGPT-like response generation
- FastAPI REST API
- LangChain + Groq integration
- Simple responsive frontend
- Environment variable configuration
- - CORS support
- Health check endpoint
- Docker support

## Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env