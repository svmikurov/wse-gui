"""Defines Configuration injection module."""

import json
import logging
from typing import TypeVar

from injector import Module, provider, singleton

from wse.utils.loader import load_style_data

from .layout import (
    AssignedStyle,
    AssignedTheme,
    LoginStyle,
    LoginTheme,
    NumPadStyle,
    NumPadTheme,
    StyleConfig,
    TextTaskStyle,
    TextTaskTheme,
    ThemeConfig,
    TopBarStyle,
    TopBarTheme,
)
from .settings import (
    CONFIGS_PATH,
    LAYOUT_STYLE,
    LAYOUT_THEME,
    STYLE_PATH,
    APIConfigV1,
)

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME
API_CONFIG_PATH = CONFIGS_PATH / 'api.json'

T = TypeVar('T')

logger = logging.getLogger(__name__)


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

    @provider
    @singleton
    def provide_text_exercise_style(self) -> TextTaskStyle:
        """Load and provide layout style configuration."""
        return load_style_data(
            LAYOUT_STYLE_PATH,
            TextTaskStyle,
            container_alice='text_task_panel',
        )

    @provider
    @singleton
    def provide_text_exercise_theme(self) -> TextTaskTheme:
        """Load and provide layout color theme configuration."""
        return load_style_data(
            LAYOUT_THEME_PATH,
            TextTaskTheme,
            container_alice='text_task_panel',
        )

    @provider
    @singleton
    def provide_numpad_style_config(self) -> NumPadStyle:
        """Load and provide layout style configuration."""
        return load_style_data(
            LAYOUT_STYLE_PATH,
            NumPadStyle,
            container_alice='numpad',
        )

    @provider
    @singleton
    def provide_numpad_theme_config(self) -> NumPadTheme:
        """Load and provide layout color theme configuration."""
        return load_style_data(
            LAYOUT_THEME_PATH,
            NumPadTheme,
            container_alice='numpad',
        )

    # Login

    @provider
    @singleton
    def provide_login_style(self) -> LoginStyle:
        """Load and provide layout style for Login container."""
        return load_style_data(
            LAYOUT_STYLE_PATH,
            LoginStyle,
            container_alice='login',
        )

    @provider
    @singleton
    def provide_numpad_theme(self) -> LoginTheme:
        """Load and provide layout color theme for Login container."""
        return load_style_data(
            LAYOUT_THEME_PATH,
            LoginTheme,
            container_alice='login',
        )

    @provider
    @singleton
    def provide_top_bar_style(self) -> TopBarStyle:
        """Load and provide layout style for top bar container."""
        return load_style_data(
            LAYOUT_STYLE_PATH,
            TopBarStyle,
            container_alice='top_bar',
        )

    @provider
    @singleton
    def provide_top_bar_theme(self) -> TopBarTheme:
        """Load and provide layout color theme for top bar container."""
        return load_style_data(
            LAYOUT_THEME_PATH,
            TopBarTheme,
            container_alice='top_bar',
        )

    @provider
    @singleton
    def provide_assigned_style(self) -> AssignedStyle:
        """Load and provide style for Assigned exercises."""
        return load_style_data(
            LAYOUT_STYLE_PATH,
            AssignedStyle,
            container_alice='assigned',
        )

    @provider
    @singleton
    def provide_assigned_theme(self) -> AssignedTheme:
        """Load and Provide theme for Assigned exercises."""
        return load_style_data(
            LAYOUT_THEME_PATH,
            AssignedTheme,
            container_alice='assigned',
        )
