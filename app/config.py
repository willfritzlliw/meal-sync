from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    app_name: str = "Meal Sync App"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "not_set")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "not_set")

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
