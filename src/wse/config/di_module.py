"""Defines Configuration injection module."""

import json
import logging

from injector import Module, provider, singleton
from pydantic import ValidationError

from wse.config.api_paths import APIConfigV1, MathAPIConfigV1
from wse.config.layout import StyleConfig, ThemeConfig
from wse.config.settings import (
    CONFIGS_PATH,
    LAYOUT_STYLE,
    LAYOUT_THEME,
    STYLE_PATH,
)
from wse.utils.loader import load_style_data

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME

API_CONFIG_PATH = CONFIGS_PATH / 'api.json'
MATH_API_CONFIG_PATH = CONFIGS_PATH / 'api_math.json'

log = logging.getLogger(__name__)


class ConfigModule(Module):
    """Configuration injection module."""

    @provider
    @singleton
    def provide_api_config(self) -> APIConfigV1:
        """Provide API configuration."""
        with open(API_CONFIG_PATH, 'r') as f:
            try:
                return APIConfigV1(**json.load(f))
            except ValidationError:
                log.exception('Load API config error')
                raise

    @provider
    @singleton
    def provide_math_api_config(self) -> MathAPIConfigV1:
        """Provide Math API configuration."""
        with open(MATH_API_CONFIG_PATH, 'r') as f:
            return MathAPIConfigV1(**json.load(f))

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
