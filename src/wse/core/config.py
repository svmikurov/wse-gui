"""Application settings."""

from pathlib import Path
from typing import Tuple

from pydantic import Field, BaseModel, SecretStr
from pydantic_settings import BaseSettings

MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent


class UiSettings(BaseModel):
    """User interface settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)

    HEADING_LABEL_FONT_SIZE: int = 16
    HEADING_HEIGHT: int = 35
    HEADING_PADDING: Tuple[int, int, int, int] = (5, 0, 10, 0)


class ApiSettings(BaseModel):
    """External API settings."""

    API_BASE_URL: str = Field(default='http://wselfedu.online')
    LOGIN: str = '/auth/token/login/'
    CHECK_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = 'WSE'
    PROJECT_PATH: Path = PROJECT_PATH

    api: ApiSettings = Field(default_factory=ApiSettings)
    ui: UiSettings = Field(default_factory=UiSettings)

    encryption_key: SecretStr
    model_config = {
        'env_file': PROJECT_PATH / '.env',
        'env_file_encoding': 'utf-8',
    }
