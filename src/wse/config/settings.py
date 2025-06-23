"""Defines application settings."""

from pathlib import Path

from wse.config.enums import (
    ColorStyles,
    Languages,
    LayoutStyles,
)

# General paths
PROJECT_PATH = Path(__file__).parents[1]
RESOURCES_PATH = PROJECT_PATH / 'resources'
CONFIGS_PATH = RESOURCES_PATH / 'config'

# Layout style configuration
LANGUAGE = Languages.RU
COLOR_STYLE = ColorStyles.DEFAULT
LAYOUT_STYLE = LayoutStyles.DEFAULT
