"""Table container."""

import toga
from toga.constants import ITALIC
from toga.style import Pack

from wse.controllers.table import ControllerTable
from wse.pages.handlers.goto_handler import (
    goto_back_handler,
)
from wse.pages.widgets.box_page import BaseBox
from wse.pages.widgets.button import BtnApp, SmBtn
from wse.pages.widgets.label import TitleLabel
from wse.sources.source_list import SourceListApp


class TableWidgets:
    """Table of selected items."""

    title: str
    table_headings: list
    table_accessors: list
    source_accessors: list
    url: str
    url_detail: str

    def __init__(self, controller: ControllerTable) -> None:
        """Construct the table."""
        super().__init__()
        self._plc = controller
        self._plc.entry = SourceListApp(accessors=self.source_accessors)
        self._plc.event.add_listener(self)

        # fmt: off
        # Title
        self._label_title = TitleLabel(self.title)

        # The table entries management buttons
        self._btn_create = SmBtn('Добавить', on_press=self._create_handler)
        self._btn_update = SmBtn('Изменить', on_press=self._update_handler)
        self._btn_delete = SmBtn('Удалить', on_press=self._display_confirm_deletion_handler)  # noqa: E501
        self._btn_delete_cancel = SmBtn('Отмена', on_press=self._hide_confirm_deletion_handler)  # noqa: E501
        self._btn_delete_confirm = SmBtn('Удалить', on_press=self._confirm_deletion_handler)  # noqa: E501

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
            headings=self.table_headings,
            data=self._plc.entry,
            accessors=self.table_accessors,
            style=Pack(flex=1, font_style=ITALIC),
        )

    async def on_open(self, widget: toga.Widget) -> None:
        """Call a methods when opening a page."""
        self._plc.on_open(widget, self.url)

    #####################################################################
    # Listener methods

    def update_next_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_next.enabled = is_active

    def update_previous_button(self, is_active: bool) -> None:
        """Set active or not the next button."""
        self._btn_previous.enabled = is_active

    #####################################################################
    # Button handlers

    async def _create_handler(self, widget: toga.Widget) -> None:
        await self._plc.goto_create_handler(widget, url=self.url)

    async def _update_handler(self, widget: toga.Widget) -> None:
        item_id = self._get_entry_id()
        if item_id:
            await self._plc.goto_update_handler(
                widget, url=self.url_detail, item_id=item_id
            )

    async def _confirm_deletion_handler(self, widget: toga.Widget) -> None:
        await self._delete(widget)
        self._hide_confirm_deletion_handler(widget)

    #################
    # Utility methods

    def _get_entry_id(self) -> str:
        try:
            entry_id = self._table.selection.id
        except AttributeError:
            print('INFO: The entry is empty')
        else:
            return entry_id

    async def _delete(self, widget: toga.Widget) -> None:
        item_id = self._get_entry_id()
        if item_id:
            await self._plc.delete_handler(
                widget, self.url_detail, item_id=self._get_entry_id()
            )

    #############################
    # Interactive button handlers

    def _display_confirm_deletion_handler(self, _: toga.Widget) -> None:
        raise NotImplementedError()

    def _hide_confirm_deletion_handler(self, _: toga.Widget) -> None:
        raise NotImplementedError()


class TableLayout(TableWidgets, BaseBox):
    """Item list table."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        """Construct a table layout."""
        super().__init__(*args, **kwargs)
        # Table button box
        self._box_btns_manage = toga.Box()
        # Pagination button box
        self._box_btns_paginate = toga.Box()

        # Interactive widgets
        self._box_confirm_deletion = toga.Box(
            children=[self._btn_delete_cancel, self._btn_delete_confirm]
        )

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

    #############################
    # Interactive button handlers

    def _display_confirm_deletion_handler(self, _: toga.Widget) -> None:
        self.replace(self._box_btns_manage, self._box_confirm_deletion)

    def _hide_confirm_deletion_handler(self, _: toga.Widget) -> None:
        self.replace(self._box_confirm_deletion, self._box_btns_manage)
