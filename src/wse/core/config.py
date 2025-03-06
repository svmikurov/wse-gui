"""Defines application settings and configurations."""

from pathlib import Path
from typing import Tuple

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent
ENV_PATH = PROJECT_PATH / '.env'


class UIConfig(BaseModel):
    """Stores user interface settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)

    HEADING_LABEL_FONT_SIZE: int = 16
    HEADING_HEIGHT: int = 35
    HEADING_PADDING: Tuple[int, int, int, int] = (5, 0, 10, 0)


class APIConfig(BaseModel):
    """Stores configuration for API endpoints and settings."""

    base_url: str = Field(default='http://wselfedu.online')
    REQUEST_TIMEOUT: int = 10

    LOGIN: str = '/auth/token/login/'
    VALIDATE_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class StorageConfig(BaseSettings):
    """Stores configuration for storage-related settings."""

    token_file: Path = PROJECT_PATH / 'token.enc'
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

    api_config: APIConfig = Field(default_factory=APIConfig)
    storage_config: StorageConfig = Field(default_factory=StorageConfig)
    ui_config: UIConfig = Field(default_factory=UIConfig)

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )
