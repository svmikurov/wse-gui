"""Defines thema configuration for widgets."""

from typing import Any

from pydantic import BaseModel, Field


class BaseTheme(BaseModel):
    """Base class for thema config."""


class AssignedTheme(BaseTheme):
    """Theme config for the container of Assigned exercises."""

    label: dict[str, str] = {}
    button: dict[str, str] = {}


class LoginTheme(BaseTheme):
    """Theme config for login container."""

    input: dict[str, str] = {}
    button: dict[str, str] = {}


class NumPadTheme(BaseTheme):
    """Theme config for NumPad container."""

    button: dict[str, str] = {}
    outer_box: dict[str, str] = {}


class TextTaskTheme(BaseTheme):
    """Theme config for exercise task I/O text container."""

    label_question: dict[str, str] = {}
    label_answer: dict[str, str] = {}


class TopBarTheme(BaseTheme):
    """Theme config for Top Bar container."""

    button: dict[str, str] = {}
    label_balance: dict[str, str | int] = {}


class ThemeConfig(BaseTheme):
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

    content: dict[str, Any] = {}

    btn_nav: dict[str, str] = {}
    button: dict[str, str] = {}
    label_title: dict[str, str] = {}
    selection: dict[str, str] = {}

    assigned: AssignedTheme = Field(default_factory=AssignedTheme)
    login: LoginTheme = Field(default_factory=LoginTheme)
    numpad: NumPadTheme = Field(default_factory=NumPadTheme)
    text_task: TextTaskTheme = Field(default_factory=TextTaskTheme)
    top_bar: TopBarTheme = Field(default_factory=TopBarTheme)
