"""Defines Number keyword container."""

import logging
import sys
from dataclasses import dataclass
from typing import Literal

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.base import Controller
from wse.feature.base.container import Container
from wse.feature.base.mixins import AddObserverGeneric
from wse.feature.interfaces.icontent import ContentProto
from wse.feature.interfaces.iobserver import Observable
from wse.feature.shared.widgets.boxes import FlexColumn

from .protocols import (
    NumpadContainerProto,
    NumpadControllerProto,
    NumpadModelProto,
)

logger = logging.getLogger(__name__)

MAX_CHAR_COUNT = 8
NO_TEXT = ''

# Numpad characters
BACKSPACE = '\u232b'
DOT = '\u002e'
MINUS = '\u002d'
ALLOWED_CHARACTERS = '1234567890'
SPECIAL_CHARACTERS = [BACKSPACE, DOT, MINUS]

ModelNotifyT = Literal['numpad_input_updated']
ContainerNotifyT = Literal['button_pressed']
ControllerNotifyT = Literal['numpad_entered']


@inject
class NumpadModel(
    AddObserverGeneric[ModelNotifyT],
):
    """Model for NumPad container."""

    def __init__(
        self,
        subject: Observable,
    ) -> None:
        """Construct the model."""
        self._subject = subject
        self._input: str = ''

    # Business logic

    def _handle_backspace_char(self) -> bool:
        if self._input == '0.':
            self._input = NO_TEXT
        elif self._input == MINUS + '0.':
            self._input = MINUS
        elif self._input == NO_TEXT:
            return False
        else:
            self._input = self._input[:-1]
        return True

    def _handle_dot_char(self) -> bool:
        if DOT in self._input:
            return False
        elif self._input == NO_TEXT or self._input == MINUS:
            self._input += '0.'
        else:
            self._input += DOT
        return True

    def _handle_minus_char(self) -> None:
        if self._input.startswith(MINUS):
            self._input = self._input[1:]
        else:
            self._input = MINUS + self._input

    def _handle_allowed_char(self, char: str) -> None:
        if self._input == '0':
            self._input += DOT
        self._input += char

    @staticmethod
    def _validate_char(char: str) -> bool:
        if not isinstance(char, str) or len(char) != 1:
            logger.error(f'Expected single character as str, got {repr(char)}')
            return False

        if char in ALLOWED_CHARACTERS:
            return True

        if char in SPECIAL_CHARACTERS:
            return True

        logger.error(
            f'Invalid character. Allowed: digits 0-9 or '
            f'{" ".join(repr(c) for c in SPECIAL_CHARACTERS)}, '
            f'got {repr(char)}'
        )
        return False

    def _notify_input_updated(self) -> None:
        self._notify('numpad_input_updated', value=self._input)

    # API for controller

    def update_input(self, char: str) -> None:
        """Update the user input."""
        if not self._validate_char(char):
            return
        elif len(self._input) >= MAX_CHAR_COUNT and char != BACKSPACE:
            return

        module = sys.modules[__name__]
        to_notify = True

        match char:
            case module.BACKSPACE:
                to_notify = self._handle_backspace_char()
            case module.DOT:
                to_notify = self._handle_dot_char()
            case module.MINUS:
                self._handle_minus_char()
            case _:
                self._handle_allowed_char(char)

        if to_notify:
            self._notify_input_updated()
        else:
            # Ignore event
            pass

    def clear_input(self) -> None:
        """Clear the entered data."""
        self._input = NO_TEXT


@inject
@dataclass
class NumpadContainer(
    AddObserverGeneric[ContainerNotifyT],
    Container,
):
    """Number keyword container."""

    _subject: Observable
    _style: StyleConfig
    _theme: ThemeConfig

    def _setup(self) -> None:
        self._build_boxes()
        self.update_style(self._style)
        self.update_style(self._theme)

    def _populate_content(self) -> None:
        self.content.add(self._outer_box)

    def _create_ui(self) -> None:
        # Create buttons
        self._btn_1 = self._create_button(1)
        self._btn_2 = self._create_button(2)
        self._btn_3 = self._create_button(3)
        self._btn_4 = self._create_button(4)
        self._btn_5 = self._create_button(5)
        self._btn_6 = self._create_button(6)
        self._btn_7 = self._create_button(7)
        self._btn_8 = self._create_button(8)
        self._btn_9 = self._create_button(9)
        self._btn_0 = self._create_button(0)
        self._btn_backspace = self._create_button(BACKSPACE)
        self._btn_dote = self._create_button(DOT)
        self._btn_minus = self._create_button(MINUS)

    def _build_boxes(self) -> None:
        self._build_num_box()
        self._build_sign_box()
        self._build_outer_box()

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""
        # Update buttons style
        for row in self._num_box.children:
            for button in row.children:
                button.style.update(**config.button)

        for button in self._sign_box.children:
            button.style.update(**config.button)

        # Update outer NumPad box style
        self._outer_box.style.update(**config.numpad.outer_box)

    def update_enabled(self, enabled: bool) -> None:
        """Update buttons enabled features."""
        for row in self._num_box.children:
            for button in row.children:
                button.enabled = enabled

        for button in self._sign_box.children:
            button.enabled = enabled

    # Utility layout methods

    def _create_button(self, text: str | int) -> toga.Button:
        return toga.Button(text=str(text), on_press=self._handle_button_press)

    def _handle_button_press(self, button: toga.Button) -> None:
        self._notify('button_pressed', value=button.text)

    def _build_outer_box(self) -> None:
        """Create outer box for NumPad."""
        # NamPad is wrapped in box
        self._outer_box = toga.Box(children=[self._num_box, self._sign_box])

    def _build_num_box(self) -> None:
        self._num_box = toga.Row(
            children=[
                FlexColumn(
                    children=[
                        self._btn_1,
                        self._btn_4,
                        self._btn_7,
                        self._btn_dote,
                    ]
                ),
                FlexColumn(
                    children=[
                        self._btn_2,
                        self._btn_5,
                        self._btn_8,
                        self._btn_0,
                    ]
                ),
                FlexColumn(
                    children=[
                        self._btn_3,
                        self._btn_6,
                        self._btn_9,
                        self._btn_backspace,
                    ]
                ),
            ]
        )
        self._num_box.style.update(flex=3)

    def _build_sign_box(self) -> None:
        self._sign_box = FlexColumn(
            children=[
                self._btn_minus,
            ]
        )


@inject
@dataclass
class NumpadController(
    AddObserverGeneric[ControllerNotifyT],
    Controller,
    NumpadControllerProto,
):
    """Number keyword controller."""

    _subject: Observable
    _model: NumpadModelProto
    _container: NumpadContainerProto

    def _setup(self) -> None:
        self._model.add_observer(self)
        self._container.add_observer(self)

    # Notification from View

    def button_pressed(self, value: str) -> None:
        """Handle the button press event."""
        self._model.update_input(value)

    # Notification for outer component

    def numpad_input_updated(self, value: str) -> None:
        """Handle the input update event."""
        self._subject.notify('numpad_entered', value=value)

    # API for outer component

    def clear_input(self) -> None:
        """Clear the entered data."""
        self._model.clear_input()

    def disable_buttons(self) -> None:
        """Disable numpad buttons."""
        self._container.update_enabled(enabled=False)

    def enable_buttons(self) -> None:
        """Enable numpad buttons."""
        self._container.update_enabled(enabled=True)

    # Property

    @property
    def content(self) -> ContentProto:
        """Get container content."""
        return self._container.content
