"""Defines protocol for config interfaces."""

from typing import Any, Protocol


class IConfig(Protocol):
    """Protocol for layout config interface."""


class IThemeConfig(IConfig, Protocol):
    """Protocol for layout theme config interface."""

    content: dict[str, Any]
    title: dict[str, str]
    btn_nav: dict[str, str]


class IStyleConfig(IConfig, Protocol):
    """Protocol for layout style config interface."""

    window_size: tuple[int, int]
    title: dict[str, str | int]
    btn_nav: dict[str, str | int]


class ITextTaskIOContainerSC(IConfig, Protocol):
    """Protocol for exercise task I/O text config interface."""

    label: dict[str, str | int]
    output_text: dict[str, str | int]
    input_text: dict[str, str | int]
