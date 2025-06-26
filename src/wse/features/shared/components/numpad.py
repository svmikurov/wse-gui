"""Defines Number keyword container."""

import logging
from dataclasses import dataclass

import toga
from injector import inject

from wse.config.layout import NumPadStyleConfig, NumPadThemeConfig

from ...base.boxes import FlexColumn
from ...base.container import BaseContainer
from ...base.mixins import AddObserverMixin
from ...interfaces import IContent, ISubject
from ...shared.components.interfaces import INumPadContainer, INumPadModel

logger = logging.getLogger(__name__)

MAX_SYMBOL_COUNT = 8
NO_TEXT = ''

# Numpad signs
BACKSPACE = '\u232b'
DOTE = '\u002e'
MINUS = '\u2014'


@inject
class NumPadModel(
    AddObserverMixin,
):
    """Model for NumPad container."""

    def __init__(
        self,
        subject: ISubject,
    ) -> None:
        """Construct the model."""
        self._subject = subject
        self._input: str = ''

    def update_input(self, symbol: str) -> None:
        """Update the user input."""
        if symbol == BACKSPACE and self._input == '0.':
            self._input = NO_TEXT
        elif symbol == BACKSPACE:
            self._input = self._input[:-1]
        elif len(self._input) >= MAX_SYMBOL_COUNT:
            return
        elif symbol == DOTE and symbol in self._input:
            return
        elif symbol == DOTE and self._input == NO_TEXT:
            self._input += '0.'
        elif self._input == '0':
            self._input += DOTE + symbol
        else:
            self._input += symbol

        self._subject.notify('numpad_input_updated', value=self._input)


@inject
@dataclass
class NumPadContainer(
    BaseContainer,
    AddObserverMixin,
):
    """Number keyword container."""

    _model: INumPadModel
    _style_config: NumPadStyleConfig
    _theme_config: NumPadThemeConfig

    def _setup(self) -> None:
        self._subject.add_observer(self._model)
        self._build_boxes()
        self.update_style(self._style_config)
        self.update_style(self._theme_config)

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
        self._btn_dote = self._create_button(DOTE)
        self._btn_minus = self._create_button(MINUS)

    def _build_boxes(self) -> None:
        self._build_num_box()
        self._build_sign_box()
        self._build_outer_box()

    # TODO: Remove `localize_ui()` method dependency (SOLID error)
    def localize_ui(self) -> None:
        """Localize the UI text."""
        pass

    def update_style(
        self, config: NumPadStyleConfig | NumPadThemeConfig
    ) -> None:
        """Update widgets style."""
        # Update buttons style
        for row in self._num_box.children:
            for button in row.children:
                button.style.update(**config.button)

        for button in self._sign_box.children:
            button.style.update(**config.button)

        # Update outer NumPad box style
        self._outer_box.style.update(**config.outer_box)

    # Utility methods

    def _create_button(self, text: str | int) -> toga.Button:
        return toga.Button(text=str(text), on_press=self._handle_button_press)

    def _handle_button_press(self, button: toga.Button) -> None:
        self._subject.notify('button_pressed', value=button.text)

    def _build_outer_box(self) -> None:
        """Create outer box for NumPad."""
        # NamPad is wrapped in box
        self._outer_box = toga.Box(children=[self._num_box, self._sign_box])

    def _build_num_box(self) -> None:
        self._num_box = toga.Row(
            children=[
                FlexColumn(children=[self._btn_1, self._btn_4, self._btn_7]),
                FlexColumn(children=[self._btn_2, self._btn_5, self._btn_8]),
                FlexColumn(children=[self._btn_3, self._btn_6, self._btn_9]),
            ]
        )
        self._num_box.style.update(flex=3)

    def _build_sign_box(self) -> None:
        self._sign_box = FlexColumn(
            children=[
                self._btn_backspace,
                self._btn_minus,
                self._btn_dote,
            ]
        )


# TODO: Add base controller without navigate feature
#  (to avoid SOLID error)
@inject
@dataclass
class NumPadController(
    AddObserverMixin,
):
    """Number keyword controller."""

    _subject: ISubject
    _model: INumPadModel
    _container: INumPadContainer

    def __post_init__(self) -> None:
        """Set up the controller."""
        self._model.add_observer(self)
        self._container.add_observer(self)

    @property
    def content(self) -> IContent:
        """Get page content."""
        return self._container.content

    # Event notifications

    def button_pressed(self, value: str) -> None:
        """Handel the button press event."""
        self._model.update_input(value)

    def numpad_input_updated(self, value: str) -> None:
        """Handle the input update event."""
        self._subject.notify('numpad_input_updated', value=value)
