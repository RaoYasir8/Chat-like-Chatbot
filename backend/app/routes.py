from fastapi import APIRouter, HTTPException

from app.llm_service import generate_response
from app.schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok", "message": "Chatbot API is running"}


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await generate_response(request.message)
        return ChatResponse(response=response)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate response: {str(exc)}",
        )