"""Defines application settings and configurations."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Paths
MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent
ENV_PATH = PROJECT_PATH / '.env'


class Languages(str, Enum):
    """Defines aliases of supported languages."""

    EN = 'en'
    RU = 'ru'


@dataclass
class ScreenConfig:
    """Stores screen settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)


class APIConfig(BaseModel):
    """Stores configuration for API endpoints and settings."""

    REQUEST_TIMEOUT: int = 10

    # Endpoints
    LOGIN: str = '/auth/token/login/'
    VALIDATE_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class StorageConfig(BaseSettings):
    """Stores configuration for storage-related settings."""

    token_file: Path = PROJECT_PATH / 'data' / 'secrets' / 'token.enc'
    encryption_key: SecretStr

    model_config = SettingsConfigDict(
        env_prefix='STORAGE_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )


class Settings(BaseSettings):
    """Stores and manages application settings."""

    APP_ID: str = 'online.wselfedu'
    APP_NAME: str = 'WSE'
    FORMAL_NAME: str = 'WSE'
    base_url: str = Field(default='http://wselfedu.online')

    AUTH_REQUIRED: bool = Field(default=True)
    LANGUAGE: Languages = Field(default=Languages.EN)
    HISTORY_LEN: int = Field(default=10)

    api_config: APIConfig = Field(default_factory=APIConfig)
    storage_config: StorageConfig = Field(default_factory=StorageConfig)
    screen_config: ScreenConfig = Field(default_factory=ScreenConfig)

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )
