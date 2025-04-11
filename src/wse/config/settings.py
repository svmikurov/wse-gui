"""Defines application settings and configurations."""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

# Paths
MODULE_PATH = Path(__file__).resolve().parent
PROJECT_PATH = MODULE_PATH.parents[2]
ENV_PATH = PROJECT_PATH / '.env'


class Settings(BaseSettings):
    """Stores and manages application settings."""

    # Paths
    PROJECT_PATH: Path = PROJECT_PATH

    # URL
    base_url: str = Field(default='http://wselfedu.online')
