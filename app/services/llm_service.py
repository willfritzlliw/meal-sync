from ..config import settings
from langchain_openai import ChatOpenAI

def get_llm(temperature: float = 0.7):
    llm = ChatOpenAI(
        model_name=settings.MODEL_NAME,
        openai_api_key=settings.OPENAI_API_KEY,
        temperature=temperature,
        max_retries=3
    )
    return llm
