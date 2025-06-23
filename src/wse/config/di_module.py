"""Defines config injector modules container."""

import json

from injector import Module, provider, singleton

from wse.config.layout import StyleConfig, ThemeConfig
from wse.config.settings import LAYOUT_STYLE, LAYOUT_THEME, STYLE_PATH

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME


class ConfigModule(Module):
    """Configuration injection modules container."""

    @provider
    @singleton
    def provide_style_config(self) -> StyleConfig:
        """Load and provide layout style configuration."""
        try:
            with open(LAYOUT_STYLE_PATH, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        return StyleConfig(**data)

    @provider
    @singleton
    def provide_theme_config(self) -> ThemeConfig:
        """Load and provide layout color theme configuration."""
        try:
            with open(LAYOUT_THEME_PATH, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        return ThemeConfig(**data)
