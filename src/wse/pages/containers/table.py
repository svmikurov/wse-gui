"""Table container."""

import toga
from toga.constants import ITALIC
from toga.style import Pack

from wse.pages.handlers.goto_handler import (
    goto_back_handler,
    goto_foreign_update_handler,
)
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp, SmBtn
from wse.pages.widgets.label import TitleLabel


class TableWidgets:
    """Table of selected items."""

    title = ''

    def __init__(self, controller) -> None:
        """Construct the table."""
        super().__init__()
        self.plc_selected = controller

        # Title
        self.label_title = TitleLabel(self.title)

        # Source
        self.entry = self.source_class

        # fmt: off
        # The pagination buttons
        self._btn_previous = BtnApp('<', on_press=self.plc_selected.previous_handler)  # noqa: E501
        self._btn_reload = BtnApp('Обновить', on_press=self.plc_selected.reload_handler)  # noqa: E501
        self._btn_next = BtnApp('>', on_press=self.plc_selected.next_handler)
        # By default, the pagination buttons is disabled.
        self._btn_previous.enabled = False
        self._btn_next.enabled = False
        # Pagination buttons container
        self.box_paginate = toga.Box(
            children=[self._btn_previous, self._btn_reload, self._btn_next]
        )
        # The table entries management buttons
        self._btn_create = SmBtn('Добавить', on_press=self.plc_selected.create_handler)  # noqa: E501
        self._btn_update = SmBtn('Изменить', on_press=self.plc_selected.update_handler)  # noqa: E501
        self._btn_delete = SmBtn('Удалить', on_press=self.plc_selected.delete_handler)  # noqa: E501
        # Management buttons container 
        self.btns_manage = toga.Box(
            children=[self._btn_create, self._btn_update, self._btn_delete]
        )
        # fmt: on

        # Navigation buttons
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)
        self.btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Table
        self.table = toga.Table(
            headings=self.headings,
            data=self.entry,
            accessors=self.entry.accessors,
            style=Pack(flex=1, font_style=ITALIC)
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke the populate the table when the table opens."""
        self.clear_table()
        self.plc_selected.on_open(widget)

    #####################################################################
    # Button handlers

    async def update_handler(self, widget: toga.Widget) -> None:
        """Update the entry, button handler."""
        entry = self.table.selection
        self.plc_selected.update_item(entry)
        await goto_foreign_update_handler(widget)

    #####################################################################
    # Event handlers

    def update_next_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_next.enabled = is_active

    def update_previous_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_previous.enabled = is_active

    def populate_table(self, entries) -> None:
        """Populate the table on url request."""
        for entry in entries:
            self.entry.add_entry(entry)

    def clear_table(self) -> None:
        """Clear the table."""
        self.table.data.clear()


class TableLayout(TableWidgets, BaseBox):
    """Table of items list."""

    def __init__(self, *args, **kwargs) -> None:
        """Construct the page."""
        super().__init__(*args, **kwargs)

        # DOM
        self.add(
            self.label_title,
            self.btns_manage,
            self.table,
            self.box_paginate,
            self.btn_goto_back,
        )
