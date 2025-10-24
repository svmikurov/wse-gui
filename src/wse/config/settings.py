"""Defines application settings."""

from pathlib import Path

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
FIXTURE_PATH = RESOURCES_PATH / 'fixtures'

# Language
LANGUAGE = Language.RU  # Default language
LOCALE_DOMAINS = [  # Localization domains
    LocaleDomain.CORE,
    LocaleDomain.NAV,
    LocaleDomain.LABEL,
    LocaleDomain.EXERCISE,
]

# Layout style
LAYOUT_THEME = LayoutTheme.DEVELOP
LAYOUT_STYLE = LayoutStyle.DEVELOP
