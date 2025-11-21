from dotenv import load_dotenv
from fastapi import FastAPI

from api.routes import router as main_router
from api.routes.chat import router as chat_router

load_dotenv()

app = FastAPI(title="Agent Framework API")

# Include routers
app.include_router(main_router)
app.include_router(chat_router)
