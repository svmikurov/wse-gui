"""Defines widget style configuration."""

from pydantic import BaseModel, Field


class BaseStyle(BaseModel):
    """Base class for style config."""


class AssignedStyle(BaseStyle):
    """Style config for the container of Assigned exercises."""

    mark: dict[str, str | int] = {}
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
    """Style config for Top Bar container."""

    button: dict[str, str | int] = {}
    label_balance: dict[str, str | int] = {}


class PresenterStyle(BaseStyle):
    """Style config for Presenter container."""

    question: dict[str, str | int] = {}
    answer: dict[str, str | int] = {}


class ParamsStyle(BaseStyle):
    """Style config for Params container."""

    label: dict[str, str | int] = {}
    select: dict[str, str | int] = {}
    number: dict[str, str | int] = {}


class ControlStyle(BaseStyle):
    """Style config for Control container."""

    left_btn: dict[str, str | int] = {}
    inner_btn: dict[str, str | int] = {}
    right_btn: dict[str, str | int] = {}
    outbox: dict[str, str | int] = {}


class InfoStyle(BaseStyle):
    """Style config for Info container."""

    label: dict[str, str | int] = {}


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
    # TODO: Rename 'label_title' to 'title'
    label_title: dict[str, str | int] = {}
    selection: dict[str, str | int] = {}
    number_input: dict[str, str | int] = {}
    switch: dict[str, str | int] = {}

    top_bar: TopBarStyle = Field(default_factory=TopBarStyle)
    login: LoginStyle = Field(default_factory=LoginStyle)
    numpad: NumPadStyle = Field(default_factory=NumPadStyle)
    assigned: AssignedStyle = Field(default_factory=AssignedStyle)
    text_task: TextTaskStyle = Field(default_factory=TextTaskStyle)
    presenter: PresenterStyle = Field(default_factory=PresenterStyle)
    params: ParamsStyle = Field(default_factory=ParamsStyle)
    control: ControlStyle = Field(default_factory=ControlStyle)
    info: InfoStyle = Field(default_factory=InfoStyle)
