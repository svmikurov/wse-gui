"""Multiplication exercise page."""

import toga
from toga.constants import RIGHT
from toga.style import Pack

from wse.controllers.multiplication import MultiplicationController
from wse.pages.containers.num_keyboard import NumKeyboard
from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexRow
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.text_input import ListenerMixin

NUM_FONT_SIZE = 48
HEIGHT_SIZE_RATIO = 3.2
NUM_HEIGHT = int(NUM_FONT_SIZE * HEIGHT_SIZE_RATIO)


class NumInput(ListenerMixin, toga.MultilineTextInput):
    """Number input panel."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the widget."""
        super().__init__(*args, **kwargs)
        self.readonly = True
        self.placeholder = '0.0'
        self.style.flex = 1
        self.style.height = NUM_HEIGHT
        self.style.text_align = RIGHT


class MultiplicationWidgets:
    """Multiplication exercise widgets."""

    title: str

    def __init__(self, controller: MultiplicationController) -> None:
        """Construct the page."""
        super().__init__()
        self._plc = controller

        self._label_title = TitleLabel(text=self.title)
        self._text_panel = NumInput(
            style=Pack(
                padding=(0, 0, 0, 0),
                font_size=NUM_FONT_SIZE,
            ),
        )
        self._num_keyboard = NumKeyboard()
        self._num_keyboard.plc.add_listener(self._text_panel)
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke methods on page open."""
        await self._plc.on_open(widget)


class MultiplicationLayout(MultiplicationWidgets, BaseBox):
    """Multiplication exercise layout."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the layout."""
        super().__init__(*args, **kwargs)

        _box_text_panel = BoxFlexRow(children=[self._text_panel])
        _box_align = BoxFlexRow()

        # DOM
        self.add(
            self._label_title,
            _box_text_panel,
            self._num_keyboard,
            self._btn_goto_back,
        )
