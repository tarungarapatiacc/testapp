from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Application settings."""
    
    # Server
    PORT: int = 8000
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # Security
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # NLP
    SPACY_MODEL: str = "en_core_web_sm"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
