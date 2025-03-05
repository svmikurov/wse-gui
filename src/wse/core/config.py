"""Application settings."""

from pathlib import Path
from typing import Tuple

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent


class UIConfig(BaseModel):
    """User interface settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)

    HEADING_LABEL_FONT_SIZE: int = 16
    HEADING_HEIGHT: int = 35
    HEADING_PADDING: Tuple[int, int, int, int] = (5, 0, 10, 0)


class APIConfig(BaseModel):
    """Configuration for API endpoints and settings."""

    base_url: str = Field(default='http://wselfedu.online')
    REQUEST_TIMEOUT: int = 10

    LOGIN: str = '/auth/token/login/'
    VALIDATE_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    APP_NAME: str = 'WSE'
    PROJECT_PATH: Path = PROJECT_PATH

    api_config: APIConfig = Field(default_factory=APIConfig)
    ui_config: UIConfig = Field(default_factory=UIConfig)

    token_file: Path = PROJECT_PATH / 'token.enc'
    encryption_key: SecretStr

    model_config = SettingsConfigDict(
        env_file=PROJECT_PATH / '.env',
        env_file_encoding='utf-8',
        env_prefix='API_',
        extra='ignore',
    )
