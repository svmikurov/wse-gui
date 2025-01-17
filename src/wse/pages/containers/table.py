"""Table container."""

import toga
from toga.constants import ITALIC
from toga.style import Pack

from wse.controllers.table import ConntrollerTable
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
    source_class = None

    def __init__(self, controller: ConntrollerTable) -> None:
        """Construct the table."""
        super().__init__()
        self.plc = controller
        self.plc.event.add_listener(self)
        # To override
        self.headings = None

        # Title
        self._label_title = TitleLabel(self.title)

        # Source
        self.entry = self.source_class

        # The table entries management buttons
        self._btn_create = SmBtn('Добавить', on_press=self.plc.create_handler)
        self._btn_update = SmBtn('Изменить', on_press=self.plc.update_handler)
        self._btn_delete = SmBtn('Удалить', on_press=self.plc.delete_handler)

        # The pagination buttons
        self._btn_previous = BtnApp('<', on_press=self.plc.previous_handler)
        self._btn_reload = BtnApp('Обновить', on_press=self.plc.reload_handler)
        self._btn_next = BtnApp('>', on_press=self.plc.next_handler)
        # By default, the pagination buttons is disabled.
        self._btn_previous.enabled = False
        self._btn_next.enabled = False

        # Navigation buttons
        self._btn_goto_back = BtnApp('Назад', on_press=goto_back_handler)

        # Table
        self._table = toga.Table(
            headings=self.headings,
            data=self.plc.entry,
            accessors=self.entry.accessors,
            style=Pack(flex=1, font_style=ITALIC),
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Invoke the populate the table when the table opens."""
        self.plc.on_open(widget)

    #####################################################################
    # Button handlers

    async def update_handler(self, widget: toga.Widget) -> None:
        """Update the entry, button handler."""
        entry = self._table.selection
        self.plc.update_item(entry)
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
