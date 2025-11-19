import asyncio
import os

from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIResponsesClient
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")


async def main():
    client = AzureOpenAIResponsesClient(
        api_key=api_key,
        endpoint=endpoint,
        deployment_name=deployment_name,
    )

    agent = ChatAgent(chat_client=client, instructions="You are good at reasoning.")

    async for update in agent.run_stream("Explain quantum computing in simple terms."):
        if update.text:
            print(update.text, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
