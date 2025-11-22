import asyncio
import uuid

from core.utils import call_agent


async def main():
    session_id = str(uuid.uuid4())

    response = await call_agent("If x = 2 and y = 5, what is x + y", session_id)
    print("Agent Response:", response)

    # Use same session_id - should remember context
    response2 = await call_agent("Add 10 to that", session_id)
    print("Agent Response 2:", response2)


if __name__ == "__main__":
    asyncio.run(main())
