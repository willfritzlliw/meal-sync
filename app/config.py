from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    app_name: str = "Meal Sync App"
    admin_email: str = "admin@example.com"
    items_per_user: int = 10
    OPENAI_API_KEY: str
    MODEL_NAME: str = "gpt-4"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
