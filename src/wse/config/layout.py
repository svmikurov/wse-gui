"""Defines application layout configuration."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LayoutConfig:
    """Application layout configuration."""

    window_size: tuple[int, int] = field(default=(400, 400))
    content_style: dict[str, Any] = field(default_factory=dict)
    title: dict[str, Any] = field(default_factory=dict)
    btn_nav: dict[str, Any] = field(default_factory=dict)
