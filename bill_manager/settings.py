from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    HOST: str = "172.27.96.1"
    PORT: int = 8080
    RELOAD: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
