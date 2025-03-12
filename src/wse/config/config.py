"""Defines application settings and configurations."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Paths
MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parents[2]
ENV_PATH = PROJECT_PATH / '.env'


class Languages(str, Enum):
    """Defines aliases of supported languages."""

    EN = 'en'
    RU = 'ru'


@dataclass
class ScreenConfig:
    """Stores screen settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)


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

    # Paths
    PROJECT_PATH: Path = PROJECT_PATH

    # API
    REQUEST_TIMEOUT: int = 10
    base_url: str = Field(default='http://wselfedu.online')

    # Auth
    AUTH_REQUIRED: bool = Field(default=True)

    # Translation
    LANGUAGE: Languages = Field(default=Languages.EN)

    # Navigation
    HISTORY_LEN: int = Field(default=10)

    # Configs
    storage_config: StorageConfig = Field(default_factory=StorageConfig)
    screen_config: ScreenConfig = Field(default_factory=ScreenConfig)

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )
