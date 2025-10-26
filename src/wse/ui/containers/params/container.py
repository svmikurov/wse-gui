"""Params container."""

from dataclasses import dataclass
from typing import Any, override

import toga
from injector import inject

from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.content.mixins import GetContentMixin
from wse.utils.i18n import I18N

from . import ParamsContainerABC, ParamsContainerModelABC


@inject
@dataclass
class ParamsContainerModel(
    ObserverManagerGen[Any],
    ParamsContainerModelABC,
):
    """Params container model."""


@inject
@dataclass
class ParamsContainer(
    GetContentMixin,
    ParamsContainerABC,
):
    """Params container."""

    @override
    def _create_ui(self) -> None:
        self._count_label = toga.Label(I18N.LABEL('Word count'))
        self._count_select = toga.Selection(flex=1)
        self._mark_label = toga.Label(I18N.LABEL('Mark'))
        self._mark_select = toga.Selection(flex=1)

    @override
    def _populate_content(self) -> None:
        self._content.add(
            self._build_row(self.count_select, self.mark_select),
        )

    # Combined widgets
    # ----------------

    @property
    def count_select(self) -> toga.Box:
        """Word count select."""
        return self._combine_widgets(self._count_label, self._count_select)

    @property
    def mark_select(self) -> toga.Box:
        """Mark select."""
        return self._combine_widgets(self._mark_label, self._mark_select)

    # Utility methods
    # ---------------

    @staticmethod
    def _build_row(*children: toga.Widget) -> toga.Box:
        return toga.Box(children=children)

    @staticmethod
    def _combine_widgets(label: toga.Label, widget: toga.Widget) -> toga.Box:
        return toga.Box(
            flex=1,
            padding=(0, 5, 0, 5),
            align_items='center',
            children=[
                toga.Box(children=[label], flex=1),
                toga.Box(children=[widget], flex=1),
            ],
        )
