from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    PORT:int = 9000
    DATABASE_CONNECTION_STRING:str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()