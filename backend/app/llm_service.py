from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq

from app.config import settings


SYSTEM_PROMPT = """
You are a helpful AI assistant like ChatGPT.
Answer clearly, politely, and accurately.
If the user asks for code, provide clean and practical code.
If you do not know something, say so honestly.
"""


llm = ChatGroq(
    groq_api_key=settings.GROQ_API_KEY,
    model=settings.GROQ_MODEL,
    temperature=0.7,
    max_tokens=1024,
)


async def generate_response(user_message: str) -> str:
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_message),
    ]

    result = await llm.ainvoke(messages)
    return result.content