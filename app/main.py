from fastapi import FastAPI
from .api import endpoints
from .config import settings
from .chains import summarize_chain
from pydantic import BaseModel, Field

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

class SummarizeRequest(BaseModel):
    text: str = Field(..., example="Recipe to summarize goes here.")
    max_length: int = Field(300, example=300)

class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    summary_length: int

@app.post("/summarize")
async def root(request: SummarizeRequest) -> SummarizeResponse:
    """
    Summarize the recipe text.
    
    Args:
        request: SummarizeRequest containing the text to summarize
        
    Returns:
        SummarizeResponse with the summarized text and metadata
    """
    try:
        summary = summarize_chain.summarize_text(request.text)
        return SummarizeResponse(
            summary=summary,
            original_length=len(request.text),
            summary_length=len(summary)
        )
    except Exception as e:
        return {"error": str(e)}
