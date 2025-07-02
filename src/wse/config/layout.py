"""Defines application layout configuration."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseConfig:
    """Base class for config."""


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
    label_title: dict[str, str | int] = field(default_factory=dict)
    button: dict[str, str | int] = field(default_factory=dict)
    btn_nav: dict[str, str | int] = field(default_factory=dict)
    selection: dict[str, str | int] = field(default_factory=dict)


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
    label_title: dict[str, str] = field(default_factory=dict)
    button: dict[str, str] = field(default_factory=dict)
    btn_nav: dict[str, str] = field(default_factory=dict)
    selection: dict[str, str] = field(default_factory=dict)


@dataclass
class TextTaskStyle(BaseConfig):
    """Style config for exercise task I/O text container."""

    label_question: dict[str, str | int] = field(default_factory=dict)
    label_answer: dict[str, str | int] = field(default_factory=dict)


@dataclass
class TextTaskTheme(BaseConfig):
    """Theme config for exercise task I/O text container."""

    label_question: dict[str, str] = field(default_factory=dict)
    label_answer: dict[str, str] = field(default_factory=dict)


@dataclass
class NumPadStyle(BaseConfig):
    """Style config for NumPad container."""

    button: dict[str, str | int] = field(default_factory=dict)
    outer_box: dict[str, str | int] = field(default_factory=dict)


@dataclass
class NumPadTheme(BaseConfig):
    """Theme config for NumPad container."""

    button: dict[str, str] = field(default_factory=dict)
    outer_box: dict[str, str] = field(default_factory=dict)


@dataclass
class LoginStyle(BaseConfig):
    """Style config for login container."""

    input: dict[str, str | int] = field(default_factory=dict)
    button: dict[str, str | int] = field(default_factory=dict)


@dataclass
class LoginTheme(BaseConfig):
    """Theme config for login container."""

    input: dict[str, str] = field(default_factory=dict)
    button: dict[str, str] = field(default_factory=dict)
