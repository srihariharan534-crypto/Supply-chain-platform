import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings using Pydantic for validation."""
    
    # Project Settings
    PROJECT_NAME: str = "Supply Chain Platform"
    ENVIRONMENT: str = "development"
    
    # Database Settings
    DATABASE_URL: str = "sqlite:///data/warehouse/supply_chain.db"
    
    # API Settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    SECRET_KEY: str = "default-secret-key-replace-in-production"
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Base paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR: str = os.path.join(BASE_DIR, "data")
    RAW_DATA_DIR: str = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR: str = os.path.join(DATA_DIR, "processed")
    FEATURE_STORE_DIR: str = os.path.join(DATA_DIR, "feature_store")
    WAREHOUSE_DIR: str = os.path.join(DATA_DIR, "warehouse")
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

# Global settings instance
settings = Settings()

# Ensure directories exist
for directory in [settings.RAW_DATA_DIR, settings.PROCESSED_DATA_DIR, settings.FEATURE_STORE_DIR, settings.WAREHOUSE_DIR]:
    os.makedirs(directory, exist_ok=True)
