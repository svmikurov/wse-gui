"""Example pages."""

import toga
from toga.constants import COLUMN
from toga.style import Pack

from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_table_source_handler,
)
from wse.pages.widgets.button import BtnApp


class ExampleWidgets:
    """Example main page widgets."""

    def __init__(self) -> None:
        """Construct the widgets."""
        super().__init__()

        self.label_title = toga.Label('Примеры')

        # fmt: off
        # Buttons
        self.btn_goto_table_source = BtnApp('Таблица с источниками', on_press=goto_table_source_handler)  # noqa: E501
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on


class ExampleLayout(ExampleWidgets, toga.Box):
    """Example page layout."""

    def __init__(self) -> None:
        """Construct the layout."""
        super().__init__()
        self.style.direction = COLUMN

        box_alignment = toga.Box(style=Pack(flex=1))

        # DOM
        self.add(
            self.label_title,
            box_alignment,
            self.btn_goto_table_source,
            self.btn_goto_back,
        )
