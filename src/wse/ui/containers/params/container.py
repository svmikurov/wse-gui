"""Params container."""

from dataclasses import dataclass
from functools import partial
from typing import Any, override

import toga
from injector import inject

from wse.feature.observer.accessor import AccessorMixin
from wse.feature.observer.mixins import AddNotifyMixin, ObserverManagerGen
from wse.ui.base.content.mixins import GetContentMixin
from wse.utils.contextmanager import EventDisabler
from wse.utils.i18n import I18N

from . import ParamsContainerABC
from .entity import NamedEntitySource


@inject
@dataclass
class ParamsContainer(
    AccessorMixin,
    AddNotifyMixin,
    ObserverManagerGen[Any],
    GetContentMixin,
    ParamsContainerABC,
):
    """Params container."""

    _accessors = ('mark_select', 'category_select')

    @override
    def _create_ui(self) -> None:
        self._category_label = toga.Label(I18N.LABEL('Category'))
        self._category_select = self._create_selection('category_select')
        self._mark_label = toga.Label(I18N.LABEL('Mark'))
        self._mark_select = self._create_selection('mark_select')

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._build_row(self.category_select, self.mark_select),
        )

    # Combined widgets
    # ----------------

    @property
    def category_select(self) -> toga.Box:
        """Word count select."""
        return self._combine(self._category_label, self._category_select)

    @property
    def mark_select(self) -> toga.Box:
        """Mark select."""
        return self._combine(self._mark_label, self._mark_select)

    # Utility methods
    # ---------------

    @staticmethod
    def _build_row(*children: toga.Widget) -> toga.Box:
        """Build row box."""
        return toga.Box(children=children)

    @staticmethod
    def _combine(label: toga.Label, widget: toga.Widget) -> toga.Box:
        """Combine into a labeled widget."""
        return toga.Box(
            flex=1,
            margin=(0, 5, 0, 5),
            align_items='center',
            children=[
                toga.Box(children=[label], flex=1),
                toga.Box(children=[widget], flex=1),
            ],
        )

    def _create_selection(self, accessor: str) -> toga.Selection:
        """Create Selection with valid accessor."""
        if accessor not in self._accessors:
            raise RuntimeError(
                f"Gon invalid accessor name: '{accessor}'. "
                f'Available: {self._accessors}'
            )

        return toga.Selection(
            accessor='name',
            items=NamedEntitySource(),
            on_change=partial(self._on_select, accessor=accessor),
            flex=1,
        )

    # Source methods
    # --------------

    @override
    def change(self, accessor: str, value: object) -> None:
        """Change widget context via accessor.

        Widget must implement `items.update()` interface.
        """
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.items.update(value)

    def _on_select(self, selection: toga.Selection, accessor: str) -> None:
        self.notify('update', accessor=accessor, value=selection.value)
