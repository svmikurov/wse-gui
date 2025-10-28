"""Defines theme configuration for widgets."""

from typing import Any

from pydantic import BaseModel, Field


class BaseTheme(BaseModel):
    """Base class for theme config."""


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
    label_balance: dict[str, str] = {}


class PresenterTheme(BaseTheme):
    """Theme config for Presenter container."""

    definition: dict[str, str] = {}
    explanation: dict[str, str] = {}


class ParamsConfig(BaseTheme):
    """Theme config for params container."""

    label: dict[str, str] = {}
    select: dict[str, str] = {}
    number: dict[str, str] = {}


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
    number_input: dict[str, str] = {}

    top_bar: TopBarTheme = Field(default_factory=TopBarTheme)
    login: LoginTheme = Field(default_factory=LoginTheme)
    numpad: NumPadTheme = Field(default_factory=NumPadTheme)
    assigned: AssignedTheme = Field(default_factory=AssignedTheme)
    text_task: TextTaskTheme = Field(default_factory=TextTaskTheme)
    presenter: PresenterTheme = Field(default_factory=PresenterTheme)
    params: ParamsConfig = Field(default_factory=ParamsConfig)
