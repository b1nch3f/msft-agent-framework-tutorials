from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from core.run import call_agent

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    response: str


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to the agent and get a response.

    Args:
        request: ChatRequest with message and session_id

    Returns:
        ChatResponse with the agent's response text
    """
    try:
        result = await call_agent(request.message, request.session_id)
        return ChatResponse(response=result.text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
