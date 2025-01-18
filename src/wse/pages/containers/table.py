"""Table container."""

import toga
from toga.constants import ITALIC
from toga.style import Pack

from wse.controllers.table import ControllerTable
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_update_handler,
)
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp, SmBtn
from wse.pages.widgets.label import TitleLabel


class TableWidgets:
    """Table of selected items."""

    title: str
    headings: list
    table_accessors: list

    def __init__(self, controller: ControllerTable) -> None:
        """Construct the table."""
        super().__init__()
        self._plc = controller
        self._plc.event.add_listener(self)

        # fmt: off
        # Title
        self._label_title = TitleLabel(self.title)

        # The table entries management buttons
        self._btn_create = SmBtn('Добавить', on_press=self._plc.create_handler)
        self._btn_update = SmBtn('Изменить', on_press=self._plc.update_handler)
        self._btn_delete = SmBtn('Удалить', on_press=self._plc.delete_handler)

        # The pagination buttons
        self._btn_previous = BtnApp('<', on_press=self._plc.previous_handler)
        self._btn_reload = BtnApp('Обновить', on_press=self._plc.reload_handler)  # noqa: E501
        self._btn_next = BtnApp('>', on_press=self._plc.next_handler)
        # By default, the pagination buttons is disabled.
        self._btn_previous.enabled = False
        self._btn_next.enabled = False

        # Navigation buttons
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        # fmt: on

        # Table
        self._table = toga.Table(
            headings=self.headings,
            accessors=self.table_accessors,
            style=Pack(flex=1, font_style=ITALIC),
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke the populate the table when the table opens."""
        self._plc.on_open(widget)

    #####################################################################
    # Button handlers

    async def update_handler(self, widget: toga.Widget) -> None:
        """Update the entry, button handler."""
        entry = self._table.selection
        self._plc.update_item(entry)
        await goto_foreign_update_handler(widget)

    #####################################################################
    # Source handlers

    def update_next_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_next.enabled = is_active

    def update_previous_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_previous.enabled = is_active


class TableLayout(TableWidgets, BaseBox):
    """Table of items list."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)
        self._box_btns_manage = toga.Box()
        self._box_btns_paginate = toga.Box()

        # DOM
        self.add(
            self._label_title,
            self._box_btns_manage,
            self._table,
            self._box_btns_paginate,
            self._btn_goto_back,
        )
        self._box_btns_manage.add(
            self._btn_create,
            self._btn_update,
            self._btn_delete,
        )
        self._box_btns_paginate.add(
            self._btn_previous,
            self._btn_reload,
            self._btn_next,
        )
