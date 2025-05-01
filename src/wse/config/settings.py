"""Defines application settings and configurations."""

from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Paths
MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parents[2]
RESOURCES_PATH = PROJECT_PATH / 'src' / 'wse' / 'resources'
STYLES = RESOURCES_PATH / 'styles'
ENV_PATH = PROJECT_PATH / '.env'


class StorageConfig(BaseSettings):
    """Stores configuration for storage-related settings."""

    token_path: Path = PROJECT_PATH / 'data' / 'secrets' / 'token.enc'
    encryption_key: SecretStr

    model_config = SettingsConfigDict(
        env_prefix='STORAGE_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )


class Settings(BaseSettings):
    """Stores and manages application settings."""

    # Paths
    PROJECT_PATH: Path = PROJECT_PATH
    ENDPOINTS_PATH: Path = (
        PROJECT_PATH / 'src' / 'wse' / 'config' / 'endpoints.yml'
    )

    # Navigation
    HISTORY_LEN: int = 10

    # URL
    base_url: str = Field(default='http://wselfedu.online')
    request_timeout: int = Field(default=10)

    # Configs
    storage_config: StorageConfig = Field(default_factory=StorageConfig)

    model_config = SettingsConfigDict(
        env_prefix='APP_',
        env_file=ENV_PATH,
        env_file_encoding='utf-8',
        extra='ignore',
    )
