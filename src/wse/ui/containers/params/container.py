"""Params container."""

from dataclasses import dataclass
from functools import partial
from typing import Any, override

import toga
from injector import inject

from wse.config.layout import StyleConfig, ThemeConfig
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
    """Params container.

    To create Selection widget use ``_create_selection`` method.
    """

    _accessors = (
        'mark_select',
        'category_select',
        'count_input',
    )

    @override
    def _create_ui(self) -> None:
        self._category_label = toga.Label(I18N.LABEL('Category'))
        self._category_select = self._create_selection('category_select')
        self._mark_label = toga.Label(I18N.LABEL('Mark'))
        self._mark_select = self._create_selection('mark_select')
        self._count_label = toga.Label(I18N.LABEL('Count'))
        self._count_input = toga.NumberInput()

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self.select_category,
            self.select_mark,
            self.input_count,
        )

    @override
    def _update_style(self, config: StyleConfig | ThemeConfig) -> None:
        self._category_label.style.update(**config.params.label)
        self._category_select.style.update(**config.params.select)
        self._mark_label.style.update(**config.params.label)
        self._mark_select.style.update(**config.params.select)
        self._count_label.style.update(**config.params.label)
        self._count_input.style.update(**config.params.number)

    # Combined widgets
    # ----------------

    @property
    def select_category(self) -> toga.Box:
        """Word count select."""
        return self._combine(self._category_label, self._category_select)

    @property
    def select_mark(self) -> toga.Box:
        """Mark select."""
        return self._combine(self._mark_label, self._mark_select)

    @property
    def input_count(self) -> toga.Box:
        """Word count select."""
        return self._combine(self._count_label, self._count_input)

    # Utility methods
    # ---------------

    @staticmethod
    def _combine(label: toga.Label, widget: toga.Widget) -> toga.Box:
        """Combine into a labeled widget."""
        return toga.Box(
            children=[
                toga.Box(children=[label], flex=1),
                toga.Box(children=[widget], flex=1),
            ],
            margin=(2, 5, 2, 5),
            align_items='center',
            flex=1,
        )

    def _create_selection(self, accessor: str) -> toga.Selection:
        """Create Selection with valid accessor."""
        if accessor not in self._accessors:
            raise RuntimeError(
                f"Got invalid accessor name: '{accessor}'. "
                f'Available: {self._accessors}'
            )
        return toga.Selection(
            accessor='name',
            items=NamedEntitySource(),
            on_change=partial(self._on_select, accessor=accessor),
        )

    # Source methods
    # --------------

    @override
    def update(self, accessor: str, value: object) -> None:
        """Update widget context via accessor.

        Updated widget must implement ``items.update()`` Source
        interface.
        """
        ui = self._get_ui(accessor)
        with EventDisabler(ui):
            ui.items.update(value)

    def _on_select(self, selection: toga.Selection, accessor: str) -> None:
        self.notify('update', accessor=accessor, value=selection.value)
