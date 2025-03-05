"""Application settings."""

from pathlib import Path
from typing import Tuple

from pydantic import BaseModel, Field, SecretStr
from pydantic.json import SecretStrJsonMixin
from pydantic_settings import BaseSettings

MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parent.parent.parent


class UIConfig(BaseModel):
    """User interface settings."""

    SCREEN_SIZE: Tuple[int, int] = (440, 700)

    HEADING_LABEL_FONT_SIZE: int = 16
    HEADING_HEIGHT: int = 35
    HEADING_PADDING: Tuple[int, int, int, int] = (5, 0, 10, 0)


class APIConfig(BaseModel):
    """Configuration for API endpoints and settings.

    :param base_url: Base URL of the API.
    :param REQUEST_TIMEOUT: Timeout for HTTP requests in seconds.
    :param LOGIN: Endpoint for authentication.
    :param VALIDATE_TOKEN: Endpoint for token validation.
    :param TASK: Endpoint for get task, send answer.
    """

    base_url: str = Field(default='http://wselfedu.online')

    REQUEST_TIMEOUT: int = 10

    LOGIN: str = '/auth/token/login/'
    VALIDATE_TOKEN: str = '/api/v1/auth/users/me/'
    TASK: str = '/api/v1/task/'


class Settings(SecretStrJsonMixin, BaseSettings):
    """Application settings loaded from environment variables.

    :param api_config: Configuration for API endpoints.
    :param token_file: File to store the authentication token.
    :param encryption_key: Secret key for encrypting the token file.
    """

    APP_NAME: str = 'WSE'
    PROJECT_PATH: Path = PROJECT_PATH

    api_config: APIConfig = Field(default_factory=APIConfig)
    ui_config: UIConfig = Field(default_factory=UIConfig)

    token_file: Path = PROJECT_PATH / 'token'
    encryption_key: SecretStr

    model_config = {
        'env_file': PROJECT_PATH / '.env',
        'env_file_encoding': 'utf-8',
    }
