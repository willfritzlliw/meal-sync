from fastapi import FastAPI
from app.api import endpoints
from app.config import settings

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
