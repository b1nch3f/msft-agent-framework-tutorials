import uuid

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "AI Agent API is running"}


@router.get("/health")
async def health():
    return {"status": "healthy"}


@router.get("/session")
async def create_session():
    """Create a new session ID"""
    return {"session_id": str(uuid.uuid4())}
