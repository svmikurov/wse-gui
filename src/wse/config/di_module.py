"""Defines config injector modules container."""

import json
from dataclasses import fields
from pathlib import Path
from typing import Any, Type, TypeVar

from injector import Module, provider, singleton

from wse.config.layout import (
    NumPadStyleConfig,
    NumPadThemeConfig,
    StyleConfig,
    TextExerciseStyleConfig,
    TextExerciseThemeConfig,
    ThemeConfig,
)
from wse.config.settings import LAYOUT_STYLE, LAYOUT_THEME, STYLE_PATH

LAYOUT_STYLE_PATH = STYLE_PATH / LAYOUT_STYLE
LAYOUT_THEME_PATH = STYLE_PATH / LAYOUT_THEME

T = TypeVar('T')


def filter_data(
    klass: Type[T],
    data: dict[str, Any],
) -> dict[str, Any]:
    """Filter data for dataclass."""
    return {f.name: data[f.name] for f in fields(klass) if f.name in data}  # type: ignore[arg-type]


def load_data(path: Path, klass: Type[T], component: str | None = None) -> T:
    """Load config data from file."""
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
            data = json_data if component is None else json_data[component]
    except FileNotFoundError:
        data = {}

    filtered_data = filter_data(klass, data)
    return klass(**filtered_data)


class ConfigModule(Module):
    """Configuration injection modules container."""

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
    def provide_text_exercise_style_config(self) -> TextExerciseStyleConfig:
        """Load and provide layout style configuration."""
        return load_data(
            LAYOUT_STYLE_PATH,
            TextExerciseStyleConfig,
            'text_exercise',
        )

    @provider
    @singleton
    def provide_text_exercise_theme_config(self) -> TextExerciseThemeConfig:
        """Load and provide layout color theme configuration."""
        return load_data(
            LAYOUT_THEME_PATH,
            TextExerciseThemeConfig,
            'text_exercise',
        )

    @provider
    @singleton
    def provide_numpad_style_config(self) -> NumPadStyleConfig:
        """Load and provide layout style configuration."""
        return load_data(
            LAYOUT_STYLE_PATH,
            NumPadStyleConfig,
            'numpad',
        )

    @provider
    @singleton
    def provide_numpad_theme_config(self) -> NumPadThemeConfig:
        """Load and provide layout color theme configuration."""
        return load_data(
            LAYOUT_THEME_PATH,
            NumPadThemeConfig,
            'numpad',
        )
