import os
from typing import Dict

from agent_framework.azure import AzureOpenAIResponsesClient
from dotenv import load_dotenv

load_dotenv()

from agent_framework import ChatAgent, ChatMessage, ChatMessageStore, Role, TextContent

from core.message_store import get_or_create_message_store

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")


client = AzureOpenAIResponsesClient(
    api_key=api_key,
    endpoint=endpoint,
    deployment_name=deployment_name,
)


agent = ChatAgent(
    chat_client=client,
    instructions="You are good at reasoning.",
)


async def call_agent(text_message: str, session_id: str):
    message_store = await get_or_create_message_store(session_id)

    # Add user message to store
    await message_store.add_messages([ChatMessage(role=Role.USER, text=text_message)])

    # Get all messages for context
    text_messages = await message_store.list_messages()

    # Run agent with messages
    response = await agent.run(text_messages)

    # Add assistant response back to message store
    await message_store.add_messages(
        [ChatMessage(role=Role.ASSISTANT, content=TextContent(text=response.text))]
    )

    return response
