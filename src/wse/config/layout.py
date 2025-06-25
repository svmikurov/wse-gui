"""Defines application layout configuration."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseConfig:
    """Base class for config."""


@dataclass
class ThemeConfig(BaseConfig):
    """Application layout theme configuration.

    For example, load from json config:

        {
          "content": {
            "background_color": "blue"
          },
          "title": {
            "background_color": "green",
            "color": "yellow"
          },
          ...
        }
    """

    content: dict[str, Any] = field(default_factory=dict)
    title: dict[str, str] = field(default_factory=dict)
    btn_nav: dict[str, str] = field(default_factory=dict)


@dataclass
class StyleConfig(BaseConfig):
    """Application layout style configuration.

    For example, load from json config:

        {
          "window_size": [440, 700],
          "title": {
            "font_size": 20,
            "text_align": "center",
            ...
          },
          ...
        }
    """

    window_size: tuple[int, int] = field(default=(440, 700))
    title: dict[str, str | int] = field(default_factory=dict)
    btn_nav: dict[str, str | int] = field(default_factory=dict)


@dataclass
class TextExerciseStyleConfig(BaseConfig):
    """Style config for exercise task I/O text container."""

    label: dict[str, str | int] = field(default_factory=dict)
    output_text: dict[str, str | int] = field(default_factory=dict)
    input_text: dict[str, str | int] = field(default_factory=dict)


@dataclass
class TextExerciseThemeConfig(BaseConfig):
    """Theme config for exercise task I/O text container."""

    label: dict[str, str] = field(default_factory=dict)
    output_text: dict[str, str] = field(default_factory=dict)
    input_text: dict[str, str] = field(default_factory=dict)


@dataclass
class NumPadStyleConfig(BaseConfig):
    """Style config for NumPad container."""

    button: dict[str, str | int] = field(default_factory=dict)


@dataclass
class NumPadThemeConfig(BaseConfig):
    """Theme config for NumPad container."""

    button: dict[str, str | int] = field(default_factory=dict)
