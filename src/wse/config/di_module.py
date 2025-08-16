"""Defines Configuration injection module."""

import json

from injector import Module, provider, singleton

from wse.config.layout import StyleConfig, ThemeConfig
from wse.config.settings import (
    CONFIGS_PATH,
    LAYOUT_STYLE,
    LAYOUT_THEME,
    STYLE_PATH,
    APIConfigV1,
)
from wse.utils.loader import load_style_data

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME

API_CONFIG_PATH = CONFIGS_PATH / 'api.json'


class ConfigModule(Module):
    """Configuration injection module."""

    @provider
    @singleton
    def provide_api_config(self) -> APIConfigV1:
        """Provide API configuration."""
        with open(API_CONFIG_PATH, 'r') as f:
            return APIConfigV1(**json.load(f))

    @provider
    @singleton
    def provide_style_config(self) -> StyleConfig:
        """Load and provide layout style configuration."""
        return load_style_data(LAYOUT_STYLE_PATH, StyleConfig)

    @provider
    @singleton
    def provide_theme_config(self) -> ThemeConfig:
        """Load and provide layout color theme configuration."""
        return load_style_data(LAYOUT_THEME_PATH, ThemeConfig)
