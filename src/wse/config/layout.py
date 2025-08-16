"""Defines application layout configuration."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class BaseConfig:
    """Base class for config."""


@dataclass
class BaseStyle(BaseConfig):
    """Base class for style config."""


@dataclass
class BaseThema(BaseConfig):
    """Base class for thema config."""


@dataclass
class StyleConfig(BaseStyle):
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
    top_bar: dict[str, str | int] = field(default_factory=dict)
    assigned: dict[str, str | int] = field(default_factory=dict)


@dataclass
class ThemeConfig(BaseThema):
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
    top_bar: dict[str, str] = field(default_factory=dict)
    assigned: dict[str, str] = field(default_factory=dict)


@dataclass
class TextTaskStyle(BaseStyle):
    """Style config for exercise task I/O text container."""

    label_question: dict[str, str | int] = field(default_factory=dict)
    label_answer: dict[str, str | int] = field(default_factory=dict)


@dataclass
class TextTaskTheme(BaseThema):
    """Theme config for exercise task I/O text container."""

    label_question: dict[str, str] = field(default_factory=dict)
    label_answer: dict[str, str] = field(default_factory=dict)


@dataclass
class NumPadStyle(BaseStyle):
    """Style config for NumPad container."""

    button: dict[str, str | int] = field(default_factory=dict)
    outer_box: dict[str, str | int] = field(default_factory=dict)


@dataclass
class NumPadTheme(BaseThema):
    """Theme config for NumPad container."""

    button: dict[str, str] = field(default_factory=dict)
    outer_box: dict[str, str] = field(default_factory=dict)


@dataclass
class LoginStyle(BaseStyle):
    """Style config for login container."""

    input: dict[str, str | int] = field(default_factory=dict)
    button: dict[str, str | int] = field(default_factory=dict)


@dataclass
class LoginTheme(BaseThema):
    """Theme config for login container."""

    input: dict[str, str] = field(default_factory=dict)
    button: dict[str, str] = field(default_factory=dict)


@dataclass
class TopBarStyle(BaseStyle):
    """Theme config for Top Bar container."""

    button: dict[str, str | int] = field(default_factory=dict)
    label_balance: dict[str, str | int] = field(default_factory=dict)


@dataclass
class TopBarTheme(BaseThema):
    """Theme config for Top Bar container."""

    button: dict[str, str] = field(default_factory=dict)
    label_balance: dict[str, str | int] = field(default_factory=dict)


@dataclass
class AssignedStyle(BaseStyle):
    """Style config for the container of Assigned exercises."""

    label: dict[str, str | int] = field(default_factory=dict)


@dataclass
class AssignedTheme(BaseThema):
    """Theme config for the container of Assigned exercises."""

    label: dict[str, str] = field(default_factory=dict)
