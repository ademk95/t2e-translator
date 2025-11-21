import os
from pathlib import Path 
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = f"{Path(os.path.join(os.path.dirname(__file__))).parent.parent.absolute()}/.env"

class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    model_config = SettingsConfigDict(env_file=DOTENV, env_file_encoding="utf-8", extra="allow", env_nested_delimiter="__")
    log_level: int
    logger_name: str
    hface_token: str
    
settings = Settings(_env_file=DOTENV, _env_file_encoding='utf-8')