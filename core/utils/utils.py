from typing import Dict

from agent_framework import ChatMessageStore

# Store message stores by session_id
_session_stores: Dict[str, ChatMessageStore] = {}


async def get_or_create_message_store(session_id: str) -> ChatMessageStore:
    """Get existing message store for session or create new one"""
    if session_id not in _session_stores:
        _session_stores[session_id] = ChatMessageStore()
    return _session_stores[session_id]
