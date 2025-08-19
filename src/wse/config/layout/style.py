"""Defines widget style configuration."""

from pydantic import BaseModel, Field


class BaseStyle(BaseModel):
    """Base class for style config."""


class AssignedStyle(BaseStyle):
    """Style config for the container of Assigned exercises."""

    label: dict[str, str | int] = {}
    button: dict[str, str | int] = {}


class LoginStyle(BaseStyle):
    """Style config for login container."""

    input: dict[str, str | int] = {}
    button: dict[str, str | int] = {}


class NumPadStyle(BaseStyle):
    """Style config for NumPad container."""

    button: dict[str, str | int] = {}
    outer_box: dict[str, str | int] = {}


class TextTaskStyle(BaseStyle):
    """Style config for exercise task I/O text container."""

    label_question: dict[str, str | int] = {}
    label_answer: dict[str, str | int] = {}


class TopBarStyle(BaseStyle):
    """Theme config for Top Bar container."""

    button: dict[str, str | int] = {}
    label_balance: dict[str, str | int] = {}


# TODO: Rename `label_title` to `title_sm`, `title_md`
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

    window_size: tuple[int, int] = Field(default=(440, 700))

    btn_nav: dict[str, str | int] = {}
    button: dict[str, str | int] = {}
    label_title: dict[str, str | int] = {}
    selection: dict[str, str | int] = {}

    assigned: AssignedStyle = Field(default_factory=AssignedStyle)
    login: LoginStyle = Field(default_factory=LoginStyle)
    numpad: NumPadStyle = Field(default_factory=NumPadStyle)
    text_task: TextTaskStyle = Field(default_factory=TextTaskStyle)
    top_bar: TopBarStyle = Field(default_factory=TopBarStyle)
