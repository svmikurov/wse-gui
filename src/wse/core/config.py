"""Application settings."""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent


class ApiSettings(BaseSettings):
    """External API settings."""

    API_BASE_URL: str = Field(default='http://wselfedu.online')

    LOGIN: str = '/auth/token/login/'
    CHECK_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = 'WSE'
    PROJECT_PATH: Path

    api: ApiSettings = Field(default_factory=ApiSettings)

    model_config = {
        'env_file': PROJECT_PATH / '.env',
        'env_file_encoding': 'utf-8',
    }
