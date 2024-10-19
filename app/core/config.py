from pydantic_settings import BaseSettings
from app.core.config import Settings

# Initialize settings
settings = Settings()
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://username:password@localhost/dbname"  # Replace with your actual DB URL
    SECRET_KEY: str = "your_secret_key"

