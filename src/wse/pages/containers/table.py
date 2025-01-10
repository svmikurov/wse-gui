"""Table container."""

from wse.pages.handlers.goto_handler import goto_back_handler
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp
from wse.pages.widgets.label import TitleLabel
from wse.pages.widgets.table import TableApp


class TableLayout(TableApp, BaseBox):
    """Table of items list."""

    title = ''

    def __init__(self) -> None:
        """Construct the page."""
        super().__init__()

        # Title
        self.label_title = TitleLabel(self.title)

        # Navigation buttons
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Page widgets DOM.
        self.add(
            self.label_title,
            self.btns_manage,
            self.table,
            self.btns_paginate,
            self.btn_goto_back,
        )
