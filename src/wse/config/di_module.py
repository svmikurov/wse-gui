"""Defines Configuration injection module."""

import json
import logging
from dataclasses import fields
from pathlib import Path
from typing import Any, Type, TypeVar

from injector import Module, provider, singleton

from .layout import (
    LoginStyle,
    LoginTheme,
    NumPadStyle,
    NumPadTheme,
    StyleConfig,
    TextTaskStyle,
    TextTaskTheme,
    ThemeConfig,
)
from .settings import LAYOUT_STYLE, LAYOUT_THEME, STYLE_PATH

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME

T = TypeVar('T')

logger = logging.getLogger(__name__)


def filter_data(
    klass: Type[T],
    data: dict[str, Any],
) -> dict[str, Any]:
    """Filter data for dataclass."""
    return {f.name: data[f.name] for f in fields(klass) if f.name in data}  # type: ignore[arg-type]


def load_data(path: Path, klass: Type[T], component: str | None = None) -> T:
    """Load config data from file."""
    data = {}
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
            data = json_data if component is None else json_data[component]
    except FileNotFoundError:
        logger.error(f"Config '{path.name}' not found")
    except KeyError:
        logger.error(
            f"Config '{path.name}' have no configuration "
            f"for '{component}' container"
        )

    filtered_data = filter_data(klass, data)
    return klass(**filtered_data)


class ConfigModule(Module):
    """Configuration injection module."""

    @provider
    @singleton
    def provide_style_config(self) -> StyleConfig:
        """Load and provide layout style configuration."""
        return load_data(LAYOUT_STYLE_PATH, StyleConfig)

    @provider
    @singleton
    def provide_theme_config(self) -> ThemeConfig:
        """Load and provide layout color theme configuration."""
        return load_data(LAYOUT_THEME_PATH, ThemeConfig)

    @provider
    @singleton
    def provide_text_exercise_style(self) -> TextTaskStyle:
        """Load and provide layout style configuration."""
        return load_data(
            LAYOUT_STYLE_PATH,
            TextTaskStyle,
            'text_task_panel',
        )

    @provider
    @singleton
    def provide_text_exercise_theme(self) -> TextTaskTheme:
        """Load and provide layout color theme configuration."""
        return load_data(
            LAYOUT_THEME_PATH,
            TextTaskTheme,
            'text_task_panel',
        )

    @provider
    @singleton
    def provide_numpad_style_config(self) -> NumPadStyle:
        """Load and provide layout style configuration."""
        return load_data(
            LAYOUT_STYLE_PATH,
            NumPadStyle,
            'numpad',
        )

    @provider
    @singleton
    def provide_numpad_theme_config(self) -> NumPadTheme:
        """Load and provide layout color theme configuration."""
        return load_data(
            LAYOUT_THEME_PATH,
            NumPadTheme,
            'numpad',
        )

    # Login

    @provider
    @singleton
    def provide_login_style(self) -> LoginStyle:
        """Load and provide layout style for Login container."""
        return load_data(
            LAYOUT_STYLE_PATH,
            LoginStyle,
            'login',
        )

    @provider
    @singleton
    def provide_numpad_theme(self) -> LoginTheme:
        """Load and provide layout color theme for Login container."""
        return load_data(
            LAYOUT_THEME_PATH,
            LoginTheme,
            'login',
        )
