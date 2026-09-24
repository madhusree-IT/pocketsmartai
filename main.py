from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.database.connection import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(
    title="PocketSmart AI",
    description="Smart Budget & Recommendation Assistant",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "PocketSmart AI is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}