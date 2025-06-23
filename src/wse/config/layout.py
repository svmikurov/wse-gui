"""Defines application layout configuration."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ThemeConfig:
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
class StyleConfig:
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
