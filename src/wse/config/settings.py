"""Defines application settings."""

from pathlib import Path

from pydantic import BaseModel

from wse.apps.nav_id import NavID

from .enums import (
    Language,
    LayoutStyle,
    LayoutTheme,
    LocaleDomain,
)

# General paths
PROJECT_PATH = Path(__file__).parents[1]
RESOURCES_PATH = PROJECT_PATH / 'resources'
STYLE_PATH = RESOURCES_PATH / 'style'
CONFIGS_PATH = RESOURCES_PATH / 'config'

# Language
LANGUAGE = Language.RU  # Default language
LOCALE_DOMAINS = [  # Localization domains
    LocaleDomain.CORE,
    LocaleDomain.NAV,
    LocaleDomain.LABEL,
    LocaleDomain.EXERCISE,
]

# Authentication
SUCCESS_REDIRECT = NavID.HOME

# Layout style
LAYOUT_THEME = LayoutTheme.DEVELOP
LAYOUT_STYLE = LayoutStyle.DEVELOP


class ApiConfig(BaseModel):
    """Base api configuration."""


class APIConfigV1(ApiConfig):
    """API configuration for v1 version."""

    base_url: str
    jwt: dict[str, str]
