"""Fraction widget explore page."""

import toga
from toga.constants import CENTER, COLUMN
from toga.style import Pack

from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box import BoxFlexRow
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.fraction import Fraction


class FractionPage(toga.Box):
    """Fraction widget explore page."""

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()
        self.style.flex = 1
        self.style.direction = COLUMN

        _label_title = toga.Label(
            text='Построение виджета "Дроби"',
            style=Pack(text_align=CENTER),
        )
        _fraction = Fraction()
        btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        self.add(
            _label_title,
            _fraction,
            BoxFlexRow(),
            btn_goto_back,
        )
